import itertools
import json
import tweepy
from datetime import datetime
from time import sleep
import pytz
from pyjavaproperties import Properties
import os
import webbrowser
import urllib.parse


def get_current_date():
  return "02-20-2022"


def get_current_date_token():
  return get_current_date().replace("-", "")

# To set your enviornment variables in your terminal run the following line:
# MODE=open-tabs - it will open tabs for the next tweets. This is useful if your acount is still not approved
# MODE=tweet     - it will tweet based on the credentials provided as volume
# MODE=test      - it will run the tweet for the test
# MODE=list      - lists all the nfts
MODE = os.environ.get("MODE", "open-tabs")
TWEET_TEST_TIME = os.environ.get("TWEET_TEST_TIME", None)
if MODE == "test" and len(TWEET_TEST_TIME) != 6:
  TWEET_TEST_TIME = None
  MODE = "open-tabs"


# https://bitbucket.org/skeptichacker/pyjavaproperties/src/master/
def load_tweeter_credentials():
  # env vars as props
  props = Properties()
  
  # full path of the props
  # https://www.geeksforgeeks.org/python-os-path-expanduser-method/
  # https://github.com/piroor/tweet.sh/issues/35#issuecomment-1027806270
  tweeter_credentials_envs_path = os.path.expanduser('~/.tweet.client.key')
  
  # Load the properties from the file
  props.load(open(tweeter_credentials_envs_path))

  return props


# function to get unique values
def unique(times):
  # insert the list to the set
  list_set = set(times)
  
  # convert the set to the list
  unique_list = (list(list_set))
  return unique_list


def get_current_list():
  all_combinations = make_combinations() 

  # Remove all the elements before that time
  exclude_past_time(get_next_time(all_combinations), all_combinations)

  # return all the past values or the test one when provided
  return [TWEET_TEST_TIME] if TWEET_TEST_TIME else all_combinations


def make_combinations():
  # https://stackoverflow.com/questions/4928297/all-permutations-of-a-binary-sequence-x-bits-long/4928350#4928350
  full_product = ["".join(seq) for seq in itertools.product("000002", repeat=6)]

  # as they are combined, they will repeat, so let's make them unique
  full_product = unique(full_product)  
  full_product = full_product 

  # sort them all
  full_product.sort()
  return full_product


def exclude_past_time(last_viewed_time, all_times):
  index_from_last = -1

  # https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array/55034056#55034056
  for i, val in enumerate(all_times):
    if (val == last_viewed_time):
      index_from_last = i
      break

  # https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index/44353373#44353373
  del all_times[:index_from_last]


def get_time_from_token(time_token):
  # https://stackabuse.com/converting-strings-to-datetime-in-python/
  date_time_str = "%s %s" % (get_current_date(), get_tokenized_time(time_token))
  return datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')


def get_tokenized_time(specified_time):
  return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]


def get_next_time(current_list):
  # Get the current time and compare with the next avilable time
  current_time = datetime.now()

  last_seen_time = ""
  for prime_time in current_list:
    # Current time from the token
    time_from_token = get_time_from_token(prime_time)

    # Compare with the current time
    current_time = datetime.now()
    last_seen_time = prime_time

    print("Token %s  > Current time is %s" % (time_from_token, current_time))
    if time_from_token > current_time:
      break

  return last_seen_time


def make_current_time_token():
  # https://www.programiz.com/python-programming/datetime/current-datetime
  return datetime.now().strftime("%H%M%S")


def get_tokenized_time(specified_time):
  # Just format the time from 001122 => 00:11:22
  return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]


def wait_for_next_time(tweeter_credentials):
  # Get the next time from the current list

  print(f"All times list {get_current_list()}")

  for next_perfect_time in get_current_list():
    print("This is the next time: %s" % (get_tokenized_time(next_perfect_time)))

    # wait until the current time matches a unique time
    current_time = ""
    while current_time != next_perfect_time:
      current_time = make_current_time_token()

      # Now, it will break the time
      print(f"Current time: {get_current_date()} at {get_tokenized_time(current_time)}  Waiting for {get_current_date()} at {get_tokenized_time(next_perfect_time)}")

      # wait a couple of milliseconds
      sleep(0.4)

    # Attemtp to send the tweet at this specified time
    tweet_at_perfect_time(tweeter_credentials, next_perfect_time)


def tweet_at_perfect_time(tweeter_credentials, perfect_time):
  # Generate the hash tag based on the time
  hash_tag = "#" + get_tokenized_time(perfect_time)

  print("")
  print("########### Unique ##########")
  print("")
  print("* Will tweet at %s" % get_tokenized_time(perfect_time))
  print("")

  full_time = f"{get_current_date_token()}{perfect_time}"

  date_original_format = get_current_date().replace("-", "/")

  # This is the message to be tweeted
  perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {get_tokenized_time(perfect_time)}: only 2 digits on its representation! 🤖 My creator @marcellodesales told me to watch for palindrome times! This will also go to #blockchain #IPFS ⛓ #forever #nft #timecapsule #nft{full_time} #{full_time}"

  if is_time_palindrome(full_time):
    perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {get_tokenized_time(perfect_time)}: only 2 digits on its representation! 🤖 Look, @marcellodesales! I found the legendary #palindrome time 👑! This will also go to #blockchain #IPFS ⛓ #forever #nft #timecapsule #nft{full_time} #{full_time}"

  try:
    print("=---> Twitting: '%s'" % (perfect_timed_msg))
    print("")
    tweet(tweeter_credentials, perfect_timed_msg)
    print("Success!!!")

  except Exception as err:
    print("An exception occurred while sending tweet: %s" % err)

def authenticate_on_twitter_env(tweeter_credentials):
  # This is enabled by setting the keys 
  # https://developer.twitter.com/en/portal/projects/1488768050035773444/apps/23291738/auth-settings
  # ATTENTION: The key must be re-generated when the environment is re-created. Make sure to choose production!
  auth = tweepy.OAuth1UserHandler(
    tweeter_credentials["CONSUMER_KEY"], tweeter_credentials["CONSUMER_SECRET"],
    tweeter_credentials["ACCESS_TOKEN"], tweeter_credentials["ACCESS_TOKEN_SECRET"]
  )

  # Create API object
  return tweepy.API(auth)


def tweet(tweeter_credentials, status_message):
  api = authenticate_on_twitter_env(tweeter_credentials)

  # Create a tweet
  api.update_status(status_message)


def is_time_palindrome(time):
    # https://www.geeksforgeeks.org/python-list/
    return time == time[::-1]


def find_my_nft_tweets(tweeter_credentials):
  api = authenticate_on_twitter_env(tweeter_credentials)

  # TODO: The logged user is on the credentials, so maybe get it from there?
  logged_user = tweeter_credentials["MY_SCREEN_NAME"]

  # https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators
  query = "from:%s \"This is the unique tweet\"" % logged_user
  public_tweets = api.search_tweets(count=50, q=query, result_type="recent",
                                    since_id="1484063267618127872", include_entities=True)

  # tweet is the status object: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
  for tweet in public_tweets:
    url = "https://twitter.com/%s/status/%s" % (logged_user, tweet.id)

    # https://stackoverflow.com/questions/10494312/parsing-time-string-in-python/10494427#10494427
    # https://docs.python.org/3/library/time.html#time.strptime
    # output is "2022-02-02 08:22:19+00:00"
    #created_time = datetime.strptime(tweet.created_at, '%Y-%m-%d %I:%M:%S%z')

    # Military time formatter
    # https://stackoverflow.com/questions/10997577/python-timezone-conversion/62947906#62947906
    time_only = tweet.created_at.astimezone(pytz.timezone('America/Los_Angeles')).strftime("%H:%M:%S")
    
    # Verify if the tweet was sent at the exact h:m:s 
    # This is the unique tweet at 02/02/2022 at 00:22:20
    attempt_perfect_time = tweet.text.split("at")[2].split(" ")[1].replace(".", "")
    matched_time = "🎯" if time_only == attempt_perfect_time else "❌"

    # Define rarity if the time created on the server is a palindrome!
    full_date_time = tweet.created_at.astimezone(pytz.timezone('America/Los_Angeles')).strftime("%m%d%Y%I%M%S")
    print("Full time %s" % full_date_time)
    time_rarity = "👑" if is_time_palindrome(full_date_time) else ""

    print("%s%s [%s] @ %s: %s" % (time_rarity, matched_time, time_only, url, tweet.text))


def print_json_list():
  # Genetate the full list
  full_list = get_current_list()
  print(json.dumps(full_list))


def open_tweet_tabs():
  print("Will open tabs for your timely tweets...")

  for next_perfect_time in get_current_list():
    print("This is the next time: %s" % (get_tokenized_time(next_perfect_time)))
    
    hash_tag = "#" + get_tokenized_time(next_perfect_time)

    print("")
    print("########### Unique !!!!! ----")
    print("")
    print("* Will tweet at %s" % (get_tokenized_time(next_perfect_time)))
    print("")
    perfect_timed_msg = "This is the unique tweet at 02/02/2022 at %s. #nft #timecapsule #nft02022022%s" % (get_tokenized_time(next_perfect_time), next_perfect_time)

    # wait a couple of milliseconds
    sleep(3)
 
    try:
      print("=---> Twitting: '%s'" % (perfect_timed_msg))
      # https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python/9345102#9345102
      tweet_url = "https://twitter.com/compose/tweet?text=%s" % urllib.parse.quote_plus(perfect_timed_msg)

      # https://stackoverflow.com/questions/24382738/open-twitter-url-with-app-instead-of-browser
      # https://elearning.wsldp.com/python3/python-open-web-browser/
      print("Opening on browser %s" % tweet_url)
      webbrowser.get("firefox").open(tweet_url)

      print("Success!!!")

    except Exception as err:
      print("An exception occurred while sending tweet: %s" % err)

  print("Finished with all the tweets to open tabs!")     

def main():
  if MODE == "open-tabs":
    open_tweet_tabs()

  elif MODE == "list":
    tweeter_credentials = load_tweeter_credentials()
    find_my_nft_tweets(tweeter_credentials)

  else:
    tweeter_credentials = load_tweeter_credentials()
    wait_for_next_time(tweeter_credentials)

  print("")
  print("Finished attempting to tweets")
  #print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()

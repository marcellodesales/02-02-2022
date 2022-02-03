import itertools
import json
import tweepy
from datetime import datetime
from time import sleep
from pyjavaproperties import Properties
import os
import webbrowser
import urllib.parse


# To set your enviornment variables in your terminal run the following line:
# MODE=open-tabs - it will open tabs for the next tweets. This is useful if your acount is still not approved
# MODE=tweet - it will tweet based on the credentials provided as volume
MODE = os.environ.get("MODE", "open-tabs")

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
def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list

def get_current_list():
  all_combinations = make_combinations() 
  print(all_combinations)

  # Remove all the elements before that time
  exclude_past_time(get_next_time(all_combinations), all_combinations)

  # exclude all the past values
  return all_combinations

def make_combinations():
  # https://stackoverflow.com/questions/4928297/all-permutations-of-a-binary-sequence-x-bits-long/4928350#4928350
  full_product = ["".join(seq) for seq in itertools.product("000002", repeat=6)]

  full_product = unique(full_product)
  
  full_product = full_product + ["151940"]

  full_product.sort()

  return full_product

def exclude_past_time(last_viewed_time, all_times):
  index_from_last = -1
  for i, val in enumerate(all_times):
    if (val == last_viewed_time):
      index_from_last = i
      break

  # https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index/44353373#44353373
  del all_times[:index_from_last]

def get_time_from_token(time_token):
  # https://stackabuse.com/converting-strings-to-datetime-in-python/
  date_time_str = "02-02-2022 %s" % (get_tokenized_time(time_token))
  return datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')

def get_tokenized_time(specified_time):
  return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]

def get_next_time(current_list):
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

def print_json_list():
  # Genetate the full list
  full_list = get_current_list()

  print(json.dumps(full_list))

def make_current_time_token():
  # https://www.programiz.com/python-programming/datetime/current-datetime
  return datetime.now().strftime("%H%M%S")

def get_tokenized_time(specified_time):
  return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]

def wait_for_next_time(tweeter_credentials):
  for next_perfect_time in get_current_list():
    print("This is the next time: %s" % (get_tokenized_time(next_perfect_time)))
    
    # wait until the current time matches a unique time
    current_time = ""
    while current_time != next_perfect_time:
      current_time = make_current_time_token()

      # Now, it will break the time
      print("Current time: 02/02/2022 at %s  Waiting for 02/02/2022 at %s" % (get_tokenized_time(current_time), get_tokenized_time(next_perfect_time)))

      # wait a couple of milliseconds
      sleep(0.4)
    
    tweet_at_perfect_time(tweeter_credentials, next_perfect_time)
     
def tweet_at_perfect_time(tweeter_credentials, perfect_time):
  hash_tag = "#" + get_tokenized_time(perfect_time)

  print("")
  print("########### Unique !!!!! ----")
  print("")

  print("* Will tweet at %s" % (get_tokenized_time(perfect_time)))

  print("")
  
  perfect_timed_msg = "This is the unique tweet at 02/02/2022 at %s. #02022022%s" % (get_tokenized_time(perfect_time), perfect_time)

  print("=---> Twitting: '%s'" % (perfect_timed_msg))
  print("")

  tweet(tweeter_credentials, perfect_timed_msg)
  
def tweet(tweeter_credentials, status_message):
  # Authenticate to Twitter
  auth = tweepy.OAuthHandler(tweeter_credentials["CONSUMER_KEY"], tweeter_credentials["CONSUMER_SECRET"])
  auth.set_access_token(tweeter_credentials["ACCESS_TOKEN"], tweeter_credentials["ACCESS_TOKEN_SECRET"])

  # Create API object
  api = tweepy.API(auth)

  # Create a tweet
  api.update_status(status_message)

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

# print next times
#print_json_list()

if MODE == "open-tabs":
  open_tweet_tabs()

else:
  tweeter_credentials = load_tweeter_credentials()
  wait_for_next_time(tweeter_credentials)

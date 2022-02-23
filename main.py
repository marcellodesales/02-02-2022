from time import sleep
import os
import webbrowser
import urllib.parse
import random

from supercash.platform.blockchain.ipfs_proxy_client import IPFSClientProxy
from supercash.platform.messaging.twitter_proxy_client import TwitterProxyClient
from supercash.platform.scheduler.prime_time_calculator import PrimeTimeCalculator
from supercash.platform.scheduler.alarm_scheduler import AlarmScheduler


def get_tokenized_time(specified_time):
  # Just format the time from 001122 => 00:11:22
  return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]


def wait_for_next_time_after_delay(ipfs_client_proxy, twitter_proxy_client, prime_time_calculator):
  # Get the next time from the current list

  # This is when the bot missed the appointment at 00h-2am
  delayed = True
  current_delayed_list  = prime_time_calculator.get_current_list(delayed)
  print(f"All delayed time list {current_delayed_list}")

  for next_perfect_time in current_delayed_list:
    print("This is the next time: %s" % (get_tokenized_time(next_perfect_time)))

    # wait until the current time matches a unique time
    # current_time = ""
    # while current_time != next_perfect_time:
    current_time = next_perfect_time

    # Now, it will break the time
    print(f"Current time: {AlarmScheduler.get_current_date()} at {get_tokenized_time(current_time)}  Waiting for {AlarmScheduler.get_current_date()} at {get_tokenized_time(next_perfect_time)}")

    # wait a couple of milliseconds https://pynative.com/python-random-randrange/
    wait_seconds = random.randrange(5, 20)
    print(f"=> Waiting {wait_seconds}s")
    sleep(wait_seconds)

    # Attemtp to send the tweet at this specified time
    tweet_at_perfect_time(ipfs_client_proxy, twitter_proxy_client, next_perfect_time)

def wait_for_next_time(ipfs_client_proxy, twitter_proxy_client, prime_time_calculator):
  # Get the next time from the current list

  current_list  = prime_time_calculator.get_current_list()
  print(f"All times list {current_list}")

  for next_perfect_time in current_list:
    print("This is the next time: %s" % (get_tokenized_time(next_perfect_time)))

    # wait until the current time matches a unique time
    current_time = ""
    while current_time != next_perfect_time:
      current_time = AlarmScheduler.make_current_time_token()

      # Now, it will break the time
      print(f"Current time: {AlarmScheduler.get_current_date()} at {get_tokenized_time(current_time)}  Waiting for {AlarmScheduler.get_current_date()} at {get_tokenized_time(next_perfect_time)}")

      # wait a couple of milliseconds
      sleep(0.4)

    # Attempt to send the tweet at this specified time
    tweet_at_perfect_time(ipfs_client_proxy, twitter_proxy_client, next_perfect_time)


def write_file(time, tweet_message):
    file_path = f"logs/{time}.tweet"
    print(f"Saving tweet to local file-system at {file_path}")
    f = open(file_path, "a")
    f.write(tweet_message)
    f.close()

    tweet_message_file_size = os.stat(file_path).st_size
    print(f"Saved '{tweet_message_file_size}' bytes of the tweet message to local file-system at '{file_path}'")
    return file_path


def send_to_ipfs(ipfs_client_proxy, time, tweet_message):
    # https://discuss.ipfs.io/t/how-to-add-multiple-files-not-a-directory-with-one-api-request/998/2
    tweet_message_local_file_path = write_file(time, tweet_message)

    print(f"Connecting to IPFS to persist the tweet!")
    tweet_ipfs_cid_hash = ipfs_client_proxy.add_file_to_ipfs(tweet_message_local_file_path)

    # Get the hash to be returned!
    print(f"Recorded tweet from {time} to IPFS as CID: {tweet_ipfs_cid_hash}")

    persisted_ipfs_tweet_msg = ipfs_client_proxy.retrieve_file_content_by_cid(tweet_ipfs_cid_hash)
    print(f"IPFS message: {persisted_ipfs_tweet_msg}")

    # Validate first if it was correctly sent!
    if persisted_ipfs_tweet_msg != tweet_message:
        # When saving in IPFS, the string is encoded and so are the emojis
        print(f"WARNING: tweet message '{tweet_message}' was retrieved from IPFS differently as '{persisted_ipfs_tweet_msg}': Emojis encoded?")

    print(f"The same tweet was saved in the ⛓️ blockchain IFPS CID={tweet_ipfs_cid_hash}")
    print(f"Explore the message after IPFS replication: https://webui.ipfs.io/#/ipfs/{tweet_ipfs_cid_hash}")
    return tweet_ipfs_cid_hash


def make_tweet_message(date_original_format, perfect_time, full_time, tweet_cid=None):
  # TODO: Add #late if in late mode
  if tweet_cid:
    # This is the message to be tweeted
    perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {get_tokenized_time(perfect_time)} represented with only 2 digits 🤖 As asked by my creator @marcellodesales, I've saved it in the blockchain! 🕑 #timecapsule #{full_time} #IPFS #nft ⛓ #cid_{tweet_cid}"

    if is_time_palindrome(full_time):
      perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {get_tokenized_time(perfect_time)} represented with only 2 digits 🤖 Look @marcellodesales, I found the legendary #palindrome time 👑! Saved it on the #blockchain ⛓ #IPFS #nft #timecapsule #nft{full_time} #{full_time}"

  else:
    # This is the message to be tweeted
    perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {get_tokenized_time(perfect_time)} only 2 digits on its representation! 🤖 My creator @marcellodesales told me to watch for palindrome times! This will also go to #blockchain ⛓ #IPFS #nft #timecapsule #nft{full_time} #{full_time}"

    if is_time_palindrome(full_time):
      perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {get_tokenized_time(perfect_time)} only 2 digits on its representation! 🤖 Look, @marcellodesales! I found the legendary #palindrome time 👑! This will also go to #blockchain ⛓ #IPFS #nft #timecapsule #nft{full_time} #{full_time}"

  return perfect_timed_msg


def tweet_at_perfect_time(ipfs_client_proxy, twitter_proxy_client, perfect_time):
  # Generate the hash tag based on the time
  hash_tag = "#" + get_tokenized_time(perfect_time)

  # TODO: Correlate the tweet with IPFS after by using a folder!

  print("")
  print("########### Unique ##########")
  print("")
  print("* Will tweet at %s" % get_tokenized_time(perfect_time))
  print("")

  full_time = f"{AlarmScheduler.get_current_date_token()}{perfect_time}"

  # Format the value for better display
  date_original_format = AlarmScheduler.get_current_date().replace("-", "/")

  # the tweet message
  perfect_timed_msg = make_tweet_message(date_original_format, perfect_time, full_time)

  tweet_ipfs_cid = None
  try:
    print("")
    print("Writing the tweet 🐦 to the Blockchain ⛓️ (IPFS)")
    tweet_ipfs_cid = send_to_ipfs(ipfs_client_proxy, full_time, perfect_timed_msg)
    print(f"IPFS Success: tweet CID={tweet_ipfs_cid}")

  except Exception as err:
    print("An exception occurred while persisting tweet in IPFS: %s" % err)

  # Update the message with the IPFS CID of the tweet as a proof of record
  perfect_timed_msg_with_cid = make_tweet_message(date_original_format, perfect_time, full_time, tweet_ipfs_cid)

  try:
    print("=---> Twitting: '%s'" % perfect_timed_msg_with_cid)
    print("")
    twitter_proxy_client.tweet(perfect_timed_msg_with_cid)
    print("Tweet Success!!!")

  except Exception as err:
    print("An exception occurred while sending tweet: %s" % err)


def is_time_palindrome(time):
    # https://www.geeksforgeeks.org/python-list/
    return time == time[::-1]


def open_tweet_tabs():
  print("Will open tabs for your timely tweets...")

  for next_perfect_time in PrimeTimeCalculator.get_current_list():
    print("This is the next time: %s" % (get_tokenized_time(next_perfect_time)))

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

  # Just course correction if the bot is sleeping
  MISSED_TIME = False

  # Configure the twitter client based on the config file
  tweepy_config = '~/.tweet.client.key'
  twitter_proxy_client = TwitterProxyClient(tweepy_config)

  if MODE == "open-tabs":
    open_tweet_tabs()

  elif MODE == "list":
    twitter_proxy_client.find_my_nft_tweets()

  else:
    # Since python version is not working with the latest version
    # connect to an instance that is compatible
    ipfs_client_proxy = IPFSClientProxy.make_compatible_version_client()
    print("=======  Sending tweets backed by IPFS ========")
    print("")
    print(f"* HOST: {ipfs_client_proxy.host}")
    print(f"* PORT: {ipfs_client_proxy.port}")
    print("")

    prime_time_calculator = PrimeTimeCalculator(TWEET_TEST_TIME)

    if MISSED_TIME:
      wait_for_next_time_after_delay(ipfs_client_proxy, twitter_proxy_client, prime_time_calculator)

    else:
      wait_for_next_time(ipfs_client_proxy, twitter_proxy_client, prime_time_calculator)

  print("")
  print("Finished attempting to tweets")
  #print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()

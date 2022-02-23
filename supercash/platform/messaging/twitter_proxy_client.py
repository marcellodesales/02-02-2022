# Copyright Supercash Labs.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tweepy
from supercash.platform.config.properties_file_config import PropertiesFileConfig
import pytz

class TwitterProxyClient:
    """Application Logger for the application to log anything to the stdout"""

    def __init__(self, tweepy_config_file_path):
        """ default properties for IPFS """
        self.tweepy_config_file_path = tweepy_config_file_path
        self.props = PropertiesFileConfig(tweepy_config_file_path).props

    def get_credentials(self):
        return self.props

    def authenticate_on_twitter_env(self):
        # This is enabled by setting the keys
        # https://developer.twitter.com/en/portal/projects/1488768050035773444/apps/23291738/auth-settings
        # ATTENTION: The key must be re-generated when the environment is re-created. Make sure to choose production!
        auth = tweepy.OAuth1UserHandler(
            self.props["CONSUMER_KEY"], self.props["CONSUMER_SECRET"],
            self.props["ACCESS_TOKEN"], self.props["ACCESS_TOKEN_SECRET"]
        )

        # Create API object
        return tweepy.API(auth)

    def find_my_nft_tweets(self):
        api = self.authenticate_on_twitter_env()

        # TODO: The logged user is on the credentials, so maybe get it from there?
        twitter_credentials = self.get_credentials()
        logged_user = twitter_credentials["MY_SCREEN_NAME"]

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
            # created_time = datetime.strptime(tweet.created_at, '%Y-%m-%d %I:%M:%S%z')

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
            time_rarity = "👑" if self.is_time_palindrome(full_date_time) else ""

            print("%s%s [%s] @ %s: %s" % (time_rarity, matched_time, time_only, url, tweet.text))

    def tweet(self, status_message):
      api = self.authenticate_on_twitter_env()

      # Create a tweet
      tweet_response = api.update_status(status_message)
      tweet_id = tweet_response.id_str
      logged_user = self.props["MY_SCREEN_NAME"]
      tweet_url = f"https://twitter.com/{logged_user}/status/{tweet_id}"
      print(f"Tweed saved at {tweet_url}")


    def is_time_palindrome(time):
        # https://www.geeksforgeeks.org/python-list/
        return time == time[::-1]

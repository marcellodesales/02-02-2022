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

from supercash.platform.util.date_formatter import DateFormatter


class TwitterMessageFormatter:
    """Application Logger for the application to log anything to the stdout"""

    @staticmethod
    def is_time_palindrome(time):
        # https://www.geeksforgeeks.org/python-list/
        return time == time[::-1]

    @staticmethod
    def make_tweet_message(date_original_format, perfect_time, full_time, tweet_cid=None):
        # TODO: Add #late if in late mode
        if tweet_cid:
            # This is the message to be tweeted
            perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {DateFormatter.get_tokenized_time(perfect_time)} represented with only 2 digits 🤖 As asked by my creator @marcellodesales, I've saved it in the #blockchain! 🕑 #timecapsule #{full_time} #IPFS #nft ⛓ #cid_{tweet_cid}"

            if TwitterMessageFormatter.is_time_palindrome(full_time):
                perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {DateFormatter.get_tokenized_time(perfect_time)} represented with only 2 digits 🤖 Look @marcellodesales, I found the legendary #palindrome time 👑! Saved it on the #blockchain ⛓ #IPFS #nft #timecapsule #nft{full_time} #{full_time}"

        else:
            # This is the message to be tweeted
            perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {DateFormatter.get_tokenized_time(perfect_time)} only 2 digits on its representation! 🤖 My creator @marcellodesales told me to watch for palindrome times! This will also go to #blockchain ⛓ #IPFS #nft #timecapsule #nft{full_time} #{full_time}"

            if TwitterMessageFormatter.is_time_palindrome(full_time):
                perfect_timed_msg = f"This is a rare tweet time capsule on 📅 {date_original_format} at ⏰ {DateFormatter.get_tokenized_time(perfect_time)} only 2 digits on its representation! 🤖 Look, @marcellodesales! I found the legendary #palindrome time 👑! This will also go to #blockchain ⛓ #IPFS #nft #timecapsule #nft{full_time} #{full_time}"

        return perfect_timed_msg

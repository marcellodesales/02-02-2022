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

from datetime import datetime


class AlarmScheduler:
    """Application Logger for the application to log anything to the stdout"""

    def __init__(self):
        """ default properties for IPFS """

    # function to get unique values
    @staticmethod
    def get_next_time(current_list):
        """" Get the current time and compare with the next avilable time """

        last_seen_time = ""
        for prime_time in current_list:
            # Current time from the token
            time_from_token = AlarmScheduler.get_time_from_token(prime_time)

            # Compare with the current time
            current_time = datetime.now()
            last_seen_time = prime_time

            print("Token %s  > Current time is %s" % (time_from_token, current_time))
            if time_from_token > current_time:
                break

        return last_seen_time

    @staticmethod
    def get_current_date():
        return "02-22-2022"

    @staticmethod
    def get_time_from_token(time_token):
        # https://stackabuse.com/converting-strings-to-datetime-in-python/
        date_time_str = "%s %s" % (AlarmScheduler.get_current_date(), AlarmScheduler.get_tokenized_time(time_token))
        return datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')

    @staticmethod
    def get_tokenized_time(specified_time):
        return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]

    @staticmethod
    def get_current_date_token():
        return AlarmScheduler.get_current_date().replace("-", "")

    @staticmethod
    def make_current_time_token():
      # https://www.programiz.com/python-programming/datetime/current-datetime
      return datetime.now().strftime("%H%M%S")


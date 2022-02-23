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

import itertools
import json
from supercash.platform.scheduler.alarm_scheduler import AlarmScheduler


class PrimeTimeCalculator:
    """Application Logger for the application to log anything to the stdout"""

    def __init__(self, tweet_test_time):
        """ default properties for IPFS """
        self.tweet_test_time = tweet_test_time

    # function to get unique values
    @staticmethod
    def unique(times):
        # insert the list to the set
        list_set = set(times)

        # convert the set to the list
        unique_list = (list(list_set))
        return unique_list

    def get_current_list(self, missed_time=False):
        all_combinations = PrimeTimeCalculator.make_combinations()

        # Remove all the elements before that time
        PrimeTimeCalculator.exclude_past_time(AlarmScheduler.get_next_time(all_combinations), all_combinations)

        # For missed entries, use the set to fix it case
        if missed_time:
            return ['000000', '000002', '000020', '000022', '000200', '000202', '000220', '000222', '002000',
                    '002002', '002020', '002022', '002200', '002202', '002220', '002222', '020000', '020002', '020020',
                    '020022', '020200', '020202', '020220', '020222', '022000', '022002', '022020', '022022', '022200',
                    '022202', '022220', '022222']

        # return all the past values or the test one when provided
        return [self.tweet_test_time] if self.tweet_test_time else all_combinations

    @staticmethod
    def make_combinations():
        # https://stackoverflow.com/questions/4928297/all-permutations-of-a-binary-sequence-x-bits-long/4928350#4928350
        full_product = ["".join(seq) for seq in itertools.product("000002", repeat=6)]

        # as they are combined, they will repeat, so let's make them unique
        full_product = PrimeTimeCalculator.unique(full_product)
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


    def print_json_list(self):
      # Genetate the full list
      full_list = self.get_current_list()
      print(json.dumps(full_list))
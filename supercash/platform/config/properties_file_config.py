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

from pyjavaproperties import Properties
import os


class PropertiesFileConfig:
    """Application Logger for the application to log anything to the stdout"""

    def __init__(self, config_file_path):
        """ default properties for IPFS """
        self.config_file_path = config_file_path
        self.props = self._load()

    # https://bitbucket.org/skeptichacker/pyjavaproperties/src/master/
    def _load(self):
        # env vars as props
        props = Properties()

        # full path of the props
        # https://www.geeksforgeeks.org/python-os-path-expanduser-method/
        # https://github.com/piroor/tweet.sh/issues/35#issuecomment-1027806270
        _envs_path = os.path.expanduser(self.config_file_path)

        # Load the properties from the file
        props.load(open(_envs_path))

        return props

    def get_props(self):
        return self.props

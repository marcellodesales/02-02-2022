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

import os


class FileUtil:
    """Application Logger for the application to log anything to the stdout"""

    @staticmethod
    def write_content_to_file_path(content, file_path):
        f = open(file_path, "a")
        f.write(content)
        f.close()

    @staticmethod
    def get_file_fize(file_path):
        return os.stat(file_path).st_size
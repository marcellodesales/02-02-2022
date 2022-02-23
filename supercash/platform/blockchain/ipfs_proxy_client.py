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
import ipfshttpclient


class IPFSClientProxy:
    """Application Logger for the application to log anything to the stdout"""

    def __init__(self):
        """ default setting for IPFS """
        self("localhost", "5001")
        # self.host = "localhost"
        # self.port = "5001"

    def __init__(self, host: str, port: int):
        """ Constructs a new logger instance with the provided context name. """
        self.host = host
        self.port = port
        self._ipfs_client = self._connect()

    def _connect(self):
        # Make sure the IPFS service is running at the configred values
        return ipfshttpclient.connect(addr=f"/dns/{self.host}/tcp/{self.port}/http")

    @staticmethod
    def make_compatible_version_client():
        """ Makes an instance with the default compatible verison host """
        # Just run against an IPFS server running a compatible version
        # docker ps | grep 15001
        # 5c316d790864   ipfs/go-ipfs:v0.7.0 "/sbin/tini -- /usr/…"   49 seconds ago   Up 47 seconds
        # 0.0.0.0:14001->4001/tcp, 0.0.0.0:14001->4001/udp, 0.0.0.0:15001->5001/tcp, 0.0.0.0:18080->8080/tcp, 0.0.0.0:18081->8081/tcp
        return IPFSClientProxy("localhost", 15001)

    def add_file_to_ipfs(self, local_file_path):
        tweet_ipfs_response = self._ipfs_client.add(local_file_path)

        # Get the hash to be returned!
        file_hash_cid = tweet_ipfs_response['Hash']

        # TODO: Validate
        return file_hash_cid

    def retrieve_file_content_by_cid(self, file_hash_cid):
        return self._ipfs_client.cat(file_hash_cid)
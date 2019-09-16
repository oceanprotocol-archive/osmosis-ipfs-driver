#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
import os

from osmosis_driver_interface.data_plugin import AbstractPlugin


class Plugin(AbstractPlugin):
    IPFS_GATEWAY_ENVVAR = 'IPFS_GATEWAY'
    DEFAULT_IPFS_GATEWAY = 'gateway.ipfs.io/ipfs'
    PROTOCOL = 'ipfs://'

    def __init__(self, config=None):
        self.config = config
        self._ipfs_gateway = os.getenv(Plugin.IPFS_GATEWAY_ENVVAR, Plugin.DEFAULT_IPFS_GATEWAY)

    def type(self):
        """str: the type of this plugin (``'IPFS'``)"""
        return 'IPFS'

    def upload(self, local_file, remote_file):
        pass

    def download(self, remote_file, local_file):
        pass

    def list(self, remote_folder):
        pass

    def generate_url(self, remote_file):
        cid = remote_file.split('ipfs://')[1]
        url = f'{self._ipfs_gateway}/ipfs/{cid}'
        return url

    def delete(self, remote_file):
        pass

    def copy(self, source_path, dest_path):
        pass

    def create_directory(self, remote_folder):
        pass

    def retrieve_availability_proof(self):
        pass

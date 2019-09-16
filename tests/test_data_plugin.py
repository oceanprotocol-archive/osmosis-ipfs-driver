#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from osmosis_ipfs_driver.data_plugin import Plugin

osmo = Plugin()


def test_copy_file():
    assert osmo.type() == 'IPFS'


def test_list():
    pass


def test_files_share():
    pass


def test_split_url():
    pass


def test_parse_file_url():
    pass

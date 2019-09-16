#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from osmosis_ipfs_driver.data_plugin import Plugin

osmo = Plugin()


def test_driver_type():
    assert osmo.type() == 'IPFS'


def test_list():
    pass


def test_split_url():
    pass


def test_parse_file_url():
    pass

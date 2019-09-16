#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
import pytest

from osmosis_ipfs_driver.data_plugin import Plugin

osmo = Plugin()


def test_driver_type():
    assert osmo.type() == 'IPFS'


def test_parse_url():
    # Invalid urls
    # None
    url = None
    with pytest.raises(AssertionError):
        osmo.parse_url(url)

    # Empty str
    url = ''
    with pytest.raises(AssertionError):
        osmo.parse_url(url)
    # str with no ipfs://
    url = 'ip://ZnOfotxMMnLTXCCW0GPVYT8gtEugghgD8Hgz'
    with pytest.raises(AssertionError):
        osmo.parse_url(url)

    cid = 'some-valid-ipfs-cid'
    url = f'ipfs://{cid}'
    assert osmo.parse_url(url) == cid


def test_generate_url():
    cid = 'some-valid-ipfs-cid'
    url = f'ipfs://{cid}'
    resolved_url = f'{osmo.DEFAULT_IPFS_GATEWAY}/ipfs/{self.parse_url(url)}'
    assert osmo.generate_url(url) == resolved_url

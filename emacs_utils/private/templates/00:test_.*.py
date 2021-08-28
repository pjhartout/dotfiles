#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_filename.py

***file description***

"""

import pytest

test_data = list()


@pytest.mark.parametrize("out1, out2, expected", sample_func)
def test_sample_func(arg1):
    """test sample func"""
    assert arg1 == "test"

# -*- coding: utf-8 -*-
from __future__ import absolute_import

# reset the variables counter before running tests
def setup_module(module):
    from coffeehouse_nlpfr.sem import logic

    logic._counter._value = 0

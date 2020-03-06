# -*- coding: utf-8 -*-
from __future__ import absolute_import


def setup_module(module):
    from nose import SkipTest
    import coffeehouse_nlpfr.data

    try:
        coffeehouse_nlpfr.data.find("corpora/childes/data-xml/Eng-USA-MOR/")
    except LookupError as e:
        print(e)
        raise SkipTest(
            "The CHILDES corpus is not found. "
            "It should be manually downloaded and saved/unpacked "
            "to [NLTK_Data_Dir]/corpora/childes/"
        )

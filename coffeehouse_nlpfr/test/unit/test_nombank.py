# -*- coding: utf-8 -*-
"""
Unit tests for coffeehouse_nlpfr.corpus.nombank
"""

from __future__ import unicode_literals
import unittest

from coffeehouse_nlpfr.corpus import nombank
# Load the nombank once.
nombank.nouns()

class NombankDemo(unittest.TestCase):
    def test_numbers(self):
        # No. of instances.
        self.assertEqual(len(nombank.instances()), 114574)
        # No. of rolesets
        self.assertEqual(len(nombank.rolesets()), 5577)
        # No. of nouns.
        self.assertEqual(len(nombank.nouns()), 4704)


    def test_instance(self):
        self.assertEqual(nombank.instances()[0].roleset, 'perc-sign.01')

    def test_framefiles_fileids(self):
        self.assertEqual(len(nombank.fileids()), 4705)
        self.assertTrue(all(fileid.endswith('.xml') for fileid in nombank.fileids()))

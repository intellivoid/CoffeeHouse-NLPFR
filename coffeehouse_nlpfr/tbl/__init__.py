# -*- coding: utf-8 -*-
# Natural Language Toolkit: Transformation-based learning
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Marcus Uneson <marcus.uneson@gmail.com>
#   based on previous (nltk2) version by
#   Christopher Maloof, Edward Loper, Steven Bird
# URL: <http://nltk.org/>
# For license information, see  LICENSE.TXT

"""
Transformation Based Learning

A general purpose package for Transformation Based Learning,
currently used by coffeehouse_nlpfr.tag.BrillTagger.
"""

from coffeehouse_nlpfr.tbl.template import Template

# API: Template(...), Template.expand(...)

from coffeehouse_nlpfr.tbl.feature import Feature

# API: Feature(...), Feature.expand(...)

from coffeehouse_nlpfr.tbl.rule import Rule

# API: Rule.format(...), Rule.templatetid

from coffeehouse_nlpfr.tbl.erroranalysis import error_list

# Natural Language Toolkit: Stemmers
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Trevor Cohn <tacohn@cs.mu.oz.au>
#         Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK Stemmers

Interfaces used to remove morphological affixes from words, leaving
only the word stem.  Stemming algorithms aim to remove those affixes
required for eg. grammatical role, tense, derivational morphology
leaving only the stem of the word.  This is a difficult problem due to
irregular words (eg. common verbs in English), complicated
morphological rules, and part-of-speech and sense ambiguities
(eg. ``ceil-`` is not the stem of ``ceiling``).

StemmerI defines a standard interface for stemmers.
"""

from coffeehouse_nlpfr.stem.api import StemmerI
from coffeehouse_nlpfr.stem.regexp import RegexpStemmer
from coffeehouse_nlpfr.stem.lancaster import LancasterStemmer
from coffeehouse_nlpfr.stem.isri import ISRIStemmer
from coffeehouse_nlpfr.stem.porter import PorterStemmer
from coffeehouse_nlpfr.stem.snowball import SnowballStemmer
from coffeehouse_nlpfr.stem.wordnet import WordNetLemmatizer
from coffeehouse_nlpfr.stem.rslp import RSLPStemmer
from coffeehouse_nlpfr.stem.cistem import Cistem

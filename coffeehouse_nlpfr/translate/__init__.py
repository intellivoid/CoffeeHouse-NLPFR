# -*- coding: utf-8 -*-
# Natural Language Toolkit: Machine Translation
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>, Tah Wei Hoon <hoon.tw@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Experimental features for machine translation.
These interfaces are prone to change.
"""

from coffeehouse_nlpfr.translate.api import AlignedSent, Alignment, PhraseTable
from coffeehouse_nlpfr.translate.ibm_model import IBMModel
from coffeehouse_nlpfr.translate.ibm1 import IBMModel1
from coffeehouse_nlpfr.translate.ibm2 import IBMModel2
from coffeehouse_nlpfr.translate.ibm3 import IBMModel3
from coffeehouse_nlpfr.translate.ibm4 import IBMModel4
from coffeehouse_nlpfr.translate.ibm5 import IBMModel5
from coffeehouse_nlpfr.translate.bleu_score import sentence_bleu as bleu
from coffeehouse_nlpfr.translate.ribes_score import sentence_ribes as ribes
from coffeehouse_nlpfr.translate.meteor_score import meteor_score as meteor
from coffeehouse_nlpfr.translate.metrics import alignment_error_rate
from coffeehouse_nlpfr.translate.stack_decoder import StackDecoder

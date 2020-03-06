# Natural Language Toolkit: Inference
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Dan Garrette <dhgarrette@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
#
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Classes and interfaces for theorem proving and model building.
"""

from coffeehouse_nlpfr.inference.api import ParallelProverBuilder, ParallelProverBuilderCommand
from coffeehouse_nlpfr.inference.mace import Mace, MaceCommand
from coffeehouse_nlpfr.inference.prover9 import Prover9, Prover9Command
from coffeehouse_nlpfr.inference.resolution import ResolutionProver, ResolutionProverCommand
from coffeehouse_nlpfr.inference.tableau import TableauProver, TableauProverCommand
from coffeehouse_nlpfr.inference.discourse import (
    ReadingCommand,
    CfgReadingCommand,
    DrtGlueReadingCommand,
    DiscourseTester,
)

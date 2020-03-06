# Natural Language Toolkit: Metrics
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
#

"""
NLTK Metrics

Classes and methods for scoring processing modules.
"""

from coffeehouse_nlpfr.metrics.scores import (
    accuracy,
    precision,
    recall,
    f_measure,
    log_likelihood,
    approxrand,
)
from coffeehouse_nlpfr.metrics.confusionmatrix import ConfusionMatrix
from coffeehouse_nlpfr.metrics.distance import (
    edit_distance,
    edit_distance_align,
    binary_distance,
    jaccard_distance,
    masi_distance,
    interval_distance,
    custom_distance,
    presence,
    fractional_presence,
)
from coffeehouse_nlpfr.metrics.paice import Paice
from coffeehouse_nlpfr.metrics.segmentation import windowdiff, ghd, pk
from coffeehouse_nlpfr.metrics.agreement import AnnotationTask
from coffeehouse_nlpfr.metrics.association import (
    NgramAssocMeasures,
    BigramAssocMeasures,
    TrigramAssocMeasures,
    QuadgramAssocMeasures,
    ContingencyMeasures,
)
from coffeehouse_nlpfr.metrics.spearman import (
    spearman_correlation,
    ranks_from_sequence,
    ranks_from_scores,
)
from coffeehouse_nlpfr.metrics.aline import align

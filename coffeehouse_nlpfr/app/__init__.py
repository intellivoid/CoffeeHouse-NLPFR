# Natural Language Toolkit: Applications package
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Interactive NLTK Applications:

chartparser:  Chart Parser
chunkparser:  Regular-Expression Chunk Parser
collocations: Find collocations in text
concordance:  Part-of-speech concordancer
nemo:         Finding (and Replacing) Nemo regular expression tool
rdparser:     Recursive Descent Parser
srparser:     Shift-Reduce Parser
wordnet:      WordNet Browser
"""


# Import Tkinter-based modules if Tkinter is installed
try:
    from six.moves import tkinter
except ImportError:
    import warnings

    warnings.warn("coffeehouse_nlpfr.app package not loaded " "(please install Tkinter library).")
else:
    from coffeehouse_nlpfr.app.chartparser_app import app as chartparser
    from coffeehouse_nlpfr.app.chunkparser_app import app as chunkparser
    from coffeehouse_nlpfr.app.collocations_app import app as collocations
    from coffeehouse_nlpfr.app.concordance_app import app as concordance
    from coffeehouse_nlpfr.app.nemo_app import app as nemo
    from coffeehouse_nlpfr.app.rdparser_app import app as rdparser
    from coffeehouse_nlpfr.app.srparser_app import app as srparser
    from coffeehouse_nlpfr.app.wordnet_app import app as wordnet

    try:
        from matplotlib import pylab
    except ImportError:
        import warnings

        warnings.warn(
            "coffeehouse_nlpfr.app.wordfreq not loaded " "(requires the matplotlib library)."
        )
    else:
        from coffeehouse_nlpfr.app.wordfreq_app import app as wordfreq

# skip doctests from this package
def setup_module(module):
    from nose import SkipTest

    raise SkipTest("coffeehouse_nlpfr.app examples are not doctests")

# Natural Language Toolkit: graphical representations package
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Import Tkinter-based modules if Tkinter is installed
try:
    from six.moves import tkinter
except ImportError:
    import warnings

    warnings.warn("coffeehouse_nlpfr.draw package not loaded " "(please install Tkinter library).")
else:
    from coffeehouse_nlpfr.draw.cfg import ProductionList, CFGEditor, CFGDemo
    from coffeehouse_nlpfr.draw.tree import (
        TreeSegmentWidget,
        tree_to_treesegment,
        TreeWidget,
        TreeView,
        draw_trees,
    )
    from coffeehouse_nlpfr.draw.table import Table

from coffeehouse_nlpfr.draw.dispersion import dispersion_plot

# skip doctests from this package
def setup_module(module):
    from nose import SkipTest

    raise SkipTest("coffeehouse_nlpfr.draw examples are not doctests")

# -*- coding: utf-8 -*-
# Natural Language Toolkit: Twitter
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK Twitter Package

This package contains classes for retrieving Tweet documents using the
Twitter API.

"""
try:
    import twython
except ImportError:
    import warnings

    warnings.warn(
        "The twython library has not been installed. "
        "Some functionality from the twitter package will not be available."
    )
else:
    from coffeehouse_nlpfr.twitter.util import Authenticate, credsfromfile
    from coffeehouse_nlpfr.twitter.twitterclient import (
        Streamer,
        Query,
        Twitter,
        TweetViewer,
        TweetWriter,
    )


from coffeehouse_nlpfr.twitter.common import json2csv

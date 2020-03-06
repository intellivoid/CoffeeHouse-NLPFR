# Natural Language Toolkit: Corpus Readers
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus fileids in a variety of formats.  These
functions can be used to read both the corpus fileids that are
distributed in the NLTK corpus package, and corpus fileids that are part
of external corpora.

Corpus Reader Functions
=======================
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a fileid, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``nltk.corpus.brown.words()``:

    >>> from coffeehouse_nlpfr.corpus import brown
    >>> print(", ".join(brown.words()))
    The, Fulton, County, Grand, Jury, said, ...

"""

from coffeehouse_nlpfr.corpus.reader.plaintext import *
from coffeehouse_nlpfr.corpus.reader.util import *
from coffeehouse_nlpfr.corpus.reader.api import *
from coffeehouse_nlpfr.corpus.reader.tagged import *
from coffeehouse_nlpfr.corpus.reader.cmudict import *
from coffeehouse_nlpfr.corpus.reader.conll import *
from coffeehouse_nlpfr.corpus.reader.chunked import *
from coffeehouse_nlpfr.corpus.reader.wordlist import *
from coffeehouse_nlpfr.corpus.reader.xmldocs import *
from coffeehouse_nlpfr.corpus.reader.ppattach import *
from coffeehouse_nlpfr.corpus.reader.senseval import *
from coffeehouse_nlpfr.corpus.reader.ieer import *
from coffeehouse_nlpfr.corpus.reader.sinica_treebank import *
from coffeehouse_nlpfr.corpus.reader.bracket_parse import *
from coffeehouse_nlpfr.corpus.reader.indian import *
from coffeehouse_nlpfr.corpus.reader.toolbox import *
from coffeehouse_nlpfr.corpus.reader.timit import *
from coffeehouse_nlpfr.corpus.reader.ycoe import *
from coffeehouse_nlpfr.corpus.reader.rte import *
from coffeehouse_nlpfr.corpus.reader.string_category import *
from coffeehouse_nlpfr.corpus.reader.propbank import *
from coffeehouse_nlpfr.corpus.reader.verbnet import *
from coffeehouse_nlpfr.corpus.reader.bnc import *
from coffeehouse_nlpfr.corpus.reader.nps_chat import *
from coffeehouse_nlpfr.corpus.reader.wordnet import *
from coffeehouse_nlpfr.corpus.reader.switchboard import *
from coffeehouse_nlpfr.corpus.reader.dependency import *
from coffeehouse_nlpfr.corpus.reader.nombank import *
from coffeehouse_nlpfr.corpus.reader.ipipan import *
from coffeehouse_nlpfr.corpus.reader.pl196x import *
from coffeehouse_nlpfr.corpus.reader.knbc import *
from coffeehouse_nlpfr.corpus.reader.chasen import *
from coffeehouse_nlpfr.corpus.reader.childes import *
from coffeehouse_nlpfr.corpus.reader.aligned import *
from coffeehouse_nlpfr.corpus.reader.lin import *
from coffeehouse_nlpfr.corpus.reader.semcor import *
from coffeehouse_nlpfr.corpus.reader.framenet import *
from coffeehouse_nlpfr.corpus.reader.udhr import *
from coffeehouse_nlpfr.corpus.reader.bnc import *
from coffeehouse_nlpfr.corpus.reader.sentiwordnet import *
from coffeehouse_nlpfr.corpus.reader.twitter import *
from coffeehouse_nlpfr.corpus.reader.nkjp import *
from coffeehouse_nlpfr.corpus.reader.crubadan import *
from coffeehouse_nlpfr.corpus.reader.mte import *
from coffeehouse_nlpfr.corpus.reader.reviews import *
from coffeehouse_nlpfr.corpus.reader.opinion_lexicon import *
from coffeehouse_nlpfr.corpus.reader.pros_cons import *
from coffeehouse_nlpfr.corpus.reader.categorized_sents import *
from coffeehouse_nlpfr.corpus.reader.comparative_sents import *
from coffeehouse_nlpfr.corpus.reader.panlex_lite import *
from coffeehouse_nlpfr.corpus.reader.panlex_swadesh import *

# Make sure that coffeehouse_nlpfr.corpus.reader.bracket_parse gives the module, not
# the function bracket_parse() defined in coffeehouse_nlpfr.tree:
from coffeehouse_nlpfr.corpus.reader import bracket_parse

__all__ = [
    'CorpusReader',
    'CategorizedCorpusReader',
    'PlaintextCorpusReader',
    'find_corpus_fileids',
    'TaggedCorpusReader',
    'CMUDictCorpusReader',
    'ConllChunkCorpusReader',
    'WordListCorpusReader',
    'PPAttachmentCorpusReader',
    'SensevalCorpusReader',
    'IEERCorpusReader',
    'ChunkedCorpusReader',
    'SinicaTreebankCorpusReader',
    'BracketParseCorpusReader',
    'IndianCorpusReader',
    'ToolboxCorpusReader',
    'TimitCorpusReader',
    'YCOECorpusReader',
    'MacMorphoCorpusReader',
    'SyntaxCorpusReader',
    'AlpinoCorpusReader',
    'RTECorpusReader',
    'StringCategoryCorpusReader',
    'EuroparlCorpusReader',
    'CategorizedBracketParseCorpusReader',
    'CategorizedTaggedCorpusReader',
    'CategorizedPlaintextCorpusReader',
    'PortugueseCategorizedPlaintextCorpusReader',
    'tagged_treebank_para_block_reader',
    'PropbankCorpusReader',
    'VerbnetCorpusReader',
    'BNCCorpusReader',
    'ConllCorpusReader',
    'XMLCorpusReader',
    'NPSChatCorpusReader',
    'SwadeshCorpusReader',
    'WordNetCorpusReader',
    'WordNetICCorpusReader',
    'SwitchboardCorpusReader',
    'DependencyCorpusReader',
    'NombankCorpusReader',
    'IPIPANCorpusReader',
    'Pl196xCorpusReader',
    'TEICorpusView',
    'KNBCorpusReader',
    'ChasenCorpusReader',
    'CHILDESCorpusReader',
    'AlignedCorpusReader',
    'TimitTaggedCorpusReader',
    'LinThesaurusCorpusReader',
    'SemcorCorpusReader',
    'FramenetCorpusReader',
    'UdhrCorpusReader',
    'BNCCorpusReader',
    'SentiWordNetCorpusReader',
    'SentiSynset',
    'TwitterCorpusReader',
    'NKJPCorpusReader',
    'CrubadanCorpusReader',
    'MTECorpusReader',
    'ReviewsCorpusReader',
    'OpinionLexiconCorpusReader',
    'ProsConsCorpusReader',
    'CategorizedSentencesCorpusReader',
    'ComparativeSentencesCorpusReader',
    'PanLexLiteCorpusReader',
    'NonbreakingPrefixesCorpusReader',
    'UnicharsCorpusReader',
    'MWAPPDBCorpusReader',
    'PanlexSwadeshCorpusReader',
]

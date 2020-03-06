# Natural Language Toolkit: Chatbots
#
# Copyright (C) 2001-2019 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.

"""
A class for simple chatbots.  These perform simple pattern matching on sentences
typed by users, and respond with automatically generated sentences.

These chatbots may not work using the windows command line or the
windows IDLE GUI.
"""

from coffeehouse_nlpfr.chat.util import Chat
from coffeehouse_nlpfr.chat.eliza import eliza_chat
from coffeehouse_nlpfr.chat.iesha import iesha_chat
from coffeehouse_nlpfr.chat.rude import rude_chat
from coffeehouse_nlpfr.chat.suntsu import suntsu_chat
from coffeehouse_nlpfr.chat.zen import zen_chat

bots = [
    (eliza_chat, "Eliza (psycho-babble)"),
    (iesha_chat, "Iesha (teen anime junky)"),
    (rude_chat, "Rude (abusive bot)"),
    (suntsu_chat, "Suntsu (Chinese sayings)"),
    (zen_chat, "Zen (gems of wisdom)"),
]


def chatbots():
    import sys

    print("Which chatbot would you like to talk to?")
    botcount = len(bots)
    for i in range(botcount):
        print("  %d: %s" % (i + 1, bots[i][1]))
    while True:
        print("\nEnter a number in the range 1-%d: " % botcount, end=" ")
        choice = sys.stdin.readline().strip()
        if choice.isdigit() and (int(choice) - 1) in range(botcount):
            break
        else:
            print("   Error: bad chatbot number")

    chatbot = bots[int(choice) - 1][0]
    chatbot()

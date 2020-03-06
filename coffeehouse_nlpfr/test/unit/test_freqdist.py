import unittest
import coffeehouse_nlpfr


class TestFreqDist(unittest.TestCase):

    def test_iterating_returns_an_iterator_ordered_by_frequency(self):

        samples = ['one', 'two', 'two']

        distribution = coffeehouse_nlpfr.FreqDist(samples)

        most_frequent, less_frequent = [entry for entry in distribution]

        self.assertEqual(most_frequent, 'two')
        self.assertEqual(less_frequent, 'one')

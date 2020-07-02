import unittest
from crossword import *
from generate import *


class TestGenerate(unittest.TestCase):
    def test_enforce_node_consistency(self):
        # Parse command-line arguments
        structure = "data/structure1.txt"
        words = "data/words1.txt"

        # Generate crossword
        crossword = Crossword(structure, words)
        creator = CrosswordCreator(crossword)
        creator.enforce_node_consistency()


if __name__ == "__main__":
    unittest.main()

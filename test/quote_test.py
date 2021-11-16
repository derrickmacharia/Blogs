import unittest
from app.models import Quote


class TestQuote(unittest.TestCase):
    """
    Test class to test the behaviour of the  class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_quote = Quote(
            author='Jamie zawinski'
        )
import unittest

from ...utils.url import get_url_title


class TestUtils(unittest.TestCase):

    def test_google_title(self):
        title = get_url_title('https://wikipedia.com')
        self.assertIsNotNone(title)

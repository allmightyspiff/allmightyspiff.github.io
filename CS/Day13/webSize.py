import requests

class urlParser():

    def getSize(self, url):
        result = requests.get(url)
        return len(result.content)

class fakeRequest():
    def __init__(self):
        self.statusCode = 200
        self.content = "HELLO"

import unittest
from unittest import mock
class TestWebSize(unittest.TestCase):

    def setUp(self):
        self.url = "https://github.com"
        self.urlParser = urlParser()

    @mock.patch('requests.get')
    def test_first_thing(self, _fake_request):
        _fake_request.return_value = fakeRequest() 
        result = self.urlParser.getSize(self.url)
        self.assertEqual(result,5)
        self.assertEqual(1, _fake_request.call_count)
        _fake_request.assert_called_once_with(self.url)


if __name__ == '__main__':
    unittest.main()
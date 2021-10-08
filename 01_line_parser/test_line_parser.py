# Import Python built-in unittest library
import unittest
# We import the parse_line function from os_detection.py
from line_parser import parse_line


# To define tests, as per documentation we need to create a class
class TestLineParser(unittest.TestCase):
    # Each test case if defined in a function starting with "test_"
    def test_parse_simple_line(self):
        # To make tests, we use the provided functions starting with `self.assert`
        self.assertEqual(
            # This is the value we expect to be returned by our parser_line function
            dict(
                remote_ip='83.149.9.216',
                time='17/May/2015:10:05:03 +0000',
                request='GET /image.png HTTP/1.1',
                response=200,
                bytes=203023,
                referrer='http://referred-url.com',
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
            )
            ,
            parse_line(
                '83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /image.png HTTP/1.1" 200 203023 "http://referred-url.com" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'
            )
        )


# If the file is not imported but run directly: we run all tests
if __name__ == '__main__':
    unittest.main()

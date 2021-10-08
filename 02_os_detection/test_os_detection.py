# Import Python built-in unittest library
import unittest
# We import the parse_line function from os_detection.py
from os_detection import detect_os


# To define tests, as per documentation we need to create a class
class TestOsDetection(unittest.TestCase):
    # Each test case if defined in a function starting with "test_"
    def test_mac_os_x(self):
        # To make tests, we use the provided functions starting with `self.assert`
        self.assertEqual(
            # This is the value we expect to be returned by our detect_os function
            # We could decide to match only "Mac OS" or also match the version: "Mac OS X 10_9_1"
            'Mac OS X'
            ,
            detect_os(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'
            )
        )

    def test_linux(self):
        self.assertEqual(
            # This is the value we expect to be returned by our detect_os function
            'Linux'
            ,
            detect_os(
                'Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0'
            )
        )

    def test_windows(self):
        self.assertEqual(
            # This is the value we expect to be returned by our detect_os function
            'Windows NT 6.2'
            ,
            detect_os(
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'
            )
        )

    def test_bot(self):
        self.assertEqual(
            # This is the value we expect to be returned by our detect_os function
            'iOS 6_0'
            ,
            detect_os(
                'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
            )
        )

    def test_unknown(self):
        self.assertEqual(
            # This is the value we expect to be returned by our detect_os function
            None
            ,
            detect_os(
                'UniversalFeedParser/4.2-pre-314-svn +http://feedparser.org/'
            )
        )


# If the file is not imported but run directly: we run all tests
if __name__ == '__main__':
    unittest.main()

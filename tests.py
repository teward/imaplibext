import imaplibext
import unittest


class TestIMAPMethods(unittest.TestCase):

    def test_imap4_plain(self):
        # type: () -> None
        # noinspection PyUnusedLocal
        conn = None
        conn = imaplibext.IMAP4('mail.dark-net.io', 143)
        self.assertIsNotNone(conn, 'Expected an actual conn here.')
        self.assertEqual(conn.state, 'NONAUTH', "Expected non-authenticated connection state.")
        return None  # Python 2 Type Hinting Compliance

    def test_imap4_ssl(self):
        # type: () -> None
        # noinspection PyUnusedLocal
        conn = None
        conn = imaplibext.IMAP4_SSL('mail.dark-net.io', 993)
        self.assertIsNotNone(conn, 'Expected an actual conn here.')
        self.assertEqual(conn.state, 'NONAUTH', "Expected non-authenticated connection state.")
        return None  # Python 2 Type Hinting Compliance


if __name__ == '__main__':
    unittest.main()

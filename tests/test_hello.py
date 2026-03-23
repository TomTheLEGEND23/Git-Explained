import unittest

from hello import get_message, get_status_message


class TestHello(unittest.TestCase):
    def test_get_message_returns_expected_text(self) -> None:
        self.assertEqual(get_message(), "Hello from Git-Explained!")

    def test_get_status_message_mentions_tests(self) -> None:
        self.assertIn("tests", get_status_message().lower())


if __name__ == "__main__":
    unittest.main()

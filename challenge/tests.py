from main import longest_streak
import unittest

class LongestStreakTest(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(longest_streak('aaabababb'), 3)

    def test_case_02(self):
        self.assertEqual(longest_streak('ababababa'), 1)

    def test_case_03(self):
        self.assertEqual(longest_streak('aaabbddddabbd'), 4)

    def test_case_04(self):
        self.assertEqual(longest_streak('ababbbbbabbbbbb'), 6)

    def test_case_05(self):
        self.assertEqual(longest_streak('dlkfaadhouflkkndhodlngggggggfsadkjluijna'), 7)

unittest.main(verbosity=2)

import unittest
import divisors
import choosing_test_cases

class TestDivisors(unittest.TestCase):
    """
    Example unittest test methods for get_divisors.
    """

    def test_divisors_example_1(self):
        """
        Test get_divisors with 8 and [1, 2, 3].
        """
        actual = divisors.get_divisors(8, [1, 2, 3])
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_divisors_example_2(self):
        """
        Test get_divisors with 4 and [-2, 0, 2].
        """
        actual = divisors.get_divisors(4, [-2, 0, 2])
        expected = [-2, 2]
        self.assertEqual(expected, actual)


class TestCountLowercaseVowels(unittest.TestCase):
    """
    Example unittest methods for count_lowercase_vowels.
    """

    def test_is_empty(self):
        """
        Test for empty string.
        """
        actual = choosing_test_cases.count_lowercase_vowels('')
        expected = 0
        self.assertEqual(expected, actual)

    def test_is_vowel(self):
        """
        Test for single character, vowel.
        """
        actual = choosing_test_cases.count_lowercase_vowels('a')
        expected = 1
        self.assertEqual(expected, actual)

    def test_is_not_vowel(self):
        """
        Test for single character, not a vowel.
        """
        actual = choosing_test_cases.count_lowercase_vowels('b')
        expected = 0
        self.assertEqual(expected, actual)

    def test_multiple_characters_no_vowels(self):
        """
        Test for multiple-character string with no vowels.
        """
        actual = choosing_test_cases.count_lowercase_vowels('pfffft')
        expected = 0
        self.assertEqual(expected, actual)

    def test_multiple_characters_some_vowels(self):
        """
        Test for multiple-character string containing some vowels.
        """
        actual = choosing_test_cases.count_lowercase_vowels('bandit')
        expected = 2
        self.assertEqual(expected, actual)

    def test_multiple_characters_all_vowels(self):
        """
        Test for multiple-character string with all vowels.
        """
        actual = choosing_test_cases.count_lowercase_vowels('aeioua')
        expected = 6
        self.assertEqual(expected, actual)


class TestIsPalindrome(unittest.TestCase):
    """
    Example unittest methods for is_palindrome.
    """

    def test_empty_string(self):
        """
        Test for an empty string.
        """
        actual = choosing_test_cases.is_palindrome('')
        expected = True
        self.assertEqual(actual, expected)

    def test_single_character(self):
        """
        Test for a single character palindrome.
        """
        actual = choosing_test_cases.is_palindrome('a')
        expected = True
        self.assertEqual(actual, expected)

    def test_two_characters_palindrome(self):
        """
        Test for two characters, not a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('aa')
        expected = True
        self.assertEqual(actual, expected)

    def test_two_characters_not_palindrome(self):
        """
        Test for two characters, not a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('ab')
        expected = False
        self.assertEqual(actual, expected)

    def test_three_characters_palindrome(self):
        """
        Test for a three-character palindrome.
        """
        actual = choosing_test_cases.is_palindrome('aba')
        expected = True
        self.assertEqual(actual, expected)

    def test_three_characters_not_palindrome(self):
        """
        Test for three-character string that is not a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('abc')
        expected = False
        self.assertEqual(actual, expected)

    def test_even_numbered_string_palindrome(self):
        """
        Test for a longer string with an even number of characters that is a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('redder')
        expected = True
        self.assertEqual(actual, expected)

    def test_even_numbered_string_not_palindrome(self):
        """
        Test for a longer string with an even number of characters that is not a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('reader')
        expected = False
        self.assertEqual(actual, expected)

    def test_odd_numbered_string_palindrome(self):
        """
        Test for a longer string with an odd number of characters that is a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('racecar')
        expected = True
        self.assertEqual(actual, expected)

    def test_odd_numbered_string_not_palindrome(self):
        """
        Test for a longer string with an odd number of characters that is not a palindrome.
        """
        actual = choosing_test_cases.is_palindrome('bananas')
        expected = False
        self.assertEqual(actual, expected)


if __name__=='__main__':
# The (exit=False) parameter is used when calling unittest from within IDLE.
# https://stackoverflow.com/questions/2457068/using-idle-to-run-python-pyunit-unit-tests
    unittest.main(exit=False)

import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_odd_num_elements_k_equals_zero(self):
        """
        Test for a list with an odd number of elements with k equal to zero.
        """
        L = [1, 2, 3, 4, 5]
        L_expected = [1, 2, 3, 4, 5]
        a1.swap_k(L, 0)
        self.assertEqual(L, L_expected)

    def test_odd_num_elements_k_equals_one(self):
        """
        Test for a list with an odd number of elements with k equal to one.
        """
        L = [1, 2, 3, 4, 5]
        L_expected = [5, 2, 3, 4, 1]
        a1.swap_k(L, 1)
        self.assertEqual(L, L_expected)

    def test_odd_num_elements_k_is_odd(self):
        """
        Test for a list with an odd number of elements with k being an odd number.
        """
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [5, 6, 7, 4, 1, 2, 3]
        a1.swap_k(L, 3)
        self.assertEqual(L, L_expected)

    def test_odd_num_elements_k_is_even(self):
        """
        Test for a list with an odd number of elements with k being an even number.
        """
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [6, 7, 3, 4, 5, 1, 2]
        a1.swap_k(L, 2)
        self.assertEqual(L, L_expected)

    def test_even_num_elements_k_equals_one(self):
        """
        Test for a list with an even number of elements with k equal to 1.
        """
        L = [1, 2, 3, 4, 5, 6]
        L_expected = [6, 2, 3, 4, 5, 1]
        a1.swap_k(L, 1)
        self.assertEqual(L, L_expected)

    def test_even_num_elements_k_is_odd(self):
        """
        Test for a list with an even number of elements with k being an odd number.
        """
        L = [1, 2, 3, 4, 5, 6, 7, 8]
        L_expected = [6, 7, 8, 4, 5, 1, 2, 3]
        a1.swap_k(L, 3)
        self.assertEqual(L, L_expected)

    def test_even_num_elements_k_is_even(self):
        """
        Test for a list with an even number of elements with k being an even number.
        """
        L = [1, 2, 3, 4, 5, 6]
        L_expected = [5, 6, 3, 4, 1, 2]
        a1.swap_k(L, 2)
        self.assertEqual(L, L_expected)



if __name__ == '__main__':
    unittest.main(exit=False)

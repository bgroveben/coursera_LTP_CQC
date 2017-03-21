import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_empty_list(self):
        """
        Test for an empty list of price change inputs.
        """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_single_item_list_of_zero(self):
        """
        Test for a single item list containing zero.
        """
        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_single_item_list_of_one_gain(self):
        """
        Test for a single item list containing one positive item.
        """
        actual = a1.stock_price_summary([0.05])
        expected = (0.05, 0)
        self.assertEqual(actual, expected)

    def test_single_item_list_of_one_loss(self):
        """
        Test for a single item list containing one negative item.
        """
        actual = a1.stock_price_summary([-0.05])
        expected = (0, -0.05)
        self.assertEqual(actual, expected)

    def test_inputs_are_all_zeros(self):
        """
        Test for list of price change inputs that are all zero.
        """
        actual = a1.stock_price_summary([0, 0, 0, 0, 0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_inputs_are_all_gains(self):
        """
        Test for list of price change inputs that are all positive values.
        """
        actual = a1.stock_price_summary([0.01, 0.03, 0.02, 0.14, 0.10, 0.01])
        expected = (0.31, 0)
        self.assertEqual(actual, expected)

    def test_inputs_are_all_losses(self):
        """
        Test for list of price change inputs that are all negative values.
        """
        actual = a1.stock_price_summary([-0.01, -0.03, -0.02, -0.14, -0.10, -0.01])
        expected = (0, -0.31)
        self.assertEqual(actual, expected)

    def test_mixed_inputs(self):
        """
        Test for list of price change inputs that are a mix of zeros, gains and losses.
        """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main(exit=False)

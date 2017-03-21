import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_no_people(self):
        """
        Test for no people, so no buses are needed.
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_person(self):
        """
        Test for one person, the minimum number of people needed for one bus.
        """
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_maximum_for_one_bus(self):
        """
        Test for the maximum number of people allowed for one bus.
        """
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_between_one_and_two_buses(self):
        """
        Test for greater than 1 bus threshold, less than 2 bus threshold.
        """
        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_maximum_for_two_buses(self):
        """
        Test for the maximum number of people allowed for two buses.
        """
        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(actual, expected)

    def test_for_many_people(self):
        """
        Test for many people.
        """
        actual = a1.num_buses(235)
        expected = 5
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main(exit=False)

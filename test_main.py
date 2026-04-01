import unittest
from main import calculate_sum_and_average, get_numbers_from_user, find_max_number, calculate_factorial

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()

class TestNewFunctions(unittest.TestCase):

    def test_find_max_number(self):
        # Test này sẽ FAIL vì hàm có bug (trả về max + 1)
        self.assertEqual(find_max_number([1, 5, 3, 9, 2]), 9)
    
    def test_find_max_empty_list(self):
        with self.assertRaises(ValueError):
            find_max_number([])
    
    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

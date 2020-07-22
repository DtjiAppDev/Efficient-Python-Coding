import unittest


from efficient_python_coding import *


class MyTestCase(unittest.TestCase):
    def test_mpf_sum_of_list_1(self):
        self.assertEqual(mpf_sum_of_list(["5.34", "4.37", "3.32"]), mpf_sum_of_list(["5.34", "ssx", "4.37", "3.32"]))

    def test_mpf_sum_of_list_2(self):
        self.assertEqual(mpf_sum_of_list(["2.5", "2.5"]), mpf("5"))

    def test_mpf_sum_of_list_3(self):
        self.assertEqual(mpf_sum_of_list(["5.34", "ssx", "4.37", "3.32"]), mpf("13.03"))

    def test_mpf_sum_of_list_4(self):
        self.assertEqual(mpf_sum_of_list(["w", "k", 1, 2]), 3)

    def test_mpf_product_of_list_1(self):
        self.assertEqual(mpf_product_of_list(["5.34", "4.37", "3.32"]),
                         mpf_product_of_list(["5.34", "ssx", "4.37", "3.32"]))

    def test_mpf_product_of_list_2(self):
        self.assertEqual(mpf_product_of_list(["2.5", "2.5"]), mpf("6.25"))

    def test_mpf_product_of_list_3(self):
        self.assertEqual(mpf_product_of_list(["5.34", "ssx", "4.37", "3.32"]), mpf("77.474856"))

    def test_mpf_product_of_list_4(self):
        self.assertEqual(mpf_product_of_list(["w", "k", 5, 8]), 40)

    def test_factorial_1(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_2(self):
        self.assertEqual(factorial(6), 720)

    def test_factorial_3(self):
        self.assertEqual(factorial(-2), 0)

    def test_factorial_4(self):
        self.assertEqual(factorial(0), 1)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(-2), 0)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci(2), 1)

    def test_count_occurrences_1(self):
        self.assertEqual(count_occurrences("badiahsdbeieifbadiahseaefdsf", "badiah"), 2)

    def test_count_occurrences_2(self):
        self.assertEqual(count_occurrences("dafaokpfrekpogrjrgjagg", "frek"), 1)

    def test_count_occurrences_3(self):
        self.assertEqual(count_occurrences("tagtagcatcatg", "a"), 4)


if __name__ == '__main__':
    unittest.main()

import unittest
from MySimpleLRUCache_KaranMaheshwari.helper import is_signed_32_bit_integer_format


class TestHelperClass(unittest.TestCase):

	def test_signed_positive_32_bit_integer(self):
		self.assertTrue(is_signed_32_bit_integer_format(10))

	def test_signed_negative_32_bit_integer(self):
		self.assertTrue(is_signed_32_bit_integer_format(-10))

	def test_max_signed_positive_32_bit_integer(self):
		self.assertTrue(is_signed_32_bit_integer_format(2147483647))

	def test_max_signed_negative_32_bit_integer(self):
		self.assertTrue(is_signed_32_bit_integer_format(-2147483648))

	def test_signed_positive_greater_than_32_bit_integer(self):
		self.assertFalse(is_signed_32_bit_integer_format(2147483648))

	def test_signed_negative_greater_than_32_bit_integer(self):
		self.assertFalse(is_signed_32_bit_integer_format(-2147483649))

	def test_float(self):
		self.assertFalse(is_signed_32_bit_integer_format(1.0))

	def test_string(self):
		self.assertFalse(is_signed_32_bit_integer_format("string"))


if __name__ == '__main__':
	unittest.main()

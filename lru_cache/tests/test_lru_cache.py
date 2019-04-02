import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

	def setUp(self):
		self.cache = LRUCache(3)

	def test_0_as_max_capacity_of_cache(self):
		self.assertEqual(LRUCache(0).get_max_capacity(), 5, "Should be 5.")

	def test_string_as_max_capacity_of_cache(self):
		self.assertEqual(LRUCache("abc").get_max_capacity(), 5, "Should be 5.")

	def test_float_as_max_capacity_of_cache(self):
		self.assertEqual(LRUCache(2.0).get_max_capacity(), 5, "Should be 5.")

	def test_None_as_max_capacity_of_cache(self):
		self.assertEqual(LRUCache(None).get_max_capacity(), 5, "Should be 5.")

	def test_negative_value_as_max_capacity_of_cache(self):
		self.assertEqual(LRUCache(-5).get_max_capacity(), 5, "Should be 5.")

	def test_put_1_element(self):
		self.cache.put(1)
		self.assertIn(1, self.cache.get_elements(), "Should exist.")

	def test_put_1_element_check_capacity(self):
		self.cache.put(1)
		self.assertEqual(self.cache.get_current_capacity(), 1, "Should be equal.")

	def test_get_elements(self):
		self.cache.put(1)
		self.cache.put(2)
		self.assertEqual([1, 2], self.cache.get_elements(), "Should be [1, 2].")

	def test_put_2_elements_check_capacity(self):
		self.cache.put(1)
		self.cache.put(2)
		self.assertEqual(self.cache.get_current_capacity(), 2, "Should be equal.")

	def test_put_max_capacity(self):
		self.cache.put(1)
		self.cache.put(2)
		self.cache.put(3)
		self.assertIn(3, self.cache.get_elements(), "Should exist.")

	def test_put_more_than_max_capacity(self):
		self.cache.put(1)
		self.cache.put(2)
		self.cache.put(3)
		self.cache.put(4)
		self.assertNotIn(1, self.cache.get_elements(), "Should not exist.")
		self.assertIn(4, self.cache.get_elements(), "Should exist.")

	def test_put_more_than_max_capacity_check_capacity(self):
		self.cache.put(1)
		self.cache.put(2)
		self.cache.put(3)
		self.cache.put(4)
		self.assertEqual(self.cache.get_current_capacity(), 3, "Should be equal.")

	def test_clear_cache(self):
		self.cache.put(1)
		self.cache.put(2)
		self.cache.put(3)
		self.cache.clear_cache()
		self.assertEqual(len(self.cache.get_elements()), 0, "Should be 0.")

	def test_get(self):
		self.cache.put(1)
		self.assertTrue(self.cache.get(1), "Should be True.")

	def test_get_element_does_not_exist(self):
		self.assertFalse(self.cache.get(1), "Should be False.")


if __name__ == '__main__':
	unittest.main()

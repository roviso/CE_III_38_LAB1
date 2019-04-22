import unittest
from searchAlgo import LinearSearch
from searchAlgo import BinarySearch

class SearchTestCase(unittest.TestCase):
# Linear Search Test
	def test_linear_search(self):
		arr=[5,3,7,2,1,0,9,8,4]
		self.assertEqual(LinearSearch(arr,5),0)	#5 lies in the 0th index so no error
		self.assertEqual(LinearSearch(arr,1),4)
		self.assertEqual(LinearSearch(arr,10),-1)

# Binary Search Test
	def test_binary_search(self):
		#sorted array for binary search
		arr=[0,1,2,3,4,5,6,7,9]
		self.assertEqual(BinarySearch(arr,5),5)
		self.assertEqual(BinarySearch(arr,1),1)
		self.assertEqual(BinarySearch(arr,10),-1)

if __name__ == '__main__':
	unittest.main()
	# All the tests will run with no errors as the index at which the values are searched are correct
	#If self.assertEqual(BinarySearch(arr,10),2) is done in test_binary_search(self) then test case will fail

import unittest


class heapSort():

    def heapify(self, array, heap_size, top_index):
        largest = top_index
        left = (2 * top_index) + 1
        right = (2 * top_index) + 2

        # Check if left exists, and if LARGEST < left
        if left < heap_size and array[largest] < array[left]:
            largest = left

        # Checks if right exist, and if LARGEST < right
        if right < heap_size and array[largest] < array[right]:
            largest = right

        if largest != top_index:
            # Swap top index and largest
            array[top_index], array[largest] = array[largest], array[top_index]
            # Recuse until no more swaps
            self.heapify(array, heap_size, largest)

    def sort(self, array):
        size = len(array)
        # Build the max heap
        for i in range(size, -1, -1):
            self.heapify(array, size, i)

        for i in range(size - 1, 0, -1):
            # Swap top and last elements
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array



class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.toSort = [4, 10, 3, 5, 1]
        self.sorted = [1, 3, 4, 5, 10]
        self.heapSort = heapSort()

    def test_sorting(self):
        sorted_array = self.heapSort.sort(self.toSort)
        self.assertEqual(self.toSort, self.sorted)

    def test_not_array(self):
        with self.assertRaises(TypeError):
            sorted_array = self.heapSort.sort('asdfg')

    def test_empty_array(self):
        sorted_array = self.heapSort.sort([])
        self.assertEqual(sorted_array, [])

if __name__ == '__main__':
    unittest.main()


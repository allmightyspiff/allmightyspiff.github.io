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


class quickSort():


    """
    partitions array so that value in high is moved to a position where
    all elements to the left are lower, and elements to the right are higher in value
    """ 
    def partition(self, array, low, high):
        i = ( low - 1 )    # smallest element value
        pivot = array[high]  # pivot value
     
        for x in range(low , high):
            if array[x] <= pivot:
                i = i + 1
                array[i], array[x] = array[x], array[i] # swap lowest and x
     
        i = i + 1
        array[i],array[high] = array[high],array[i] # Swap i and high
        return ( i ) # return new pivot point

    def sort(self, array, low = 0, high = None):
        if high is None: # default partition is last element
            high = len(array) - 1
        if low < high: # Recurse until each partition meets in the middle
            pi = self.partition(array,low,high) # partition elements, returns new index of partitioned value

            self.sort(array, low, pi-1) # sort left side of partition
            self.sort(array, pi+1, high)  # sort right side of partition


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.toSort = [4, 10, 3, 5, 1]
        self.sorted = [1, 3, 4, 5, 10]
        self.heapSort = heapSort()
        self.quickSort = quickSort()

    def test_sorting(self):
        self.heapSort.sort(self.toSort)
        self.assertEqual(self.toSort, self.sorted)

    def test_not_array(self):
        with self.assertRaises(TypeError):
            self.heapSort.sort('asdfg')

    def test_empty_array(self):
        sorted_array = []
        self.heapSort.sort(sorted_array)
        self.assertEqual(sorted_array, [])

    def test_quick_sort(self):
        self.quickSort.sort(self.toSort)
        self.assertEqual(self.toSort, self.sorted)

if __name__ == '__main__':
    unittest.main()


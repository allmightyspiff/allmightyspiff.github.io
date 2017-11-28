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

class quickSort():

    def partition(self, arr, low, high):
        i = ( low - 1 )    # index of smaller element
        pivot = arr[high]  # pivot
     
        for j in range(low , high):
     
            # If current element is smaller than or
            # equal to pivot
            if   arr[j] <= pivot:
             
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
     
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return ( i+1 )
 
    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index
     
    # Function to do Quick sort
    def sort(self, arr, low = 0, high = None):
        # Default partition is by highest element
        if high is None:
            high = len(arr) - 1

        if low < high:
     
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr,low,high)
     
            # Separately sort elements before
            # partition and after partition
            self.sort(arr, low, pi-1)
            self.sort(arr, pi+1, high)


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.toSort = [4, 10, 3, 5, 1]
        self.sorted = [1, 3, 4, 5, 10]
        self.heapSort = heapSort()
        self.quickSort = quickSort()

    def test_sorting(self):
        sorted_array = self.heapSort.sort(self.toSort)
        self.assertEqual(self.toSort, self.sorted)

    def test_not_array(self):
        with self.assertRaises(TypeError):
            sorted_array = self.heapSort.sort('asdfg')

    def test_empty_array(self):
        sorted_array = self.heapSort.sort([])
        self.assertEqual(sorted_array, [])

    def test_quick_sort(self):
        sorted_array = self.quickSort.sort(self.toSort)
        self.assertEqual(self.toSort, self.sorted)

if __name__ == '__main__':
    unittest.main()


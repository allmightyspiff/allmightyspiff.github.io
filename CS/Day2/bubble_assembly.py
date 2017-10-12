"""
@package examples 
@author Christopher Gallo
Bubble Sorting
"""
from pprint import pprint as pp
import dis
class bubbleSort():

    def sort(self, to_sort):
        """Bubble sorts to_sort
        """
        is_sorted = False
        while not is_sorted:
            array_len = len(to_sort)
            jobs_done = True
            # pp(to_sort)
            for i in range(0,array_len):
                # Makes sure we dont go out of bounds
                if i + 1 == array_len:
                    continue
                # At least one element was unsorted
                if to_sort[i] > to_sort[i + 1]:
                    jobs_done = False
                    temp = to_sort[i]
                    to_sort[i] = to_sort[i + 1]
                    to_sort[i + 1] = temp
                i = i + 1
            # If we went over the array without changes, we are done
            if jobs_done:
                is_sorted = True
        return to_sort

if __name__ == "__main__":
    test_array = [5, 9, 4, 1, 2, 3, 8]
    main = bubbleSort()
    sorted_array = main.sort(test_array)
    print("Jobs Done")
    pp(sorted_array)
    dis.dis(bubbleSort)

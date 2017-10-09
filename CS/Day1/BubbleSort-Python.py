"""
@package examples 
@author Christopher Gallo
Bubble Sorting
"""
from pprint import pprint as pp
import random
import time
import copy

class bubbleSort():

    def bubble_sort(self,my_array):
        array_length = len(my_array)
        total_number_of_passes = array_length
        for i in range(0, total_number_of_passes):
            for j in range(0, array_length):
                if j == array_length - 1:
                    continue
                if my_array[j] > my_array[j + 1]:

                    temp = my_array[j]
                    my_array[j] = my_array[j + 1]
                    my_array[j + 1] = temp
            array_length = array_length - 1
        return my_array


    def simple_sort(self, to_sort):
        to_sort.sort()
        return to_sort

    def random_array(self, length):
        the_array = []
        for i in range(0, length):
            the_array.append(random.randint(0,100000))
        return the_array

if __name__ == "__main__":
    main = bubbleSort()
    test_array1 = main.random_array(5000)
    test_array2 = copy.deepcopy(test_array1)

    print("Sorting #1")
    now = time.time()
    main.bubble_sort(test_array1)
    then = time.time()
    time1 = then - now
    print("Sorting #2")
    now = time.time()
    main.simple_sort(test_array2)
    then = time.time()
    time2 = then - now

    print("#1 = %s\n#2 = %s" % (time1, time2))
    print("Jobs Done")
    # pp(sorted_array)

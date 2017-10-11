"""
@package array_reverse
@author Christopher Gallo
Reverse Array
"""
from pprint import pprint as pp
import random
import time

class array_reverse():

    def reverse(self, my_array):

        for i in range(0,len(my_array) / 2):
            temp = my_array[i]
            # (len(my_array) - 1 ) - i would also work
            reverse_i = -( i + 1)
            my_array[i] = my_array[reverse_i]
            my_array[reverse_i] = temp

    def reverse_python(self, my_array):
        my_array.reverse()

    def random_array(self, length):
        the_array = []
        for i in range(0, length):
            the_array.append(random.randint(0,100000))
        return the_array
if __name__ == "__main__":

    main = array_reverse()
    my_array = main.random_array(500000)
    now = time.time()
    main.reverse(my_array)
    then = time.time()
    print("My sort took %s" % (then - now))

    my_array = main.random_array(500000)
    now = time.time()
    main.reverse_python(my_array)
    then = time.time()
    print("Python sort took %s" % (then - now))
    # print(my_array)
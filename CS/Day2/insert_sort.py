"""
@package insert_sort 
@author Christopher Gallo
Insert Sorting
"""
from pprint import pprint as pp

class insert_sort():

    def sort(self, my_array):
        length = len(my_array)
        for i in range(length):
            temp = my_array[i]
            x = i - 1 
            while x >= 0 and my_array[x] > temp:
                my_array[x + 1] = my_array[x]
                x = x - 1
            my_array[x + 1 ] = temp
        return my_array


if __name__ == "__main__":
    my_array = [9, 4, 2, 6, 1, 0, 3, 5]
    main = insert_sort()
    main.sort(my_array)
    print(my_array)
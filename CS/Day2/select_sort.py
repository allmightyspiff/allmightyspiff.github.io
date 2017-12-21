"""
@package selection_sort 
@author Christopher Gallo
Select Sorting
"""
from pprint import pprint as pp

class selection_sort():

    def sort(self, my_array):
        length = len(my_array)
        for i in range(length):
            min_index = i
            print(my_array)
            for x in range(i + 1, length):
                if my_array[min_index] > my_array[x]:
                    min_index = x

            if i != min_index:
                temp = my_array[i]
                my_array[i] = my_array[min_index]
                my_array[min_index] = temp

        return my_array

if __name__ == "__main__":
    my_array = [9, 4, 2,11, 1, 0, 3, 5]
    main = selection_sort()
    result = main.sort(my_array)
    print(result)
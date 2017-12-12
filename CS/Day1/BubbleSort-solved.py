class bubbleSort():

    def sort(self,my_array):
        array_length = len(my_array)
        total_number_of_passes = array_length
        for i in range(0, total_number_of_passes):
            for j in range(0, array_length):
                # Avoid going out of array bounds
                if j == array_length - 1:
                    continue
                if my_array[j] > my_array[j + 1]:
                    temp = my_array[j]
                    my_array[j] = my_array[j + 1]
                    my_array[j + 1] = temp
            # Last element of every pass will be the highest number
            array_length = array_length - 1
        return my_array

if __name__ == "__main__":
    test_array = [5, 9, 4, 1, 2, 99, 3, 8]
    main = bubbleSort()
    sorted_array = main.sort(test_array)
    print("Jobs Done")
    print(sorted_array)

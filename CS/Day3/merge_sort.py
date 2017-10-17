from pprint import pprint as pp

class mergeSort():

    def merge(self,left, right):
        # If one of the arrays is empty, return the other
        if not len(left) or not len(right):
            return left or right

        result = []
        # 
        R, L = 0, 0
        # Loop until result has as many elements as left + right
        while (len(result) < len(left) + len(right)):
            if left[L] < right[R]:
                result.append(left[L])
                L+= 1
            else:
                result.append(right[R])
                R+= 1
            if L == len(left) or R == len(right):
                result.extend(left[L:] or right[R:])
                break 

        return result

    # Code for merge sort

    def sort(self, x):
        """ Function to sort an array using merge sort algorithm """
        print(x)
        if len(x) <= 1:
            return x
        else:
            middle = len(x)//2
            #Start to Middle
            a = self.sort(x[:middle])
            # Middle to end
            b = self.sort(x[middle:])
            return self.merge(a,b)
if __name__ == "__main__":
    my_array = [9, 4, 2, 6, 1, 0, 3, 5]
    main = mergeSort()
    result = main.sort(my_array)
    print(result)

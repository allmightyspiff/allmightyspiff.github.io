from pprint import pprint as pp
import time
import bisect

class binary_search():
    def search_r(self, array, item):
        if len(array) == 0:
            return False
        else:
            midpoint = len(array)//2
            # print("1midpoint is array[%s] = %s" % (midpoint,array[midpoint]))
            if array[midpoint]==item:
                # print("FOUND")
                return midpoint
            else:
                if item<array[midpoint]:
                    return self.search_r(array[:midpoint],item)
                else:
                    return self.search_r(array[midpoint:],item)

    def binarySearch(self,array, item):
        first = 0
        last = len(array)


        while first < last:
            midpoint = (first + last)//2
            # print("2midpoint is array[%s] = %s" % (midpoint,array[midpoint]))
            if array[midpoint] == item:
                return midpoint
            else:
                if item < array[midpoint]:
                    last = midpoint
                else:
                    first = midpoint+1

        return False

    def bisect_search(self, array, item):
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(array, item)
        if i != len(array) and array[i] == item:
            return i
        raise ValueError

if __name__ == "__main__":
    my_array = range(0, 100000)
    main = binary_search()

    now = time.time()
    for i in range(0,100000):
        location = main.binarySearch(my_array, i)
        if location is False:
            print("NOT FOUND %s" % i)
    then = time.time()
    print("binarySearch took %ss" % (then - now ))

    now = time.time()
    for i in range(0,100000):
        location = main.search_r(my_array, i)
        if location is False:
            print("NOT FOUN %s" % i)
    then = time.time()
    print("search_r took %ss" % (then - now) )

    now = time.time()
    for i in range(0,100000):
        location = main.bisect_search(my_array, i)
        if location is False:
            print("NOT FOUN %s" % i)
    then = time.time()
    print("bisect_search took %ss" % (then - now) )

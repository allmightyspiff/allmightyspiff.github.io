"""
@package examples 
@author Christopher Gallo
Bubble Sorting
"""
from pprint import pprint as pp

class sigma_finder():

    def main(self, limit):
        result = 0

        for i in range(1, limit):
            if i % 3 == 0 or i % 5 == 0:
                result = result + i
        return result

if __name__ == "__main__":
    limit = 50000000
    main = sigma_finder()
    result = main.main(limit)
    print("The sum of all the multiples of 3 or 5 below %s is %s" % (limit,result))
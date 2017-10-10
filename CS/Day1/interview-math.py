"""
@package examples 
@author Christopher Gallo
Bubble Sorting
"""

class sigma_finder():
    def sum_divisible_by(self, number, max):
        p = int(max / number)
        sum = number * (p * (p + 1)) / 2
        print("%s * ( %s * (%s)) / 2 = %s " % (number, p, p + 1, sum))
        return int(sum)

    def main(self, limit):
        # limit = limit - 1 
        result = self.sum_divisible_by(3, limit) + self.sum_divisible_by(5, limit) - self.sum_divisible_by(15, limit)
        return result

if __name__ == "__main__":
    limit = 1000
    main = sigma_finder()
    result = main.main(limit)
    print("The sum of all the multiples of 3 or 5 below %s is %s" % (limit,result))
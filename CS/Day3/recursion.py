from pprint import pprint as pp
import time

class factorial():

    def factorial_recursive(self, number):
        if number <= 1:
            return number
        else:
            return  number * self.factorial_recursive(number - 1) 

    def factorial_while(self, number):
        result = 1
        while(number > 0):
            result = result * number
            number = number - 1 
        return result



if __name__ == "__main__":
    main = factorial()
    now = time.time()
    result1 = main.factorial_recursive(1000)
    res1 = time.time()
    print("factorial took %s, result %s " % (res1 - now, result1))
    result2 = main.factorial_while(1000)
    res2 = time.time()
    print("normal took %s, result %s " % (res2 - res1, result2))

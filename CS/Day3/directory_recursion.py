from pprint import pprint as pp
import os

class print_dir():
    def print_dir(self,sPath):
        for sChild in os.listdir(sPath):                
            sChildPath = os.path.join(sPath,sChild)
            if os.path.isdir(sChildPath):
                print(sChildPath)
                self.print_dir(sChildPath)
                

    # https://github.com/python/cpython/blob/3.6/Lib/os.py

if __name__ == "__main__":
    my_array = '/Users/christopher/Code/allmightyspiff.github.io/'
    main = print_dir()
    main.print_dir(my_array)
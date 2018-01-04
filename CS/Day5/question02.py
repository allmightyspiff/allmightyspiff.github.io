from __future__ import print_function

def equal(a,b):
    print("%s is %s? " % (a, b), end='')
    if a is b:
        print("TRUE")
    else:
        print("FALSE")

a = 11111
b = 11111

equal(a,b)
b = b - 1
equal(a,b)
b = b + 1 
equal(a,b)

a = 2
b = 2
equal(a,b)
b = b - 1
equal(a,b)
b = b + 1 
equal(a,b)
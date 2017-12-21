import dis
def hello():
    test  = 0 
    if test  == 1:
        print("Hello World")
    else:
        print("TEST")

if __name__ == "__main__":

    dis.dis(hello)

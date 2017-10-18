def factorial(n):
    if n <= 1:
        return n
    else:
        return  n * factorial(n - 1)


result = factorial(5000)
print(result)
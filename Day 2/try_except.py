# try except program in python
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except TypeError as te:
    print("Enter only digits")
except ZeroDivisionError:
    print("Denomonator should not be zero")
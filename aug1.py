# multiple arg
import math

def sub(*args):
    sub = 0
    for arg in args:
        sub = sub - arg
    return sub

print(sub(2,4,5,6,7,3,2,5,))

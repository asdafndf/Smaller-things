# In theory this code determines whether n is prime or not, however it has to be checked
from math import *
def is_prime(n):
    for x in range(2,ceil(sqrt(n))):
        if n % x == 0:
            return "%s is not a prime" % (n)
        else:
            return "%s is a prime" % (n)
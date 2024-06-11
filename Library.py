import math
import random

# Checks whether the input is a prime number, returns True if it is a prime number and False otherwise
def isPrime(number):
    # onyl works for integers > 1
    searchspace = math.trunc(math.sqrt(number))
    
    for divisor in range(2, searchspace + 1):
        if number % divisor == 0:
            return False
        
    return True

# Genrates a random prime number bounded by the argument
def randomPrime(upperbound):
    
    randomInt = random.randint(2, upperbound)
    
    while not isPrime(randomInt):
        randomInt = random.randint(2, upperbound) # picks a random number between 2 and upperbound (both included)

    return randomInt

# Checks whether number is a primitive k-th root modulo n
def isPrimitiveRootModulo(number, k, n):
    if exponentiationBySquaring(number, k, n) != 1:
        return False
    else:
        for i in range(2, k // 2 + 1): # try all prime divisors of k
            if k % i == 0:
                if isPrime(i):
                    exponent = exponentiationBySquaring(number, k // i, n)
                    if exponent == 1:
                        return False
    
    return True

# Genrates a random primitive root modulo the argument
def randomPrimitiveRootModulo(modulus):

    randomInt = random.randint(1, modulus - 1)

    while not isPrimitiveRootModulo(randomInt, modulus - 1, modulus):
        randomInt = random.randint(1, modulus - 1)
    
    return randomInt

# Returns the lowest primitive root modulo the argument
def lowestPrimitiveRootModulo(modulus):
    for i in range(1, modulus - 1):
        if isPrimitiveRootModulo(i, modulus - 1, modulus):
            return i
        
# Calculates the power a^b mod modulus in an effective way
def exponentiationBySquaring(a, b, modulus):
    # b must be a non-negative integer
    decomposition = list()
    exponent = b
    
    while exponent > 0:
        if exponent % 2 == 0:
            decomposition.insert(0, True)
            exponent = exponent // 2
        elif exponent % 2 == 1:
            decomposition.insert(0, False)
            exponent = exponent - 1

    result = 1 % modulus

    for i in decomposition:
        if i:
            result = (result ** 2) % modulus
        else:
            result = (result * a) % modulus

    return result
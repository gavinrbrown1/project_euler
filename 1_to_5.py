##############################################################################
# 1 - Multiples of 3 & 5
##############################################################################
# Sum of all multiples of 3 and 5 less than 1000

total = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i
print("Problem 1:", total)

##############################################################################
# 2 - Even Fibonacci Numbers
##############################################################################
# sum of even Fibonacci numbers less than 4 million

f0 = 1
f1 = 2
total = 0
while f1 <= 4E6:
    if f1 % 2 == 0:
        total += f1
    f0, f1 = f1, f0 + f1
print("Problem 2:", total)

##############################################################################
# 3 - Largest Prime Factor
##############################################################################
# ... of 600851475143?

def smallest_nonunit_factor(n):
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return(i)
    return(n) # because n is prime

def make_two_factors(n):
    factor = smallest_nonunit_factor(n)
    return([n / factor, factor])

factors = [600851475143]
i = 0
while True:
    if smallest_nonunit_factor(factors[i]) == factors[i]:
        i += 1
    else:
        factors += make_two_factors(factors[i])
        del factors[i]
    if i > (len(factors) - 1):
        break
print("Problem 3:", int(max(factors)))

##############################################################################
# 4 - Largest Palindrome Product
##############################################################################
# of two three-digit numbers

def is_palindrome(n):
    n = str(n)
    for i in range(int(len(n) / 2)):
        if n[i] != n[-i-1]:
            return(False)
    return(True)

top = 0
for i in range(1000):
    for j in range(1000):
        if is_palindrome(i * j) and i * j > top:
            top = i * j

print("Problem 4:", top)

##############################################################################
# 5 - Smallest Multiple
##############################################################################
# ... evenly divisible by all numbers 1 through 20

factors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11] # only need these

def works(n):
    for factor in factors:
        if n % factor != 0:
            return(False)
    return(True)

n = 1
while True:
    if works(n):
        break
    n += 1

print("Problem 5:", n)







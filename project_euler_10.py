import math
from functools import reduce
from operator import mul
from steves_utilities.profiler import profile

@profile
def project_euler_problem_1(x, y):
    #find the sun of all multiples of 3 and 5 bellow 1000
    return sum(set(range(x, 1000, x)).union(set(range(y, 1000, y))))
print('answer for problem 1: %d' % project_euler_problem_1(3, 5))


@profile
def project_euler_problem_2(n):
    # get the sum of the even values in the fibonacci sequence
    x, y, s = 1, 2, 0
    while y <= n:
        x, y = y, x + y
        if not y % 2 and y <= n:
            s += y
    return s + 2
print('answer for problem 2: %d' % project_euler_problem_2(4000000))


def is_prime(x):

    # is the number a prime number
    if x in (2, 3):
        return True
    if not x % 2 or not x %3:
        return False

    i, w = 5, 2
    while i * i <= x:
        if x % i == 0:
            return False

        i, w = i + w, 6 - w
    return True


@profile
def project_euler_problem_3(x):

    # What is the largest prime factor of 600851475243
    y = 2
    while y < math.ceil(x/2):
        if not x % y:
            a = x // y
            if is_prime(a):
                return a
        y += 1
    return None
print('answer for problem 3: %d' % project_euler_problem_3(600851475143))

@profile
def project_euler_problem_4(low, high, palindrome=0):
    # Find the largest palindromic number made of the product of 2 3-digit numbers
    if high - low:
        for x in range(high, low - 1, -1):
            for y in range(high, low - 1, -1):
                z = str(y * x)
                if z == z[::-1]:
                    palindrome = int(z) if int(z) > palindrome else palindrome
                    return project_euler_problem_4(y + 1, x, palindrome)
    return palindrome
print('answer for problem 4: %d' % project_euler_problem_4(100, 999))


def divides(x, y):

    # Check if one number divides evenly into a group of numbers
    for z in y:
        if x % z:
            return False
    return True

@profile
def project_euler_problem_5(x, y):
    # What is the smallest positive number that divides evenly into all the numbers from 1 to 20
    d = list(z for z in range(x, y) if y % z and z != 1)
    d.reverse()
    z = y
    m = 1
    while True:
        z = y * m
        if divides(z, d):
            return z
        m += 1
print('answer for problem 5: %d' % project_euler_problem_5(1, 20))


@profile
def project_euler_problem_6(x, y):
    # Find the difference of the sum of squares of the first one hundred natural numbers
    # and the square of the sum.
    sumofthesquares, squareofthesum = 0, 0
    for a in range(x, y + 1):
        sumofthesquares += a ** 2
        squareofthesum += a
    squareofthesum **= 2
    return squareofthesum - sumofthesquares
print('answer for problem 6: %d' % project_euler_problem_6(1, 100))


def get_primes_in_range(x, y):
    # Get all primes within a range.
    primes = set()
    for num in range(x, y + 1):
        if all(num % i for i in range(2, int(math.sqrt(num)) + 1)):
            primes.add(num)
    return primes


@profile
def project_euler_problem_7(x, y, primes=set()):
    # What is the 10001st prime number
    step = math.ceil(y / 10)
    these_primes = set(get_primes_in_range(x, x + step))
    primes.update(these_primes)
    if len(primes) >= y:
        return sorted(primes)[y]
    return project_euler_problem_7(x + step, y, primes=primes)
print('answer for problem 7: %d' % project_euler_problem_7(1, 10001))


@profile
def project_euler_problem_8(n, x):
    # Find the product of the 13 adjacent numbers with the highest product
    s, high = str(n), 0
    for i in range(len(s[:-x+1])):
        product = reduce(mul, (int(z) for z in s[i:i + x]), 1)
        high = product if product > high else high
    return high
print('project euler problem 8: %s' % project_euler_problem_8(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
, 13))

@profile
def project_euler_problem_9(n):
    #find product of pythagorean triplet whose sum is 1000
    top = list(range(2, math.ceil(n/2)))
    bottom = list(range(1, math.ceil(n/4)))
    for a in bottom:
        for b in top:
            c = math.sqrt((a ** 2) + (b ** 2))
            if not c.is_integer():
                continue
            s = a + b + c
            if s > 1000:
                break
            elif a + b + c == 1000:
                return a * b * c
        a += 1
        top = range(a + 1, math.ceil(n/2))
print('answer for problem 9: %d' % project_euler_problem_9(1000))

@profile
def eratosthenes_sieve(limit):
    # Return all prime numbers at or bellow limit
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = False

@profile
def project_euler_problem_10(x):
    # return the sum of all prime numbers bellow x
    return sum(eratosthenes_sieve(x))
print('answer for problem 10: %d' % project_euler_problem_10(2000000))

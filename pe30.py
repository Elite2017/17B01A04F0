def armstrong(num,p):
    temp = num
    sum = 0
    while num != 0:
        sum = sum + pow(num % 10, p)
        num = num // 10
    if sum == temp :
        return True
    else :
        return False

def digit_powers(p):
    s = 0
    for j in  range(10, 1000000):
        if armstrong(j,p) :
            s = s + j
    return s

p = 5
print(digit_powers(p))



'''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

def curious_number(n):
    temp = n
    a = 0
    while n != 0:
        a = a + fact(n % 10)
        n = n // 10
    if a == temp:
        return True
    else:
        return False

def sum_of_num():
    s = 0
    for i in range(145,1000000):
        if curious_number(i):
            s = s + i
    return s

print(sum_of_num())



'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''




def factorial(n):
    fact = 1
    for i in range(1,n):
        fact = fact * i
    return fact

def sum_of_digits(n):
    num = factorial(n)
    digits_sum = 0
    while num != 0:
        digits_sum = digits_sum + (num % 10)
        num = num // 10
    return digits_sum

n = 100
print(sum_of_digits(n)) 



'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!'''


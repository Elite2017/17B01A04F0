def power(num,p):
    number = num
    for i in range(1,p):
        number = number * num
    return number

def sum_of_digits(num,p):
    n = power(num,p)
    digits_sum = 0
    while n != 0:
        digits_sum = digits_sum + (n % 10)
        n = n // 10
    return digits_sum

num = 2
p = 1000
print(sum_of_digits(num,p)) 



'''5 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?'''


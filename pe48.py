def get_power(n):
    s = 0
    for i in range(1,n + 1):
        s = s + pow(i,i)
    return s

n = 1000
print(get_power(n))




'''The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.'''


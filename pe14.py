def collatz_sequence(n):
    c = 0
    num = 0
    for x in range(2,n):
        i = x
        pr = []
        pr.append(x)
        while x > 1:
            if x % 2 == 0:
                x = x // 2
                pr.append(x)
            else :
                x = x * 3 + 1
                pr.append(x)
        if c < len(pr):
            c = len(pr)
            num = i
    return num

n = 1000000
print(collatz_sequence(n))

'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?'''


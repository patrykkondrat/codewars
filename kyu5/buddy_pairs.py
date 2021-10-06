'''
Buddy pairs
You know what divisors of a number are. The divisors of a positive
integer n are said to be proper when you consider only the divisors
other than n itself. In the following description, divisors will mean
proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two
positive integers such that the sum of the proper divisors of each
number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit)
should return the first pair (n m) of buddy pairs such that n (positive integer)
is between start (inclusive) and limit (inclusive); m can be greater than limit
and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or
(for Go lang) nil or (for Dart) null; (for Lua, Pascal, Perl) [-1, -1].

Examples
(depending on the languages)

buddy(10, 50) returns [48, 75]
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"
Notes
for C: The returned string will be free'd.
See more examples in "Sample Tests:" of your language.
'''

def div(num):
    t = []
    for h in [[i, num // i] for i in range(1, int(num ** 0.5) + 1) if not num % i]:
        for n in h:
            t.append(n)
    return sum(set(t)) - num

def buddy(start, limit):
    for i in range(start, limit):
        k = i + 1
        o = div(i)
        m = o - 1
        if m < start:
            continue
        if div(m) == k:
            return [i, m]
    return 'Nothing'


print(buddy(431414,42141414))
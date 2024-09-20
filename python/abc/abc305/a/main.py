from sys import setrecursionlimit, stdin
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from collections import Counter, deque, defaultdict
from copy import copy, deepcopy
from decimal import Decimal
from math import gcd
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from itertools import accumulate, product, permutations, combinations

# S,N
# fora ifa

# N = int(stdin.readline())



# kei = N // 5
# if N % 5 < 3:
#     print(N - N % 5)
# else:
#     print(N + (5- N % 5))

N = int(stdin.readline())
print(round(N/5)*5)
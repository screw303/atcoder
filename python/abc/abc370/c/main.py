# from sys import setrecursionlimit, stdin
# from collections import defaultdict, deque, Counter
# from itertools import permutations, combinations, product
# from functools import lru_cache
# from bisect import bisect_left, bisect_right
# from heapq import heappush, heappop
# from copy import copy, deepcopy
# from decimal import Decimal
# # from pypyjit import set_param
# # set_param('max_unroll_recursion=-1')

# setrecursionlimit(1 << 20)
# readline = stdin.readline
# INF = 10 ** 18
# MOD = 998244353
# # MOD = 1000000007
# DYDX = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# ALP = 26
# ''' Input '''
# def I(): return int(readline())
# def ST(): return readline()[:-1]
# def LI(): return list(map(int, readline().split()))
# def LII(): return list(map(lambda x: int(x) - 1, readline().split()))
# def LF(x, func): return [func() for _ in [0] * x]
# def SPI(): return map(int, readline().split())
# def SPII(): return map(lambda x: int(x) - 1, readline().split())
# def FIE(x): return [readline()[:-1] for _ in [0] * x]
# ''' Array '''
# def cmin(dp, i, x):
#     if x < dp[i]: dp[i] = x
# def cmax(dp, i, x):
#     if x > dp[i]: dp[i] = x

# ''' Alphabet '''
# def id_a(s): return ord(s) - ord('a')
# def id_A(s): return ord(s) - ord('A')
# def st_a(i): return chr(ord('a') + i)
# def st_A(i): return chr(ord('A') + i)

# ''' Other'''
# def ranges(*args): return [(i, j) for i in range(args[0]) for j in range(args[-1])]
# def nynx(y, x, ly = INF, lx = INF): return [(y + dy, x + dx) for dy, dx in DYDX if 0 <= y + dy < ly and 0 <= x + dx < lx]
# def gen(x, *args):
#     if len(args) == 1: return [x] * args[0]
#     if len(args) == 2: return [[x] * args[1] for _ in [0] * args[0]]
#     if len(args) == 3: return [[[x] * args[2] for _ in [0] * args[1]] for _ in [0] * args[0]]
#     if len(args) == 4: return [[[[x] * args[3] for _ in [0] * args[2]] for _ in [0] * args[1]] for _ in [0] * args[0]]
# ''' Output '''
# def puts(E):
#     for e in E: print(e)
# def pprint(E): 
#     print()
#     for e in E: print(e)
# def Yes(): print("Yes")
# def No(): print("No")
# def YES(): print("YES")
# def NO(): print("NO")
# def yn(x): print("Yes" if x else "No")
# def YN(x): print("YES" if x else "NO")
# ###############################################################################################

from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
A, B = int(input())

from sys import setrecursionlimit, stdin
setrecursionlimit(1 << 20)

N = [[int(_) for _ in input().split()] for i in range(N)]
N = [int(_) for _ in input().split()]

N = int(stdin.readline()())

S = stdin.readline()[:-1]



return int(stdin.readline())
return stdin.readline()[:-1]
return list(map(int, stdin.readline().split()))
return list(map(lambda x: int(x) - 1, stdin.readline().split()))
def LF(x, func): return [func() for _ in [0] * x]
return map(int, stdin.readline().split())
return map(lambda x: int(x) - 1, stdin.readline().split())
def FIE(x): return [stdin.readline()[:-1] for _ in [0] * x]


def solve(N):
    return 

print(solve(N))

def check(N):
    return 

if check(N):
    print('Yes')
else:
    print('No')


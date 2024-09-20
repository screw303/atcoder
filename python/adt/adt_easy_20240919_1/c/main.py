n=int(input())
abl = [[int(_) for _ in input().split()] for i in range(n-1)]


# print(abl.count("4"))

# count = sum(row.count(4) )
# print(f"{count}")

# for row in abl:

import itertools
flat = list(itertools.chain.from_iterable(abl))
# print(*flat)

# chflag=False
# for i in range (1,n+1):
#     if flat.count(i) == n - 1 :
#         print("Yes")
#         chflag =True
#         break

# if not chflag:
#    print("No")

import collections

# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(flat)

print( "Yes" if n-1 in c.values() else "No")
# dict_values([4, 1, 2])
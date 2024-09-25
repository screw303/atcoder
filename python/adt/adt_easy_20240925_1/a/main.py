n,x=[int(_) for _ in input().split()]

sl=[int(_) for _ in input().split()]

rsum=0
for s in sl:
    if s <= x:
        rsum = rsum + s
print(rsum)
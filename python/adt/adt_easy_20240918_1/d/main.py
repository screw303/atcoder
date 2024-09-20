
n = int(input())
xl=[int(_) for _ in input().split()]


xl.sort()

xlx = xl[n:len(xl)-n]

res = format((sum(xlx)/len(xlx)),".15f")

# print(f"{):16f}")
print(res)
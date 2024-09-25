n,k=[int(_) for _ in input().split()]

al=[int(_) for _ in input().split()]

# rsum=0
# for s in sl:
#     if s <= x:
#         rsum = rsum + s
# print(rsum)
count=0
nori= 0
for a in al:
    if a <= k - nori:
        nori +=a
    else :
        nori = 0
        count += 1
        nori +=a
    # print(nori,count)

print(count+1)

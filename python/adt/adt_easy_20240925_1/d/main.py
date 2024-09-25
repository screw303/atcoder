s = input()
t=input()

az="abcdefghijklmnopqrstuvwxyz"

index = az.find(s[0])
index2 = az.find(t[0])

sa =(index2 - index ) % 26
# print(sa)

s = list(s)
for i, t_v in enumerate(t):
    s[i] = az [(az.find(s[i]) + sa) % 26 ]

# print()

if "".join(s) == t :
  print("Yes")
else:
  print("No")



#cde 2 
#efg 4 sa =2

# rsum=0
# for s in sl:
#     if s <= x:
#         rsum = rsum + s
# print(rsum)
# count=0
# nori= 0
# for a in al:
#     if a <= k - nori:
#         nori +=a
#     else :
#         nori = 0
#         count += 1
#         nori +=a
#     # print(nori,count)

# print(count+1)

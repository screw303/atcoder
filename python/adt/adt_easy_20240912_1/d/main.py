n, m = map(int, input().split())
al = map(int, input().split())  # n
bl = map(int, input().split())  # m

al = sorted(al)
bl = sorted(bl)
isExist = True
# print(al)
# print(bl)

for i in range(n - 1):
    al[i]
    al[i + 1]
    # bl[] 見つかるまですべて
    istonariwanai = False
    for j in range(m):
        istonariwanai = istonariwanai or (al[i] < bl[j] < al[i + 1])

        # print(f"{isExist} {al[i]} < {bl[j]} < {al[i + 1]}")
    isExist = isExist and istonariwanai

print("Yes") if not isExist else print("No")

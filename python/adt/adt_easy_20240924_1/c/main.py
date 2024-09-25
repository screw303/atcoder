n,m=[int(_) for _ in input().split()]

uvll = [[int(_) for _ in input().split()] for i in range(m)]

# print( uvll.count([1,5]) )
count=0

for i in range(1,n+1):
    for j in range(i,n+1):
        for k in range(j,n+1):
            if  uvll.count([i,j]) > 0 and uvll.count([j,k]) > 0 and uvll.count([i,k]) > 0 :
                count += 1

print(count)

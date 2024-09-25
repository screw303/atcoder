sl= [int(_) for _ in input().split()]

slag=True

for i in range(7):
    if sl[i] <= sl[i+1] :
        slag=slag and True
    else:
        slag=slag and False


slag2=True
for s in sl:
    if 100 <= s <= 675 and s % 25 == 0:
        slag2=slag2 and True
    else:
        slag2=slag2 and False

print("Yes" if slag2 and slag  else "No")



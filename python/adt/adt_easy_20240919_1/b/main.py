a,b=map(int,input().split())

# for a in range(1,10):
#   for b in range(a+1,10):
    # print (f'{a},{b}' ,end=" ")
if  (a+b != 7 and a+b != 13 and b-a == 1)  :
    print("Yes")
else:
    print("No")
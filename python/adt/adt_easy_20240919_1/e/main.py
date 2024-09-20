n = int(input())
s = input()
# s = "RRUDL"

def aaa (b):
    if b =="R":
        return 1 +0j 
    elif b=="L":
        return -1 + 0j
    elif b=="D":
        return 0 - 1j
    elif b=="U":
        return 0 + 1j
    

rui = [ 0 for _ in range(n)]
rui[0]=aaa(s[0])
for i,v in enumerate(list(s)):
    rui[i] =rui[i-1] + aaa(s[i])

setl=set()
setl.add(0+0j)
flag=False
for i in rui:
    # print(i)
    if i in setl:
      flag=True
    else:
      setl.add(i)

print("Yes" if flag else "No")

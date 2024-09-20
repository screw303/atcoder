n=input()
nlist=[int(_) for _ in n ]

ha="Yes"
for i,iv in enumerate(nlist):
    if i==0:
        pass
    else:
        if nlist[i-1] > nlist[i]:
            pass
        else:
            ha = "No"
            break

print(ha)

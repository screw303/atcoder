a,b=map(str,input().split())


ax =a.zfill(18)
bx = b.zfill(18)

checkf=False
for i, axs in enumerate(ax):
    if int(ax[i]) + int(bx[i]) > 9:
        checkf = True
        break

print ("Hard" if checkf else "Easy" )


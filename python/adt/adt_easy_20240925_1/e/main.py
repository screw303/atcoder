h,w = map(int,input().split())

chw=[]
for i in range(h):
    chw.append(list(input()) )


def check_sharp(chw,i,j,w,h):
    # chw[i][j] == "#"
    # print(f'i={i},j={j},w={w}')
    count =1
    for k in range(1,min(h-i,w-j)):
        if chw[i+k][j+k] == "#":
            count +=1
            # print("  cont!")
        else :
            return count
    return count


def okikae(chw,i,j,size):
    c = size // 2 
    # print(c)
    for k in range(size//2,0,-1):
        # print(f"#k={k}, i,j,c={i},{j},{c}")
        chw[i+c-k][j+c-k] = "."
        chw[i+c+k][j+c-k] = "."
        chw[i+c+k][j+c+k] = "."
        chw[i+c-k][j+c+k] = "."
        # print(chw)
    chw[i+c][j+c] = "."
    return chw

n = min(h,w) 
sn= [ 0 for _ in range(n)]
for i in range(h):
    for j in range(w):
        if chw[i][j] == "#":
            size = check_sharp(chw,i,j,w,h)
            # print(size)
            sn[size//2-1] +=1
            chw = okikae(chw,i,j,size)
            # print(chw)
            # print(" ".join(map(str,sn)))
            # print("--")
        else :
            pass



print(" ".join(map(str,sn)))
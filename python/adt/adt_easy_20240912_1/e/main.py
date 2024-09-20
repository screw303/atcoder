n, q = map(int, input().split())
tablist = [[int(_) for _ in input().split()] for _ in range(q)]

# Wrong nlist = [ 0 for _ in range(n) ]
# Truth
nlist = set()

for i in range(q):
    if tablist[i][0] == 1:
        nlist.add((tablist[i][1], tablist[i][2]))
    elif tablist[i][0] == 2:
        nlist.discard((tablist[i][1], tablist[i][2]))
    else:
        if ((tablist[i][1], tablist[i][2]) in nlist) and (
            (tablist[i][2], tablist[i][1]) in nlist
        ):
            print("Yes")
        else:
            print("No")

# (n ^2 にならないために　set と工夫で　n になるよ)
# ＃pointは (a,b) と(b,a) があるときとみなす
# 何もしない系は xor でもいいが　set が使えるかも

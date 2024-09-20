n = int(input())

wxlist = [[int(_) for _ in input().split()] for i in range(n)]


sankalist = []
for i in range(24):
    sanka = 0
    for wx in wxlist:
        w = wx[0]
        x = (wx[1] + i) % 24
        if 8 < x < 18:
            sanka += w

    sankalist.append(sanka)
    # print(f"{x:02} time:{sanka}")

print(max(sankalist))

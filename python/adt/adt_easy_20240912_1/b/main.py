n = int(input())
s = input()
# 3 種類の文字 . | *


def check1(n, s):

    fisr = s.find("|")
    secound = s.find("|", fisr + 1)

    asta = s.find("*")

    return fisr < asta < secound


if check1(n, s):
    print("in")
else:
    print("out")

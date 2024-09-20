a = int(input())
b = int(input())
c = int(input())
x = int(input())

# 500A
# 100B
# 50c
# 50<x<20000

# 10 A
# 2 b
# 1 c
# 1<x<400

count += 0


def isFifth_h(x, a):
    return x - a >= 500


def isOne_h(x, b):
    return x - b >= 100


def isFifth(x, c):
    return x - c >= 50


def saiki(zankin, a, b, c):
    if zankin == 0:
        return True
    elif isFifth_h(zankin, a):
        saiki(zankin - a, a, b, c)
    elif isOne_h(zankin, b):
        saiki(zankin - b, a, b, c)
    elif isFifth(zankin, c):
        saiki(zankin - c, a, b, c)
    else:
        return False


def zanki(N):
    return N == 1


if zanki(N):
    print('Yes')
else:
    print('No')


zankin = x

# 50 ,3,3,3
# 100 ,2,2,2 : 0,1,0 0,0,2
saiki(x, a, b, c)

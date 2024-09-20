from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
n ,k= map(Decimal,input().split())

re=n
for i in range(int(k)):
    # print(i)
    # re =Decimal( round(re,-i-1))
    # print(re)
    scale=Decimal('1').scaleb(i+1)
    re = re.quantize(scale,rounding=ROUND_HALF_UP)
    # print(re)
    
print(format(re,".0f"))
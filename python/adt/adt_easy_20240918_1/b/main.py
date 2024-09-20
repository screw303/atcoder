n,k,x=map(int,input().split())
al=[ int(_) for _ in input().split()]

# bl=[]
# bl.([_ for _ in al[:k]])
# bl.append(x)
# bl.append([ _ for _ in al[k+1:]])
bl =al[:k] + [x] + al[k:]

print(" ".join(map(str, bl)))
# print(" ".join(map(str,al.insert(k,x))))
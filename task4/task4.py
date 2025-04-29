def one_number(m):
    p=m
    b=0
    y=sum(m)/len(m)
    while min(p)<y:
        t = p.index(min(p))
        p[t]=p[t]+1
        b += 1
    else:
        while max(p)>min(p):
            c = p.index(max(p))
            p[c]=p[c]-1
            b+=1
    return b

def num(x):
    x = int(x)
    return x

numbers=open(input(), 'r')
m=[]

while True:
    line = numbers.readline()
    if not line:
        break
    m.append(num(line))
print(one_number(m))

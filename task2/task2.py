
file1 = open(input(), "r")

x=file1.readline()
s=x.split(' ')
m = [int(item) for item in s]

r=file1.readline(2)
r=int(r)


def point(x):
    x=x.split()
    x = [int(item) for item in x]
    xmax = r + m[0]
    ymax = r + m[1]
    xmin = m[0] - r
    ymin = m[1] - r
    z = 0
    if (x[0]  > xmax or x[1] > ymax) or (x[0] < xmin or x[1] < ymin):
        z = 2
    if x[0] == xmax:
        if x[1] != m[1]:
            z=2
        if ymin < x[1] < m[1]:
            z=1
        if x[1]>m[1]:
            z=2
    if xmin < x[0] < xmax:
        if ymin < x[1] < ymax:
            z = 1
    if xmin < x[0] < xmax:
        if ymin < x[1] < ymax:
            z = 1
    return z

file2 = open("E:/proect/НТ Performance Lab/task2/file2.txt", "r")

while True:
    line = file2.readline()
    if not line:
        break
    result = point(line)
    print(result)

file1.close


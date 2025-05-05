import sys




def radius(args):
    try:
        file1 = open(args, "r")
        x = file1.readline()
        s = x.split(' ')
        m = [int(item) for item in s]
        r = int(file1.readline())
        file1.close()
        return r, m
    except ValueError:
        print("Ошибка: Неверный формат данных в файле")
        return None, None

def point(args, r, m):
    try:
        file2 = open(args, "r")
        for line in file2:
            coords = line.strip().split()
            x = [int(item) for item in coords]
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
            print(z)
        file2.close()
    except ValueError:
        print("Ошибка: Неверный формат данных в файле")



if __name__ == '__main__':
    r_data = radius(sys.argv[1])
    r, m = r_data
    point(sys.argv[2], r, m)
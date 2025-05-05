import sys


def main(args):
    s0 = int(args[0])
    s1 = int(args[1])
    p = s0 - (s0 - s1 + 1)
    q = s1 + p
    value = [1]
    if s1 != 1:
        value.append(s1)
    for i in range(1, s0):
        if q <= s0:
            if q != 0:
                if q not in value:
                    value.append(q)
        if q >= s0:
            q = q - s0
            if q != 0:
                if q not in value:
                    value.append(q)
        else:
            q = q + p
            if q <= s0:
                if q not in value:
                    value.append(q)
    print(*value, sep='')


if __name__ == '__main__':
    main(sys.argv[1:])

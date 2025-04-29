def circular_array(n):
    s = [int(i) for i in n]
    p = s[0] - (s[0] - s[1] + 1)
    q = s[1] + p

    value = [1]
    if s[1] != 1:
        value.append(s[1])
    for i in range(1, s[0]):
        if q <= s[0]:
            if q != 0:
                if q not in value:
                    value.append(q)
        if q >= s[0]:
            q = q - s[0]
            if q != 0:
                if q not in value:
                    value.append(q)
        else:
            q = q + p
            if q <= s[0]:
                if q not in value:
                    value.append(q)
    return value


print(*circular_array(input().split()), sep='')


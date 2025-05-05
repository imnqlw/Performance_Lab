import sys


def one_number(m):
    m.sort()
    median_index = len(m) // 2
    median = m[median_index]
    count = 0
    for num in m:
        count += abs(num - median)

    return count


def read_numbers_from_file(args):
    numbers = open(args, 'r')
    m = []
    for line in numbers:
        m.append(int(line.strip()))
    return m


if __name__ == '__main__':
    numbers = sys.argv[1]
    num = read_numbers_from_file(numbers)
    result = one_number(num)
    print(result)

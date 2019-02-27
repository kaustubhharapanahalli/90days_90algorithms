def sockMerchant(n, ar):
    a = set(ar)
    b = {}
    for i in a:
        b[i] = ar.count(i)

    count = 0
    for i in b.values():
        count += int(i / 2)

    return count

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

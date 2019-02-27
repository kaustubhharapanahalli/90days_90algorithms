if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    arr2 = [str(i) for i in arr]
    print(' '.join(arr2))

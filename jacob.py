testCases = int(input())
for j in range(testCases):
    n, k, s = map(int, input().strip().split())

    goBack = (k) + (k-s) + (n-s)
    restart = (k) + n
    m1 = min(goBack, restart)
    print(f'Case #{j + 1}: {m1}')


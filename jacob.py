n = 8 #Number of levels
k = 4 #Current Pos
s = 2 #Sword pos
testCases = int(input())
for j in range(testCases):
    n, k, s = map(int,input().strip().split())

    goBack = (k-1) + (k-s) + (n-s) + 1
    restart = (k-1) + n
    m1 = max(goBack, restart)
    print(f'Case #{i}: {min1}')


def func1(x):
    for n in range(len(x)):
        index = n
        value = int(x[n])

        if (index%2 != value%2):
            return False

    return True

testCases = int(input())
for j in range(testCases):
    l, r = map(int, input().strip().split())
    count = 0
    for t in range(l,r+1):
        x = str(t)
        if func1(x):
            ++count
    print(f'Case #{j+1}: {count}')


#N = number of levels
#K = Level you are in
#S = Level you must go to

# case 1:
TCases = int(input())


for i in range(TCases):
    N,K,S = map(int,input().strip().split())
    TimeGoBack = (K-1) + (K-S) + (N-S + 1)
    TimeRestart = (K) + N
    minTime = min(TimeGoBack,TimeRestart)
    print(f'Case #{i+1}: {minTime}')





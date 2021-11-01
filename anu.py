#N = number of levels
#K = Level you are in
#S = Level you must go to

# case 1:
K = 5
S = 3
N = 8

TimeGoBack = (K-1) + (K-S) + (N-S + 1)
TimeRestart = (K-1) + N



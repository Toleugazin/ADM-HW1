N = int(raw_input())
O = raw_input().split(' ')
P = list(map(int, O))
Q = set(P)
R = sorted(list(Q))
print R[-2]

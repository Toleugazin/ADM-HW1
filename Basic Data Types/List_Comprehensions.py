X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print ans

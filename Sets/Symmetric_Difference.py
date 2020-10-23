int(raw_input())
N = raw_input().split()
Nint = set(list(map(int, N)))
int(raw_input())
M = raw_input().split()
Mint = set(list(map(int, M)))
res = []
for i in list(Nint.difference(Mint)):
    res.append(i)
for j in list(Mint.difference(Nint)):
    res.append(j)
for k in sorted(res):
    print k

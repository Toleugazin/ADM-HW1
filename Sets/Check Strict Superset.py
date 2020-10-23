A = set(raw_input().split())
b = int(raw_input())
ans = True
for _ in range(b):
    tmp = set(raw_input().split())
    if not (len(A) > len(A & tmp) and len(tmp - A) == 0):
        ans = False
        break
print ans

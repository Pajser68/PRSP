n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    a = f[i] - 1
    b = f[a] - 1
    c = f[b] - 1
    if c == i:
        print("YES")
        break
else:
    print("NO")
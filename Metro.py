n, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s -= 1  # zero-based index

if a[0] == 0:
    print("NO")
elif a[s] == 1:
    print("YES")
else:
    for i in range(s + 1, n):
        if a[i] == 1 and b[i] == 1 and b[s] == 1:
            print("YES")
            break
    else:
        print("NO")
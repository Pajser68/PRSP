n, m = map(int, input().split())
parent = list(range(n))
size = [1] * n

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return False
    if size[u_root] < size[v_root]:
        parent[u_root] = v_root
        size[v_root] += size[u_root]
    else:
        parent[v_root] = u_root
        size[u_root] += size[v_root]
    return True

components = n
max_size = 1
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if union(a, b):
        components -= 1
        max_size = max(max_size, size[find(a)])
    print(components, max_size)
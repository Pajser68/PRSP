def bfs(sx, sy, ex, ey, grid, n, m):
    dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    queue = [(sx, sy)]
    prev = [[None]*m for _ in range(n)]
    head = 0
    grid[sx][sy] = '#'  # Mark as visited
    while head < len(queue):
        x, y = queue[head]
        head += 1
        for dx, dy, move in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                prev[nx][ny] = (x, y, move)
                if (nx, ny) == (ex, ey):
                    return prev
                grid[nx][ny] = '#'
                queue.append((nx, ny))
    return prev

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            sx, sy = i, j
        if grid[i][j] == 'B':
            ex, ey = i, j

prev = bfs(sx, sy, ex, ey, grid, n, m)

if prev[ex][ey]:
    path = []
    x, y = ex, ey
    while (x, y) != (sx, sy):
        px, py, move = prev[x][y]
        path.append(move)
        x, y = px, py
    print("YES")
    print(len(path))
    print(''.join(reversed(path)))
else:
    print("NO")
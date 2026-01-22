n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

monsters = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            start = (i, j)
        if grid[i][j] == 'M':
            monsters.append((i, j))

# Step 1: BFS from all monsters
monster_time = [[float('inf')] * m for _ in range(n)]
q = monsters[:]
for mx, my in monsters:
    monster_time[mx][my] = 0
head = 0
while head < len(q):
    x, y = q[head]
    head += 1
    for dx, dy, _ in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and monster_time[nx][ny] == float('inf'):
            monster_time[nx][ny] = monster_time[x][y] + 1
            q.append((nx, ny))

# Step 2: BFS from player
player_time = [[-1] * m for _ in range(n)]
prev = [[None] * m for _ in range(n)]
sx, sy = start
player_time[sx][sy] = 0
q = [(sx, sy)]
head = 0
escaped = None
while head < len(q):
    x, y = q[head]
    head += 1
    # Check if on boundary
    if x == 0 or x == n-1 or y == 0 or y == m-1:
        escaped = (x, y)
        break
    for dx, dy, move in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and player_time[nx][ny] == -1:
            if player_time[x][y] + 1 < monster_time[nx][ny]:
                player_time[nx][ny] = player_time[x][y] + 1
                prev[nx][ny] = (x, y, move)
                q.append((nx, ny))

if escaped is None:
    print("NO")
else:
    path = []
    x, y = escaped
    while (x, y) != start:
        px, py, move = prev[x][y]
        path.append(move)
        x, y = px, py
    print("YES")
    print(len(path))
    print(''.join(reversed(path)))
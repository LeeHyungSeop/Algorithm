from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def showGraph() :
    for i in range(n) :
        for j in range(m) :
            print(graph[i][j],end=' ')
        print('\n')
    print('\n')

def BFS(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        
        showGraph()
    
    return graph[n-1][m-1]

print(BFS(0,0))
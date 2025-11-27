graph = [[0] * 11 for _ in range(11)]
visited = [0] * 11

def dfs(v, n):
    print(v, end=" ")
    visited[v] = 1

    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i, n)


def bfs(start, n):
    queue = []
    visited_b = [0] * 11

    queue.append(start)
    visited_b[start] = 1

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited_b[i] == 0:
                queue.append(i)
                visited_b[i] = 1


# MAIN PROGRAM
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        graph[i][j] = row[j - 1]

start = int(input("Enter starting vertex: "))

print("DFS:", end=" ")
visited = [0] * 11
dfs(start, n)

print("\nBFS:", end=" ")
bfs(start, n)

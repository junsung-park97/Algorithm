import sys
from collections import deque

input = sys.stdin.readline

def dfs (start:int) -> None:  
  visited[start] = True
  print(start, end=' ')

  for i in graph[start]:
    if visited[i] == False:
      dfs(i)

def bfs(start:int) -> None:
  queue = deque([start])
  visited[start] = True

  while queue:
    node = queue.popleft()
    print(node, end=' ')

    for i in graph[node]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
for i in range(1, n + 1):
  graph[i].sort()

dfs(v)
print()
visited = [False for _ in range(n + 1)]
bfs(v)

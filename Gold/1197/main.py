import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

vertexs, edges = map(int, input().split())
parent = [x for x in range(vertexs + 1)]
total_weight = 0
count = 0
tree = []

# 선택정점의 root노드를 찾기위해
def find(vertex:int) -> int:
  # 내가 찾는 정점이 대표 정점이라면
  if parent[vertex] == vertex:
    return vertex
  
  parent[vertex] = find(parent[vertex])
  return parent[vertex]

# 두 정점을 합치기 위해   
def union(verA:int, verB:int) -> bool:
  global count

  root_A = find(verA)
  root_B = find(verB)

  if root_A != root_B:
    parent[root_B] = root_A
    count += 1
    return True
  return False

for _ in range(edges):
  verA, verB, weight = map(int, input().split())
  tree.append((weight, verA, verB))

tree.sort()

for weight, verA, verB in tree:
  if union(verA, verB):
    total_weight += weight

  if count == (vertexs - 1):
    break

print(total_weight)
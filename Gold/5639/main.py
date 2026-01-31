import sys

sys.setrecursionlimit(10**6)

def to_tree(arry):
  if len(arry) == 0:
    return 0
  
  root = arry[0]
  # ⚠️ 오른쪽 서브트리 시작점 찾기
  idx = len(arry)

  for i in range(1, len(arry)):
    if root < arry[i]:
      idx = i
      break

  left = arry[1:idx]
  right = arry[idx:]

  to_tree(left)
  to_tree(right)
  print(root)


preorder = [int(x) for x in sys.stdin]
to_tree(preorder)
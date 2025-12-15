import sys

input = sys.stdin.readline


strings = input()
arr = []
n = int(input())

for s in strings:
  arr.append(s)

print(arr[n - 1])


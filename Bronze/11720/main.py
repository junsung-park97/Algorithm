import sys

input = sys.stdin.readline

arr = []
n = int(input().rstrip())
nums = input().rstrip()

for num in nums:
  arr.append(int(num))

total = sum(arr)
print(total)


import sys

input = sys.stdin.readline
nums = []
chars = []
temp = 0

for i in range(3):
  num = int(input().rstrip())
  chars.append(str(num))
  nums.append(num)

print((nums[0] + nums[1]) - nums[2])
print(int(chars[0] + chars[1]) - int(chars[2]))
import sys

input = sys.stdin.readline

while(True):
  nums = list(map(int, input().split()))
  nums.sort(reverse=True)
  c,a,b = nums

  if (a == 0 and b ==0 and c == 0) :
    break
  
  if ((a ** 2) + (b ** 2) == (c ** 2)):
    print('right')
  else :
    print('wrong')

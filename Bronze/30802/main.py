import sys

input = sys.stdin.readline

total = int(input())
s_answer = 0
p_answer = 0

size = list(map(int, input().split()))

t,p = map(int, input().split())

for s in size:
  s_answer += (s + t - 1) // t

p_answer = int(total / p)
mod = int(total) - int(p_answer * p) 

print(s_answer)
print(p_answer, mod)
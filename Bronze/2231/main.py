import sys

input = sys.stdin.readline

N = int(input())
answer = 0

for i in range(1, N):
    total = i
    for digit in str(i):
        total += int(digit)

    if total == N:
        answer = i
        break

print(answer)
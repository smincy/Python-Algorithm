# BJ_2525_오븐시계
A, B = map(int, input().split())
C = int(input())

if (B + C) >= 60:
    A += (B + C) // 60
    B = (B + C) % 60
else:
    B += C

if A >= 24:
    A -= 24

print(A, B)

###########################
# 다른 풀이
A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B + C
print((total_minutes // 60) % 24, total_minutes % 60)
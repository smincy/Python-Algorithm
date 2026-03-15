n = int(input())
list = list(map(int, input().split()))
target = int(input())

count = 0
for i in list:
    if i == target:
        count += 1

print(count)
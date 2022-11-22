m = int(input())
n = int(input())

start = ((m - 1) // 2) * 2 + 1

for i in range(start, n - 1, -2):
    print(i)

m = int(input())
n = int(input())
for i in range(m, n - 1, -2):
    if i % 2 != 0:
            print(i)

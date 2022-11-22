a, b = int(input()), int(input())
c, d = int(input()), int(input())
ab = 0
cd = 0
if a > b:
    ab = b
else:
    ab = a
if c > d:
    cd = d
else:
    cd = c
if ab < cd:
    print(ab)
else:
    print(cd)

s1, f1 = int(input()), int(input())
s2, f2 = int(input()), int(input())
if (-1<= s1 - s2<= 1) and (-1<=f1 - f2 <=1):
    print('Yes')
else:
    print('NO')

    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    x = x2 - x1  # разность координат по оси x
    y = y2 - y1  # разность координат по оси y

    # Так как король может ходить во все направления, но только на одну клетку, нужно сделать проверку: отличается ли конечная позиция от начальной на 1
    if -1 <= x <= 1 and -1 <= y <= 1:
        print('YES')
    else:
        print('NO')
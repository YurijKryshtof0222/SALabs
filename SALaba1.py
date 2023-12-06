import math


def tabulation_range(x1, x2, step):
    var = x1
    while var <= x2:
        yield var
        var += step


def func1(x):
    return 15 * math.sin(x + 1)


def func2(x):
    return 10 * math.cos(2 * x - 2.4) + 12


if __name__ == '__main__':
    f1_star = 12.82
    f2_star = 16
    x1 = 6.0
    x2 = 8.0
    step = 0.1

    paretoSet = [(x, func1(x), func2(x)) for x
                 in tabulation_range(x1=x1, x2=x2, step=step)
                 if func1(x) >= f1_star and func2(x) >= f2_star]
    max_from = []
    min_from = []

    print('Pareto set: ')
    for x, f1, f2 in paretoSet:
        f1, f2 = f1 / f1_star, f2 / f2_star
        print(f'x = {round(x, 1)}, f1 = {f1}, f2 = {f2}')
        if f1 > f2:
            max_from.append(f1)
            min_from.append(f2)
        else:
            max_from.append(f2)
            min_from.append(f1)

    print()

    print('Min values: ')
    for value in min_from:
        print(value)

    print()

    print('Max values: ')
    for value in max_from:
        print(value)

    print()

    print('minmax = ', min(max_from))
    print('maxmin = ', max(min_from))
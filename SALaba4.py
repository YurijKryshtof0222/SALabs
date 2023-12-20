def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print('\t', [format(col, '.4f') for col in row])


def print_array(arr: list[int]) -> None:
    print('\t', [format(col, '.4f') for col in arr])


def generate_g_matrix(g_arr: list[int]) -> list[list[int]]:
    result = list()
    for i in range(len(g_arr)):
        result.append([])
        for j in range(len(g_arr)):
            result[i].append(g_arr[i] / g_arr[j])
    return result


def calcualte_Vi(g_matrix: list[list[int]]) -> list[int]:
    result = list()
    for row in range(len(g_matrix)):
        mult = 1
        for col in range(len(g_matrix[0])):
            mult *= g_matrix[row][col]
        result.append(pow(mult, 1/4))
    return result


def calcualte_Pi(vi_arr: list[int]) -> list[int]:
    result = list()
    vi_sum = sum(vi_arr)

    for vi in vi_arr:
        result.append(vi / vi_sum)

    return result


def calcualte_En(g_matrix: list[list[int]], pi_arr: list[int]) -> list[list[int]]:
    result = [[], []]
    for i in range(len(g_matrix)):
        sum = 0
        for j in range(len(g_matrix)):
            sum += g_matrix[i][j] * pi_arr[j]
        result[0].append(sum)
        result[1].append(result[0][i] / pi_arr[i])
    return result


g_arr = [40, 50, 30, 20]
g_matrix = generate_g_matrix(g_arr)
vi_arr = calcualte_Vi(g_matrix)
pi_arr = calcualte_Pi(vi_arr)
en_matrix = calcualte_En(g_matrix, pi_arr)

print('Масив значень g = \n\t', g_arr)

print('Матриця попарних порівнянь об\'єктів = ')
print_matrix(g_matrix)

print('Масив значень головних власних векторів vi =')
print_array(vi_arr)

print('Масив значень вектор пріоритетів pi =')
print_array(pi_arr)

print('Матриця векторів En =')
print_matrix(en_matrix)

n = len(en_matrix[1])
lambda_max = sum(en_matrix[1]) / n
ip = (lambda_max - n) / (n - 1)
vp = ip / 0.9

print('λmax =', lambda_max)
print('ip = ', ip)
print('vp =', vp)

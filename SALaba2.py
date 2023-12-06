def tabulation_range(x1, x2, step):
    var = x1
    while var <= x2:
        yield var
        var += step


def calc_matrix(func, x_from, x_to, step):
    return [[func(i, j) for j in tabulation_range(x_from, x_to, step)]
            for i in tabulation_range(x_from, x_to, step)]


def min_of_each_columns(matrix, rows, cols):
    min_elements = []
    for i in range(rows):
        min = matrix[0][i]
        for y in range(cols):
            if matrix[y][i] < min:
                min = matrix[y][i]
        min_elements.append(min)

    return min_elements


def extra_matrix(matrix, m, n, max_value):
    return [[matrix[i][j] - max_value for j in range(0, n)]
            for i in range(0, m)]


def find_close_element(f12_extra_matrix, f21_extra_matrix, step):
    x1 = x2 = 0
    close_list = list()
    for i in range(9):
        for j in range(9):
            if f12_extra_matrix[i][j] >= 0 and f21_extra_matrix[i][j] >= 0:
                if f12_extra_matrix[i][j] > f12_extra_matrix[i][j]:
                    close_list.append((x1, x2, f12_extra_matrix[i][j]))
                else:
                    close_list.append((x1, x2, f21_extra_matrix[i][j]))
            x2 += step
        x1 += step
        x2 = 0

    if not close_list:
        return None

    closest_index = 0
    min_distance = abs(close_list[0][2])

    for i in range(1, len(close_list)):
        current_distance = abs(close_list[i][2])

        if current_distance < min_distance:
            closest_index = i
            min_distance = current_distance

    return close_list[closest_index]


def print_row(row, end='\n'):
    print('[', end='')
    for i in row:
        print(f'{i:.2f}', end='\t')
    print(end=']' + end)


def print_matrix(matrix, end='\n'):
    print('[')
    for row in matrix:
        print_row(row, '\n')
    print(']' + end)


func12 = lambda x1, x2: (
        -8 * x1 * x2 ** 2 + 9 * x2 ** 2 - 37 * x2 + 4 * x1 ** 2 + 50)
func21 = lambda x1, x2: (
        -2 * (x2 - 5) ** 2 - 9 * (x1 - 0.95) ** 2 * x2 + 2 * x1 * x2 + 50)
step = 0.25

if __name__ == '__main__':
    f12_matrix = calc_matrix(func12, 0, 2, step)
    f21_matrix = calc_matrix(func21, 0, 2, step)

    f12_mins_of_each_row = [min(row) for row in f12_matrix]
    f21_mins_of_each_col = min_of_each_columns(f21_matrix, 9, 9)

    max_of_f12_mins = max(f12_mins_of_each_row)
    max_of_f21_mins = max(f21_mins_of_each_col)

    f12_extra_matrix = extra_matrix(f12_matrix, 9, 9, max_of_f12_mins)
    f21_extra_matrix = extra_matrix(f21_matrix, 9, 9, max_of_f21_mins)

    print('f12 function tabulation matrix', end=' = ')
    print_matrix(f12_matrix)
    print('f21 function tabulation matrix', end=' = ')
    print_matrix(f21_matrix)

    print('mins of each row     of f12 ', end=' = ')
    print_row(f12_mins_of_each_row)
    print('mins of each column  of f21 ', end=' = ')
    print_row(f21_mins_of_each_col)

    print('max of f12 mins = ', max_of_f12_mins)
    print('max of f21 mins = ', max_of_f21_mins)
    print()
    print('f12 extra_matrix', end=' = ')
    print_matrix(f12_extra_matrix)
    print('f21 extra_matrix', end=' = ')
    print_matrix(f21_extra_matrix)

    print()
    closest_element = find_close_element(f12_extra_matrix, f21_extra_matrix, step)
    print(
        f'Result - closest element : x1 = {closest_element[0]}, x2 = {closest_element[1]}, value = {closest_element[2]}')

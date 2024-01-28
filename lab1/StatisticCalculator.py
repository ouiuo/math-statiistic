import math as mt


def calculate_statistic_function(normilize_el, dx):
    x = list([0])
    y = list([0])

    for i in range(1, len(normilize_el) + 1):
        x.append(x[i - 1] + dx)
        y.append(y[i - 1] + normilize_el[i - 1])
        if i == len(normilize_el):
            y[i] = round(y[i])
    return x, y


def calculate_empheric_rule(data, dx, n):
    min_el, max_el = min(data), max(data)
    counted_el = list()
    bar_names = list()

    x = min_el

    for i in range(n):
        left = x
        right = x + dx
        if i == (n - 1):
            counted_el.append(sum(left <= y <= max_el for y in data))
        else:
            counted_el.append(sum(left <= y < right for y in data))

        bar_names.append(str(round(x, 2)) +
                         '\n - \n' +
                         str(round(x + dx, 2)))
        x += dx

    normilize_el = [i / len(data) for i in counted_el]
    return counted_el, normilize_el, bar_names


def calculate_expected_value(data):
    print('Start calculate expected value')
    return sum(data) / len(data)


def calculate_dispersion(data, expected_value):
    print('Start calculate dispersion')
    dispersion = 0
    for a in data:
        dispersion += pow(a - expected_value, 2)

    return dispersion / (len(data) - 1)


def calculate_dx(data):
    R = max(data) - min(data)

    # Часто встречается записанным через десятичный логарифм:
    # n = 1 + ⌊ 3.322 lg N ⌋
    n = (1 + int(3.322 * mt.log(len(data), 10)))
    dx = R / (1 + int(3.322 * mt.log(len(data), 10)))
    return dx, n


def calculate(data):
    expected = calculate_expected_value(data)
    dispersion = calculate_dispersion(data, expected)
    dx, n = calculate_dx(data)

    return expected, dispersion, dx, n

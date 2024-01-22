def calculate_expected_value(data):
    print('Start calculate expected value')
    return sum(data)/len(data)

def calculate_dispersion(data, expected_value):
    print('Start calculate dispersion')
    dispersion = 0
    for a in data:
        dispersion+=pow(a-expected_value, 2)

    return dispersion/(len(data)-1)




def calculate(data):
    expected = calculate_expected_value(data)
    dispersion = calculate_dispersion(data, expected)

    return expected, dispersion

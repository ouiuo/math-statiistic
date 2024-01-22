# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

from model.Config import parse_config
from DataProcessor import get_data
from StatisticCalculator import calculate

config = ''




def do():
    print('Start', datetime.today())
    data = get_data(config)
    print(data)

    print(calculate(data))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = parse_config()
    do()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

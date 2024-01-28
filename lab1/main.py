# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

from model.Config import parse_config
from DataProcessor import get_data
from StatisticCalculator import calculate

import numpy as np
import math as mt
import StatisticCalculator as stc
from matplotlib import pyplot as plt
from blume.table import table

config = ''


def show(normilize_el, bar_names, statFx, statFy):
    fig, (ax1, ax2) = plt.subplots(2, 1,
                       constrained_layout = True)
    # fig.tight_layout()
    ax1.grid(True)
    ax1.bar(bar_names, normilize_el)
    # plt.subplots_adjust(left=0.3, bottom=0.2)
    # fig.tight_layout(pad=1.0)
    tab = table(ax1, [normilize_el], loc='top', colLabels=[x.replace('\n', '') for x in bar_names],
                rowLabels=['Эмперические частоты'])

    ax2.plot(statFx, statFy, label='Стат.ф. распределения')
    ax2.grid(True)
    ax2.legend()
    plt.xticks(np.arange(min(statFx), max(statFx) + 1, (max(statFx) - min(statFx)) / (len(statFx) - 1)))
    plt.savefig("myimage.png", dpi=250)
    plt.show()


def do():
    print('Start', datetime.today())
    data = get_data(config)

    expected_value, dispersion, dx, n = calculate(data)

    print("\n\n\n======================================")
    print('Expected value:  ' + str(expected_value))
    print("dispersion:      " + str(dispersion))
    print("dx:              " + str(dx))
    print("number of grups: " + str(n))

    counted_el, normilize_el, bar_names = stc.calculate_empheric_rule(data, dx, n)

    statFx, statFy = stc.calculate_statistic_function(normilize_el, dx)

    show(normilize_el, bar_names, statFx, statFy)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = parse_config()
    do()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

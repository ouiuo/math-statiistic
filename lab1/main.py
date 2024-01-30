# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

from model.Config import parse_config
from DataProcessor import get_data
from DataProcessor import store_data
from StatisticCalculator import calculate
from StatisticCalculator import laplas_f
from StatisticCalculator import calculate_theoretical_probability

import numpy as np
import math as mt
import StatisticCalculator as stc
from matplotlib import pyplot as plt
from blume.table import table

config = ''


def show(normilize_el, bar_names, statFx, statFy, probability):
    fig, axs = plt.subplots(3, 1,
                                   constrained_layout=True)
    ax1, ax2, ax3 = axs[0], axs[1], axs[2]
    # fig.tight_layout()
    ax1.grid(True)
    ax1.bar(bar_names, normilize_el)
    # plt.subplots_adjust(left=0.3, bottom=0.2)
    # fig.tight_layout(pad=1.0)
    tab = table(ax1, [normilize_el], loc='top', colLabels=[x.replace('\n', '') for x in bar_names],
                rowLabels=['Эмперические частоты'])

    ax3.axis(False)
    ax3.grid(True)

    tab2 = table(ax3, [[round(x, 4) for x in probability]], loc='center', colLabels=[x.replace('\n', '') for x in bar_names],
                 rowLabels=['Теоретические частоты'])
    tab2.auto_set_font_size(False)
    tab2.set_fontsize(5)
    # tab2.scale(2, 2)

    ax2.plot(statFx, statFy, label='Стат.ф. распределения')
    ax2.grid(True)
    ax2.legend()
    plt.xticks(np.arange(min(statFx), max(statFx) + 1, (max(statFx) - min(statFx)) / (len(statFx) - 1)))
    plt.savefig("myimage.png", dpi=250)
    plt.show()


def do(search=False):
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


    #     lab2 лаба 2 лаб2
    a = stc.calculate_a(data, expected_value, dispersion)
    e = stc.calculate_e(data, expected_value, dispersion)
    print("A value is:      " + str(a))
    print("E value is:      " + str(e))

    # lab3 лаба 3 лаб3

    theoretical_probability = calculate_theoretical_probability(data, dx, n, expected_value, dispersion)

    if not search:
        show(normilize_el, bar_names, statFx, statFy, theoretical_probability)
    return e, data


def min_a_found():
    a = 1
    while a > 0.00001:
        b, data = do(True)
        if abs(b) < abs(a):
            a = abs(b)
            print('new min a value: ' + str(a))
            print(a)
            store_data(data, 'min_data.csv')
        print(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = parse_config()
    # min_a_found()
    laplas_f(1)
    do()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
This is the third file for this project to plot the scatterplot for the genres
"""
import matplotlib.pyplot as plt
import numpy as np

import main


y = main.categorise_by_year(main.read_csv('spotify.csv'))
year_list = [2017, 2018, 2019, 2020, 2021]


def find_genre_count_for_year(year: int) -> list[dict[str: int]]:
    """ufgdksj"""
    k = year - 2017
    z = main.categorise_by_genre(y[k])
    l1 = []
    for j in range(len(z)):
        l1.append(z[j][0])
    return l1


def do_all_work() -> list[list]:
    """
    This function does all the work
    """
    l6 = []
    for i in range(26):
        for y in range(2017, 2022):
            l = find_genre_count_for_year(y)
            m = [l[i][item] for item in l[i]]
            n = m[0]
            l6.append(n)
    l1 = []
    splits = np.array_split(l6, 26)
    for array in splits:
        l1.append(list(array))
    return l1


def linegraph() -> None:
    """
    This plots the linegraph
    """
    for n in range(26):
        plt.plot(year_list, do_all_work()[n], linewidth=3, label=main.Genres[n])

    plt.legend()

    plt.xticks([2017, 2018, 2019, 2020])

    plt.show()

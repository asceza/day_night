
# https://stackoverflow-com.translate.goog/questions/1574088/plotting-time-in-python-with-matplotlib?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=sc
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot_date.html
# https://pythonworld.ru/moduli/modul-datetime.html
# https://voshod-solnca.ru/sun

import csv
import matplotlib.pyplot as plt
import matplotlib.dates

import datetime

INPUT_FILENAMES = ["Мурманск.csv",
                    "Санкт-Петербург.csv",
                    "Москва.csv",
                    "Сочи.csv",
                    "Каир.csv",
                    "Аддис-Абеба.csv",
                    "Антананариву.csv",
                    "Кейптаун.csv",
                    "Хобарт.csv"]


def get_date(filename):
    with open(filename, "r+", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        raw_date_lst = []
        for row in reader:
            raw_date_lst.append(datetime.datetime.strptime(row[0], '%d.%m'))
        return raw_date_lst


def get_time(filename):
    with open(filename, "r+", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        raw_time_lst = []
        for row in reader:
            raw_time_lst.append(datetime.datetime.strptime(row[3], '%H:%M:%S'))
        return raw_time_lst


def main():
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 8))

    for filename in INPUT_FILENAMES:
        dates = get_date(filename)
        times = get_time(filename)

        plt.plot_date(dates, times, markersize = "1", label=filename.split(".")[0])  # последний аргумент - из названия файла забираем только название города

    ax.yaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))  # '%H:%M:%S'
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d.%m'))

    # тики указываем явно
    x_tick_lst = [datetime.datetime(1900, 1, 1, 0, 0),
                    datetime.datetime(1900, 3, 20, 0, 0),
                    datetime.datetime(1900, 6, 22, 0, 0),
                    datetime.datetime(1900, 9, 23, 0, 0),
                    datetime.datetime(1900, 12, 31, 0, 0)]
    ax.set_xticks(x_tick_lst)

    y_tick_lst = [datetime.datetime(1900, 1, 1, 0, 0),
                    datetime.datetime(1900, 1, 1, 4, 0),
                    datetime.datetime(1900, 1, 1, 8, 0),
                    datetime.datetime(1900, 1, 1, 12, 0),
                    datetime.datetime(1900, 1, 1, 16, 0),
                    datetime.datetime(1900, 1, 1, 20, 0),
                    datetime.datetime(1900, 1, 1, 23, 59)]
    ax.set_yticks(y_tick_lst)

    ax.set_title("Продолжительность светового дня\n(время от восхода до захода солнца)")
    ax.set_xlabel("Даты, дд.мм")
    ax.set_ylabel("Продолжительность, чч:мм")
    ax.grid(linestyle = '--', color = "black", alpha = 0.2)


    ax.legend(numpoints=6, fontsize=10)  # первый аргумент - кол-во точек в легенде
    plt.show()




if __name__ == '__main__':
    main()

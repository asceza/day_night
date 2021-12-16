
# https://stackoverflow-com.translate.goog/questions/1574088/plotting-time-in-python-with-matplotlib?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=sc
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot_date.html
# https://pythonworld.ru/moduli/modul-datetime.html
# https://voshod-solnca.ru/sun



import csv
import matplotlib.pyplot as plt
import matplotlib.dates

import datetime


INPUT_FILENAME = "spb.csv"



def get_date():
    with open(INPUT_FILENAME, "r+", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        raw_date_lst = []
        for row in reader:
            # x_values.append(datetime(row[0]))
            month = row[0].split(".")[1]
            day = row[0].split(".")[0]
            raw_date_lst.append(datetime.date(2021, int(month), int(day)))
        return raw_date_lst


def translate_date(raw_date_lst):
    dates = matplotlib.dates.date2num(raw_date_lst)
    return dates



def get_time():
    with open(INPUT_FILENAME, "r+", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        raw_time_lst = []
        for row in reader:
            raw_time_lst.append(datetime.datetime.strptime(row[3], '%H:%M'))
        # print(raw_time_lst)
        return raw_time_lst






if __name__ == '__main__':
    raw_date_lst = get_date()
    dates = translate_date(raw_date_lst)

    times = get_time()

    # print(raw_date_lst[0])
    # print(dates[0])
    # print(raw_time_lst[0])

    fig, ax = plt.subplots(figsize=(14,10))
    plt.plot_date(dates, times, color = "red", markersize = "2")
    ax.yaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))  # '%H:%M:%S'
    plt.show()

import pandas

data = pandas.read_csv("weather_data.csv")


data_dictionary = data.to_dict()


temperature_list = data["temp"].to_list()


def average_temperature():
    average = data["temp"].mean()
    print(average)


def max_temperature():
    maximum = data["temp"].max()
    print(maximum)


def max_temperature_day():
    hottest_day = data[data.temp == data.temp.max()].day
    print(hottest_day)


max_temperature_day()

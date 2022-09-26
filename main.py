import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dictionary = data.to_dict()


temperature_list = data["temp"].to_list()


def average_temperature():
    average = data["temp"].mean()
    return average


avg = average_temperature()
print(avg)

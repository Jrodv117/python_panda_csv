import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dictionary = data.to_dict()


temperature_list = data["temp"].to_list()


def average_temperature():
    average = data["temp"].mean()
    return average


def max_temperature():
    max = data["temp"].max()
    return max


avg = average_temperature()
max_temperature = max_temperature()

print(avg)
print(max_temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dictionary = data.to_dict()


temperature_list = data["temp"].to_list()


def average_temperature():
    total_temperature = 0
    for i in temperature_list:
        total_temperature += i
    average = total_temperature / (len(temperature_list))
    return average


avg = average_temperature()
print(avg)

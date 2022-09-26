import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dictionary = data.to_dict()
print(data_dictionary)

temperature_list = data["temp"].to_list()
print(temperature_list)

import pandas

data = pandas.read_csv("weather_data.csv")

# Create a dataframe from scratch

data_dict = {
    "students" : ["Army","James","Angela"],
    "score" : [76,56,65]
}
data = pandas.DataFrame(data_dict)
print(data)

#output :
# 0     Army     76
# 1    James     56
# 2   Angela     65

#Create a new csv file :
data.to_csv("new_data.csv")
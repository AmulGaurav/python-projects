import pandas

data = pandas.read_csv("C:\\Users\\admin\Documents\\python-projects\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

all_color = data["Primary Fur Color"]

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])

red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
              "Fur Color" : ["Gray", "Cinnamon", "Black"],
              "Count" : [gray_squirrel, red_squirrel, black_squirrel]
             }

new_data = pandas.DataFrame(color_dict)

new_data.to_csv("squirrel\\squirrel_count.csv")

print(new_data)
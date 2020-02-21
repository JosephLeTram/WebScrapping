import requests
import pandas as pd
from bs4 import BeautifulSoup


# Assign the URL to the variable "page"
page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.Xk9YnSgvNEY")

# Get the content from the html and parse the data
soup = BeautifulSoup(page.content, "html.parser")

# Use the find() to find the wanted section which we want to extract data from
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_="tombstone-container")
# print(items[0].find(class_="period-name").get_text())
# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

# Use the list comprehension to find all the list of info
period_names = [item.find(class_="period-name").get_text() for item in items]
short_descriptions = [
    item.find(class_="short-desc").get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]

# Use Pandas to write into CSV file and do some data analytic
weather_stuff = pd.DataFrame(
    # Write lists into dictionary
    {"Period": period_names,
     "Short_Descriptions": short_descriptions,
     "Temperatures": temperatures,
     }
)

print(weather_stuff)
weather_stuff.to_csv("Weather.csv")

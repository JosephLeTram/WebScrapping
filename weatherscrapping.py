import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.Xk9YnSgvNEY")
soup = BeautifulSoup(page.content, "html.parser")
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_="tombstone-container")
print(items)

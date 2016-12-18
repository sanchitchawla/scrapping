import requests
from bs4 import BeautifulSoup
import pandas as pd 

page = requests.get(
	"http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
	)

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")

"""
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

#print tonight.prettify()

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
#temp = tonight.find(class_="temp").get_text() website has changed I think

print period
print short_desc
#print temp 

img = tonight.find("img")
desc = img['title']

print desc
"""


period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(
	".tombstone-container .short-desc"
	)]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#print len(periods), len(short_descs), len(temps), len(descs)
temps.append('High: 57 \xb0F') # to debug the error where len(temps) was 8 

weather = pd.DataFrame({
	"period":periods,
	"short-desc": short_descs,
	"temp": temps,
	"desc": descs
	})

print weather

#Getting just the temperature 
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
#print temp_nums

print weather['temp_num'].mean()

#Using the lower temperatures to find the night temperature 
is_night = weather['temp'].str.contains("Low")
weather['is_night'] = is_night

print weather[is_night]
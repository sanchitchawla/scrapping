import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')

# To find all the instances with class "outer-text"

outer_text_all = soup.find_all('p',class_= 'outer-text')

print outer_text_all
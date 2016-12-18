import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")


soup = BeautifulSoup(page.content, 'html.parser')

#print soup.prettify()
test = [type(item) for item in list(soup.children)]

html = list(soup.children)[2]

body = list(html.children)[3]

p = list(body.children)[1]

print p.get_text()

# Or you could do this

p = soup.find_all('p')
print p[0].get_text() 

# If you only want the first instance of a tag then 

p = soup.find('p')

# is enough 


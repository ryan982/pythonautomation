import requests
from bs4 import BeautifulSoup
import xlsxwriter



url = "http://ddnews.gov.in/national"
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content, 'html.parser')
headlines = soup.find_all('span', attrs={"class" : "field-content"})
links = []
texts = []
#collection of links and texts

i = 0
while i < len(headlines):
   for a_tag in headlines:
        a_tag = headlines[i].find('a')
        link = a_tag.get('href')
        links.append("http://ddnews.gov.in"+link)
        text = a_tag.get_text()
        texts.append(text)
        i=i+1

#create workbook and worksheet
outworkbook = xlsxwriter.Workbook("headlines.xlsx")
outsheet = outworkbook.add_worksheet()

#headers
outsheet.write("A1", "NEWS")
outsheet.write("B1", "Link")
j = 0

for j in range (0, len(links)):
        outsheet.write(j+1, 0, texts[j])
        outsheet.write(j+1, 1, links[j])

outworkbook.close()
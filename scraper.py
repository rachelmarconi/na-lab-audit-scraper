import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) 
html = response.content 
print(response.reason)

soup = BeautifulSoup(html, features="html.parser")
#print(soup.prettify())

table = soup.find('tbody')
print(table.find_all('th'))

rows_list = []
for row in table.find_all('tr'):
	cell_list = []
	for cell in row.find_all('td'):
		cell_list.append(cell.text.strip())
		if cell.find('a'):
			cell_list.append("https://www.ola.state.md.us" + cell.find('a')['href'])
			#for link in cell.find_all('a'):
				#cell_list.append(link['href'])
	rows_list.append(cell_list)
print(rows_list[0])

outfile = open("./scraped_audit_reports.csv","w",newline="")
writer = csv.writer(outfile)
writer.writerow(["date", "type", "title", "url"])
writer.writerows(rows_list)
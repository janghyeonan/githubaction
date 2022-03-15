import requests
import datetime
from bs4 import BeautifulSoup
response = requests.get("https://www.clien.net/service/board/park")
soup = BeautifulSoup(response.text, 'html.parser')
print(datetime.datetime.now())
for j, k in zip([i.get_text().replace('\t',"").replace('\n',"") for i in soup.select('.subject_fixed')], [a.get_text().replace('\t',"").replace('\n',"") for a in soup.select('.timestamp')]):
    print(k, j)

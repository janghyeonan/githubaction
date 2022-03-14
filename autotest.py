import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.clien.net/service/board/park")
soup = BeautifulSoup(response.text, 'html.parser')
for j in [ i.get_text().replace('\t',"").replace('\n',"") for i in soup.select('.subject_fixed') ]:
    print(j)

import requests 
from bs4 import BeautifulSoup

#1 Step 1:

URL = "https://www2.assemblee-nationale.fr/deputes/liste/tableau"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
all_href = [tag['href'] for tag in soup.select('td a[href]')]
all_links = ["https://www2.assemblee-nationale.fr" + end_url for end_url in all_href]
print(all_links)


#2 Step 2: 

# result = []
# for link in all_links:
#     fiche = requests.get(link)
#     soup_fiche = BeautifulSoup(fiche.text, "html.parser")
#     name = soup_fiche.find("h1").text
#     email = soup_fiche.select_one('li:-soup-contains("Mél :")').text.replace("Mél : ", "")
#     name_email = name + " : " + email
#     result += [name_email]
# print(result)


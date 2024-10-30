import requests
from bs4 import BeautifulSoup

url = "https://www.radiofrance.fr/vie-quotidienne/cuisine/recettes"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

medias = soup.find_all("div", class_="CardMedia")

for m in medias:
    fl = m.find("a", class_="CardText")

    if fl.text == "Recettes de cuisine":
        title = m.find("div", class_="CardTitle")
        description = m.find("div", class_="CardDescription")
        link = m.find("a", class_="expandToParent", href=True)
    
        print(title.text.strip())
        print(description.text)
        print(fl.text)
        print(f"https://www.radiofrance.fr{link.get("href")}")
        print("-" * 30)
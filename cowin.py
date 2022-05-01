import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=india+covid+vaccination+status&oq=india+covid+vaccination+status&aqs=chrome" \
      "..69i57j0i22i30j0i390l2.16656j0j7&sourceid=chrome&ie=UTF-8#wptab=s" \
      ":H4sIAAAAAAAAAOMwe8TYxsgt8PLHPWGp2klrTl5jLOcS9E1NyUxOzAkuSSzJLC7JTC4WSuLigQp6FheXpgoFCQVwiYFFMvNSXTKLUxOLU8MSk0E8IRkudqiIkKAUPxevfrq-oWGWUXJyfGFOjpAEF4dPfjLQ4Pw8IR4pLi4O_Vx9A-OibAOeRawqyflF-XmJZZlFpcUKZRDjFDLzUjITFYrhbgEAilxUwbMAAAA "
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

noofdoses = soup.find(class_="rFcZAd").get_text()

print(noofdoses)

import requests
from bs4 import BeautifulSoup
import lxml.html
import smtplib
import os


MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']
URL = "https://petslike.net/trek-shcho-svititsia-z-m-iachikom-dlia-kotiv"

headers = {
    "Accept-Language": "uk,uk-UA;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6,ru-UA;q=0.5,ru;q=0.4,pl-PL;q=0.3,"
                       "pl;q=0.2",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.114 Safari/537.36",
}

response = requests.get(URL,
    headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price = (soup.find(name="div", class_="product__price--current")).text
price = price.split()[0]
price = float(price.replace(",", "."))


if price < 500:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="babichvladyslava@gmail.com",
            msg=f"Subject:Petslike Price Alert!\n\nTrack glowing with a ball for cats now UAH{price}\nHurry to buy\n{URL}"
        )

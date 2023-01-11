import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
MY_EMAIL = "YOUR MAIL"
MY_PASSWORD = "GET YOUR PASSWORD AT https://myaccount.google.com/u/2/apppasswords, THIS IS NOT YOUR MAIL PASSWORD"
URL = "THE LINK OF PRODUCT THAT YOU WANT TO TRACK"
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
response = requests.get(url=URL,headers=HEADERS)
website_response = response.text
soup = BeautifulSoup(website_response,"lxml")
website = soup.find_all(name="span",class_="a-price-whole")


price = website[0]
final_price = float(price.getText())
print(final_price)
MY_DESIRED_PRICE = 730.0


if final_price <= MY_DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Hi!\n\n OMG the price dropped to only {final_price}!! "
        )


import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.amazon.com/CanaKit-Raspberry-Starter-Kit-PRO/dp/B0CRSNCJ6Y/ref=sr_1_1?crid=1XR6FAJCAOYLL&dib=eyJ2IjoiMSJ9.TzIAlcap-JN7BzO8wHpHCV1kBEl4EFbvGKEftHseQ--2-6THr0K_AeFJrbC3iDT7YpbAewog2dwqqMvgjDqySA753TTGpDohOhjak6KODQQ2_pG4losfIgl10aeTvSvcCGk-MZKmnJvWaWuSsKLXYx5EV9-4b7HXouHrZur4EpGTiADJX5H_SIzmINoon3IGLV1naMO19U3yqd2AvPbkk9C2qqlHCtqbfSU4KGx-y0E.bYp0WogKeTVtAnW25X42lG3-Ib-hMdDev92fDXZCoDE&dib_tag=se&keywords=raspberry%2Bpi%2B5&qid=1726756996&sprefix=ras%2Caps%2C283&sr=8-1&th=1"
sender = '20981a4248@raghuenggcollege.in'
password = 'hkqakqpmwbfjvgys'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
         "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
         "Dnt": "1",
        "Priority": "u=1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1"}



response=requests.get(url=URL,headers=headers)
html_code=response.text
print(html_code)

soup=BeautifulSoup(html_code,"html.parser")
price_line=soup.find(name="span",class_="a-offscreen")
price_ws=price_line.getText()
price_list=price_ws.split("$")
price=float(price_list[1])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)


message = f"{title} is on sale for {price}!"


BUY_PRICE = 170

if price<BUY_PRICE:
    msg = f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(sender, password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=sender,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
    )

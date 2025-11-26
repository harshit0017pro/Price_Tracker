import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
def fetch_html(url):
# Preparing  headers  
    headers = {
   # User agent is preferd for web scraping because without it the request  can be blocked by sites 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-IN,en;q=0.5',
    'referer': 'https://www.amazon.in/',
    'Connection': 'keep-alive'      
}

    # Making a request  
    # session is better to maintain cookies

    session = requests.Session()  # Create a session
    session.headers.update(headers) # Attach headers to session
    response = session.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return 'request blocked'
    
html = fetch_html('https://www.amazon.in/DualSense-Wireless-Controller-PlayStation-White/dp/B08GZ6QNTC/ref=sr_1_2?crid=3D7F8K1Y7PB6L&dib=eyJ2IjoiMSJ9.mlEXdBGseypru5gfvv3h9CvXg6q9VoIGm6K5oOlZL-MJZLPUP226iS8AaIMMjuDTI2paauNJEn_SbDOc7cudAGeR116nFFqTAx20q8z9dLJDOe1nniTknTaop6rq3rniLaZN_9lEAHhhdtSxbIf6V88Pkq90XHPQOhEExy6tHH8KewnMmPuR7h5CmCuRETafSB-O81QgZJvqF1QQOEkl59q0XaUeFBslAimXSQ4fEdI.3uQW7y2OCv1o64B0p6viBgpPsv1aqBJLQ0iC7X8uzSo&dib_tag=se&keywords=controller+ps5&qid=1763468001&sprefix=controller+ps%2Caps%2C464&sr=8-2')



if html != 'request blocked':
    soup = BeautifulSoup(html, 'html.parser') # Parses the html
   
    # Selecting the price span
    price_whole = soup.find("span", class_="a-price-whole")
    price_fraction = soup.find("span", class_="a-price-fraction")
    price_symbol = soup.find("span", class_="a-price-symbol")

    if price_whole and price_fraction and price_symbol:
        price = f"{price_symbol.text.strip()}{price_whole.text.strip()}.{price_fraction.text.strip()}"
        print("Price:", price)
    elif price_whole:
        print("Price (whole part only):", price_whole.text.strip())
    else:
        print("Price not found.")
else:
    print("Request blocked or failed.")

Link = 'https://amzn.in/d/eShKHUp'
file_exists = os.path.isfile('price_history.csv')

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('price_history.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    if not file_exists:  # Check if the file is empty
        writer.writerow(['Date', 'Price', 'Link'])
    writer.writerow([date, price, Link ])
    print("Saved to CSV!")

    
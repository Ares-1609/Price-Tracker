import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_price(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        if "amazon" in url:
            tag = soup.select_one("span.a-price-whole") or soup.select_one("span.a-offscreen")
        elif "flipkart" in url:
            tag = soup.select_one("div._30jeq3")
        else:
            return None

        if tag:
            return int(''.join(filter(str.isdigit, tag.text)))
        return None
    except:
        return None

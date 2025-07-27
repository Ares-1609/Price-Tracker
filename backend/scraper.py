import requests
from bs4 import BeautifulSoup
import re

def get_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title, price, image = None, None, None

        # Amazon
        if "amazon" in url:
            title_tag = soup.find("span", {"id": "productTitle"})
            price_tag = soup.find("span", {"class": "a-price-whole"}) or soup.find("span", {"class": "a-offscreen"})
            img_tag = soup.find("img", {"id": "landingImage"})

        # Flipkart
        elif "flipkart" in url:
            title_tag = soup.find("span", {"class": "B_NuCI"})
            price_tag = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
            img_tag = soup.find("img", {"class": "_396cs4"})

        else:
            return None

        # Extract title
        title = title_tag.get_text(strip=True) if title_tag else "Unknown Product"

        # Extract price
        if price_tag:
            price_text = price_tag.get_text(strip=True).replace(",", "").replace("₹", "")
            match = re.search(r"\d+", price_text)
            price = int(match.group()) if match else None

        # Extract image
        if img_tag and img_tag.has_attr("src"):
            image = img_tag["src"]

        if price:
            return {
                "title": title,
                "price": price,
                "image": image
            }

        return None

    except Exception as e:
        print("Scraper error:", e)
        return None
k
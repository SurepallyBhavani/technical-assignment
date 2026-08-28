import requests
from bs4 import BeautifulSoup
#search_term = input("Enter search term: ")

url = "https://mdcomputers.in/"

params = {
    "route": "product/search",
    "search": "hard drive"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

try:
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    print("Status:", response.status_code)
    print("Final URL:", response.url)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("\nFirst 1000 characters of response:\n")
    print(response.text[:1000])

except requests.RequestException as e:
    print("Request failed:", e)

soup = BeautifulSoup(response.text, "html.parser")

product_elements = soup.find_all("div", class_="product-grid-item")

product_list=[]

for product in product_elements:
    name = product.find("h3", class_="product-entities-title").get_text(strip=True)
    price = product.find("span", class_="ins").get_text(strip=True)

    item={
        "product_name":name,
        "price": price
    }
    product_list.append(item)

print(product_list)
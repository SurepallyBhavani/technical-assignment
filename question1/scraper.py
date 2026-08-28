import requests
from bs4 import BeautifulSoup


BASE_URL = "https://mdcomputers.in/"


def fetch_products(search_term):
    params = {
        "route": "product/search",
        "search": search_term
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/151.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as e:
        print("Request failed:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    product_elements = soup.find_all(
        "div",
        class_="product-grid-item"
    )

    product_list = []

    for product in product_elements:

        name_element = product.find(
            "h3",
            class_="product-entities-title"
        )

        price_element = product.find(
            "span",
            class_="ins"
        )

        if name_element and price_element:
            name = name_element.get_text(strip=True)
            price = price_element.get_text(strip=True)

            item = {
                "product_name": name,
                "price": price
            }

            product_list.append(item)
    print(product_elements[0].prettify())

    return product_list


def display_products(products):

    if not products:
        print("No products found.")
        return

    print()
    print(f"{'Product Name':<50} {'Selling Price':>15}")
    print("-" * 67)

    for product in products:
        print(
            f"{product['product_name']:<50} "
            f"{product['price']:>15}"
        )
        print("-"*67)

def main():

    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    products = fetch_products(search_term)

    display_products(products)

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


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

        original_price_element = product.find(
            "span",
            class_="del"
        )

        discount_element = product.find(
            "span",
            class_="onsale"
        )

        if name_element and price_element:

            item = {
                "product_name": name_element.get_text(strip=True),
                "price": price_element.get_text(strip=True),
                "original_price": (
                    original_price_element.get_text(strip=True)
                    if original_price_element
                    else "N/A"
                ),
                "discount": (
                    discount_element.get_text(strip=True)
                    if discount_element
                    else "N/A"
                )
            }

            product_list.append(item)

    return product_list


def display_products(products):

    if not products:
        print("No products found.")
        return

    table = [
        [
            product["product_name"],
            product["price"],
            product["original_price"],
            product["discount"]
        ]
        for product in products
    ]

    print("\nProducts found:\n")

    print(
        tabulate(
            table,
            headers=[
                "Product Name",
                "Selling Price",
                "Original Price",
                "Discount"
            ],
            tablefmt="grid"
        )
    )


def main():

    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    products = fetch_products(search_term)

    display_products(products)


if __name__ == "__main__":
    main()
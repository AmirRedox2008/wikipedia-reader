import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}


def fetch_page(topic: str) -> str:
    url = f"https://en.wikipedia.org/wiki/{quote(topic.replace(' ', '_'))}"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text


def print_page(html: str) -> None:
    soup = BeautifulSoup(html, "html.parser")

    caption = soup.find("div", class_="infobox-caption")
    if caption:
        print(caption.get_text(strip=True))

    table = soup.find("table")
    if table:
        for row in table.find_all("tr"):
            th, td = row.find("th"), row.find("td")
            if th and td:
                print(f"{th.get_text(strip=True)}: {td.get_text(separator=' ', strip=True)}")

    print("=" * 80)

    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            print(text)


def main() -> None:
    while True:
        topic = input("Search something (q to exit): ").strip()
        if topic.lower() == "q":
            break
        if not topic:
            continue
        try:
            print_page(fetch_page(topic))
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                print("Page not found ")
            else:
                print(f"HTTP error: {e}")
        except requests.RequestException as e:
            print(f"Network error: {e}")


if __name__ == "__main__":
    main()
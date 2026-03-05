import requests
from bs4 import BeautifulSoup
import csv
import json
import time

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

news_list = []

for title in titles:
    headline = title.text
    link = title.find("a")["href"]

    data = {
        "title": headline,
        "url": link
    }

    news_list.append(data)

    print("Title:", headline)
    print("Link:", link)
    print()

time.sleep(2)

# Save to JSON
with open("news.json", "w") as f:
    json.dump(news_list, f, indent=4)

# Save to CSV
with open("news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL"])

    for news in news_list:
        writer.writerow([news["title"], news["url"]])

print("Data saved to news.json and news.csv")
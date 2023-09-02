from bs4 import BeautifulSoup
# re standards for Regular Expression
import re

with open("scraping\index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

    with open("scraping\changed.html", "w") as file:
        file.write(str(doc))

from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/asus-geforce-rtx-4060-dual-rtx4060-o8g/p/N82E16814126665?Item=N82E16814126665"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
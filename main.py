import requests
from bs4 import BeautifulSoup

# headers = {
#     "Accept": "application/json",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Host": "www.httpbin.org",
#     "Referer": "https://www.httpbin.org/",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0",
#     "X-Amzn-Trace-Id": "Root=1-65537fc2-009ef4b9499de44f4a46c30e"
# }

# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0"}
# session = requests.Session()

# resp = session.get("https://www.wildberries.ru/services/besplatnaya-dostavka" , headers = headers)
# html_doc = resp.text

with open('WB.html') as f:
   soup1 = BeautifulSoup(f, "html.parser")

with open('YA.html') as f:
   soup2 = BeautifulSoup(f, "html.parser")

mydivs1 = soup1.find_all("span", {"class": "address-item__name-text"})
mydivs2 = soup2.find_all("a", {"class": "search-business-snippet-view__address"})

print(len(mydivs1))
print(len(mydivs2))

import pandas as pd

WB = []
for div in mydivs1:
	WB.append(str(div)[44:-14])

YA = []
for div in mydivs2:
	YA.append(str(div)[127:-4])

WB_data = {"adr": WB}
WB_frame = pd.DataFrame(data = WB_data)

YA_data = {"adr": YA}
YA_frame = pd.DataFrame(data = YA_data)

WB_frame.to_excel("/Users/romanvisotsky/Desktop/adr.xlsx")


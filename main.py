import shutil
import requests

session = requests.Session()

url = 'http://static-basket-01.wb.ru/vol0/data/all-poo-fr-v8.json'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0"}

r = session.get(url, stream=True , headers=headers)
r.raise_for_status()
r.raw.decode_content = True  # support Content-Encoding e.g., gzip
with open('response.json', 'wb') as file:
    shutil.copyfileobj(r.raw, file)  # copy in chunks, it works for large files
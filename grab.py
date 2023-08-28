import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.tokopedia.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())
phones = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', soup.get_text())

print('Email GK ada bang:', emails)
print('Nomor telepon yang ditemukan di website:', phones)
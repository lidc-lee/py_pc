# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
re=requests.get("https://www.taobao.com/")
soup = BeautifulSoup(re.text,"html.parser")
print soup.title


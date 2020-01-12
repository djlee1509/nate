from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

URL = input("Please enter the URL: ")

try:
  page = requests.get(URL, headers=headers)
except:
  print("Error while opening the URL")

words = page.text.replace('\n', ' ').split()

words = [word.lower() for word in words]

dictionary = dict()

for word in words:
  word = re.sub(r'[^a-z]', '', word)
  counter = words.count(word)
  dictionary[word] = counter

for k in dictionary:
  print("{}: {},".format(k, dictionary[k]))


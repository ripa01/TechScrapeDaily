from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests


url = "https://www.thedailystar.net/tech-startup"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

finalNews=""
for data in soup.find_all("div",class_="card-content",limit=10):
        news=data.a.string
        finalNews += '\u2022 ' +news+'\n'
print(finalNews)
    
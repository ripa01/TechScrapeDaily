from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():

        url = "https://www.thedailystar.net/tech-startup"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        finalNews=""
        for i, data in enumerate(soup.find_all("div", class_="card-content")):
                if 3 <= i < 11:  # This will include elements at indices 3 to 10 (8 elements in total)
                        news = data.p.string
                        finalNews += '\u2022 ' + news + '\n'

        return render_template("index.html", News=finalNews)

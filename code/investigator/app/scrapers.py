import requests
import lxml.html
import time
from app import db
from app.models import Backpage
from datetime import datetime

def scrape_backpage():
    while True:
        r = requests.get("http://newyork.backpage.com/FemaleEscorts/")
        html = lxml.html.fromstring(r.text)
        ads = html.xpath("//div[contains(@class, 'cat')]/a/@href")
        bp = Backpage(datetime.now(),len(ads))
        db.session.add(bp)
        db.session.commit()
        time.sleep(360)
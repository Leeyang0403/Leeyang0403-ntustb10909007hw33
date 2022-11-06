from flask import Flask , render_template
import urllib.request as request
import json
#import requests
#import csv


app = Flask(__name__)

src="https://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/8ae4cabf6973990e0169947ed32454b9"
    #如果用open的方式最後還要close，如果沒close會佔記憶體空間
with request.urlopen(src) as response:
    data = json.load(response)

    #for station in data:
        #print(station["trnOpDate"])



@app.route('/')
def index():
    
    return render_template("bike_list.html", data = data)

if __name__ == '__main__':
    app.run()
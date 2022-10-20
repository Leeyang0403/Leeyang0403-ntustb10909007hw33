from flask import Flask , render_template
import urllib.request as request
import json


app = Flask(__name__)

src="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
with request.urlopen(src) as response:
    data = json.load(response)

    for station in data:
        print(station["ar"])
    # data = response.read().decode(encoding='utf-8')
#print(data)

@app.route('/')
def index():
    return render_template('bike_list.html', data = data)

if __name__ == '__main__':
    app.run()
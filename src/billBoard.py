from flask import Flask, jsonify, Response
import requests
import json
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route("/testBillboard")
def hello():
    return "Billboard app running"


@app.route("/billboard100", methods=['POST'])
def get_top100():
    print("application is running")
    req = requests.get("https://www.billboard.com/charts/hot-100")
    soup = bs(req.content, "html.parser")

    rank = []
    song_container = soup.findAll('span', {'class': 'chart-element__rank__number'})
    for container in song_container:
        rank.append(str(container.text)+".")
    
    song = []
    song_container = soup.findAll('span', {'class': 'chart-element__information__song text--truncate color--primary'})
    for container in song_container:
        song.append(str(container.text))
    
    artist = []
    song_container = soup.findAll('span', {'class': 'chart-element__information__artist text--truncate color--secondary'})
    for container in song_container:
        artist.append("-"+str(container.text))
    
    zipped_list = list(zip(rank, song, artist))
    response = Response(json.dumps(zipped_list), mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080)

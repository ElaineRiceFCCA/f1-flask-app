#!/usr/bin/env python3
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    race = None
    season = ''
    round = ''

    if request.method == 'POST':
        season = request.form['season']
        round = request.form['round']
        url = f'https://ergast.com/api/f1/{season}/{round}/results.json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
            if races:
                race = races[0]

    return render_template('index.html', race=race, season=season, round=round)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)

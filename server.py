from flask import Flask, make_response
import requests

app = Flask(__name__)

@app.route("/quote")
def hello():
    r = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json')
    resp = make_response(r.text)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['content-type'] = 'application/json'
    return resp
    
                 

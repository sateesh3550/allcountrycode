#!/usr/bin/python
import json
import sys
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def defaultUrl():
    return "<h1> Project All Country codes </h1>"

@app.route("/diag")
def getApiStatus():
    url = 'https://www.travel-advisory.info/api'
    r = requests.post(url)
    #BELOW LINE OF CODE WILL SPECIFICALLY RETURN THE REPLY OBJECT IN JSON FROM HITTING THE API WHICH HAS STATUS OF THE RESPONSE OBJECT
    var = r.json()['api_status']['reply']
    str_conv = json.dumps(var)
    return str_conv
    #BELOW LINE OF CODE WILL RETURN ALL THERESPONSE WE RECIEVED FROM THE API CALL
    #return r.json()

@app.route("/health")
def healthcheck():
    return "status: running active"

@app.route("/convert")
def defaultUrl1():
    id = request.args.get('cc')
    url = 'https://www.travel-advisory.info/api'
    r = requests.post(url)
    data = r.json()
    concatenatedStr=''

    ## Get input parameters from cmd line argument
    #list = sys.argv
    list = id.split(' ')
    print(list)
    ## Handling with Try Catch to avoid code break when country code is not found
    for i in list:
        try:
            concatenatedStr+= i+' '+data['data'][i]['name']+'<br>'
        except KeyError:
            concatenatedStr+= i+' '+"Country Code Not Found in API JSON"+'<br>'
    #print(concatenatedStr)
    #returning all the country objects to UI
    return concatenatedStr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

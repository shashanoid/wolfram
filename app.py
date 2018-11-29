# -*- coding: utf-8 -*-
import json
import os
import sys
import requests


from flask import Flask, make_response, request
from flask import jsonify


class Handler:
    app = Flask(__name__)

    def __init__(self):
    	self.app_id = os.getenv('APP_ID')
    	return None

    def makeShortAnswer(self):
    	req = request.get_json()
    	query = req['query']
    	try:
    		units = req['units']
    	except Exception as e:
    		units = ""
    	
    	url = "http://api.wolframalpha.com/v1/result?appid={0}&i={1}%3f&units={2}".format(self.app_id, query, units)


    	response = requests.get(url)
    	return make_response(response.text)

if __name__ == '__main__':
    handler = Handler()
    handler.app.add_url_rule('/shortanswer', 'shortanswer', handler.makeShortAnswer , methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
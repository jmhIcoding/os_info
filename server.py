__author__ = 'jmh081701'
import  json
import requests
from flask import  Flask
from flask import jsonify
from flask import request
app=Flask(__name__)
@app.route("/post/osinfo",methods=["POST"])
def postinfo():
        if not request.json:
            return "Needed Json Request"
        try:
            req=requests.json
            with open("data","w") as fp:
                json.dump(req,fp)
        except :
            return "Needed correct Json Request "

@app.route("/",methods=["GET"])
def getinfo():
        try:
            with open("data","r") as fp:
                req=json.load(fp)
            return jsonify(req)
        except :
            return "No info."
app.run(host="0.0.0.0",port=801)
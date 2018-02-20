# -*- coding: utf-8 -*-
from services import SocialDataService
from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

# @app.route("/socialdata/date", methods=['GET'])
# def getSocialDataByStartAndEnd():
#     start = request.args.get('start')
#     end = request.args.get('end')
#     data = SocialDataService.getSocialDataByStartAndEnd(start, end)
#     socials = {}
#     socials['socials'] = data
#     return jsonify(socials)

@app.route("/", methods=['GET'])
def index():
    return "SocialDataService"

@app.route("/facebook/getPageDetail", methods=['GET'])
def facebookGetPageDetail():
    pageId = request.args.get('pageID')
    r = requests.get('203.154.59.55:6001/facebook/getPageDetail')
    return r.json()

@app.route("/facebook/getUserDetail", methods=['GET'])
def facebookGetUserDetail():
    userId = request.args.get('userID')
    r = requests.get('203.154.59.55:6001/facebook/getUserDetail?userID=' + userId)
    return r.json()

@app.route("/facebook/getFeedByPageID", methods=['GET'])
def facebookGetFeedByPageID():
    pageId = request.args.get('pageID')
    since = request.args.get('since')
    until = request.args.get('until')
    r = requests.get('203.154.59.55:6001/facebook/getFeedByPageID?pageID='+pageId+'&since='+ since+'$until='+until)
    return r.json()

@app.route("/facebook/getCommentByPostID", methods=['GET'])
def facebookGetCommentByPostID():
    postId = request.args.get('postID')
    r = requests.get('203.154.59.55:6001/facebook/getCommentByPostID?postID='+postId)
    return r.json()

@app.route("/twitter/getLastestTweets", methods=['GET']) 
def getLatestTweets():     
    result = {}     
    result = SocialDataService.getLastestTweets()     
    return jsonify(result)

@app.route("/twitter/getLastestTweetByLocation", methods=['GET']) 
def getLastestTweetByLocation():     
    result = {}     
    result = SocialDataService.getLastestTweetByLocation(request.args.get('name'))     
    return jsonify(result)

@app.route("/crowdflow/getLocations", methods=['GET'])
def crowdflowGetLocations():
    postId = request.args.get('postID')
    r = requests.get('203.154.59.55:5050/facebook/getCommentByPostID?postID='+postId)
    return r.json()

@app.route("/crowdflow/density/random", methods=['GET'])
def crowdflowGetRandom():
    r = requests.get('203.154.59.55:5050/crowdflow/random')
    return r.json()

@app.route("/sentimental/getAllLocations", methods=['GET']) 
def sentimentalGetAllLocations():     
    r = requests.get('203.154.59.55:5005/getAllLocations')
    return r.json()

@app.route("/sentimental/predicted", methods=['GET'])
def sentimentalGet_predicted():
    r = requests.get('203.154.59.55:5005/predicted')
    return r.json()

@app.route("/environment/getThingStations")
def getThingStations():
    #assert section == request.view_args['section']
    data = SocialDataService.getThingStations()
    result = {}
    result['data'] = data
    return jsonify(result)

@app.route("/environment/<thing_id>")
def getTelemetryByThingId(thing_id):
    #thing_id = request.view_args['thing_id']
    data = SocialDataService.getTelemetryByThingId()
    result = {}
    result['data'] = data
    return jsonify(result)

@app.route("/mobility/getTaxiRaw")
def getTaxiData():
    #thing_id = request.view_args['thing_id']
    data = SocialDataService.getTaxiData()
    result = {}
    result = data
    return jsonify(result)

@app.route("/mobility/getTaxiCurrentGps")
def getTaxiCurrentGps():
    r = requests.get('http://203.154.59.55:10010/getTaxiCurrentGps')
    return r.json()

@app.route("/mobility/getTaxiDensity")
def getTaxiDensity():
    #thing_id = request.view_args['thing_id']
    data = SocialDataService.getTaxiDensity()
    result = {}
    result = data
    return jsonify(result)

#---------------------------------------------------------------------------------------------------
#-------------------------SERVICE DEPENDENCIES------------------------------------------------------
#---------------------------------------------------------------------------------------------------
@app.route("/socialdata/date", methods=['GET'])
def getSocialDataByStartAndEnd():
    start = request.args.get('start')
    end = request.args.get('end')
    data = SocialDataService.getSocialDataByStartAndEnd(start, end)
    socials = {}
    socials['socials'] = data
    return jsonify(socials)

@app.route("/socialdata", methods=['GET'])
def getAllSocialData():
    data = SocialDataService.getAllSocialData()
    socials = {}
    socials['socials'] = data
    return jsonify(socials)

@app.route("/query", methods=['GET'])
def getAllQuery():
    data = SocialDataService.getAllQuery()
    queries = {}
    queries['queries'] = data
    return jsonify(queries)

@app.route("/place", methods=['GET'])
def getPlaceById():
    place_id = request.args.get('place_id')
    place = {}
    place['place'] = SocialDataService.getPlaceById(place_id)
    return jsonify(place)

@app.route("/getAllLocations", methods=['GET']) 
def getAllLocations():     
    place = {}     
    place['place'] = SocialDataService.getAllLocations()     
    return jsonify(place)

@app.route("/predicted", methods=['GET'])
def get_predicted():
    predicted = {}
    predicted['predicted'] = SocialDataService.get_predicted();
    return jsonify(predicted) 

@app.route("/predicted/save", methods=['POST'])
def save_predicted():
    predicted = json.loads(request.get_data())
    result = SocialDataService.save_predicted(predicted)
    if result == None:
        return  ('', 500)
    else:
        return ('', 204)

@app.route("/tweet/date", methods=['GET'])
def getTweetDataByStartAndEnd():
    start = request.args.get('start')
    end = request.args.get('end')
    data = SocialDataService.getTweetDataByStartAndEnd(start, end)
    tweet = {}
    tweet['tweets'] = data
    return jsonify(tweet)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005, threaded=True)

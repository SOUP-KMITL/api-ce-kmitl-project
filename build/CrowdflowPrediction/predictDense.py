import datetime
import PredictionService
import CheckinData

print(datetime.datetime.now())
allPlace = PredictionService.allPlace()['places']
for place in allPlace:
    latlng = repr(place['lat'])+","+repr(place['lng'])
    # print(latlng)
    den = PredictionService.getNextDensity(latlng)
    # print(den)
    predict = den['density'][0] 
    # jsonPredict = json.dumps(predict)   
    CheckinData.savePredictCheckin(predict)
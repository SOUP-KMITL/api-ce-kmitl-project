# from pymongo import MongoClient
# import CheckinData
# import PredictionService
import findMax
# import FlowPrediction

# client = MongoClient("10.0.1.3")
# db = client.SocialData
# fqDb = db.FQ_CHECKIN

# allCheckin = fqDb.find({"venueId":"4b0587fdf964a52034ab22e3"}).limit(20000)
# checkinJSON = CheckinData.getCheckinByPlace("4b0587fdf964a52034ab22e3",15)
# max = CheckinData.findMaxOfPlace("4b0587fdf964a52034ab22e3")
# print(["-"]*CheckinData.timeToRound('00:00'))
# print(checkinJSO
# now = PredictionService.getCurrentDensity("13.746102858783594,100.53440439922444")
# print(now)

# allPredict = CheckinData.getCurrentPredictByPlace(13.746102858783594,100.53440439922444)
# allPredict = LocationDistance.findPlaceInRadius(13.746102858783594,100.53440439922444,0.5)

# allPredict = CheckinData.findInRadiusVenue(bound[0],bound[1],bound[2],bound[3])

# for predict in allPredict.sort("date",1):
    # print(predict)
# print(allPredict)
# print(CheckinData.findCurrentDateTimeRange())
# print(CheckinData.getCurrentCheckinByPlace("4b0587fdf964a52034ab22e3"))
# CheckinData.getCurrentCheckinByPlace("4b0587fdf964a52034ab22e3")

# print(datetime.datetime.now().)

# print(FlowPrediction.getFlowPrediction(None))
# place =  {
#       "lat": 13.746218236940342, 
#       "lng": 100.53291019710277, 
#       "name": "Siam Center (\u0e2a\u0e22\u0e32\u0e21\u0e40\u0e0b\u0e47\u0e19\u0e40\u0e15\u0e2d\u0e23\u0e4c)"
#     }
# place = []
# place = [
#         {
#         "lat": 13.746218236940342, 
#         "lng": 100.53291019710277, 
#         "name": "Siam Center (\u0e2a\u0e22\u0e32\u0e21\u0e40\u0e0b\u0e47\u0e19\u0e40\u0e15\u0e2d\u0e23\u0e4c)"
#         }, 
#         {
#         "lat": 13.746497917923502, 
#         "lng": 100.53154785754697, 
#         "name": "Siam Discovery (\u0e2a\u0e22\u0e32\u0e21\u0e14\u0e34\u0e2a\u0e04\u0e31\u0e1f\u0e40\u0e27\u0e2d\u0e23\u0e35\u0e48)"
#         }, 
#         {
#         "lat": 13.74497311302548, 
#         "lng": 100.53022399050144, 
#         "name": "MBK Center (\u0e40\u0e2d\u0e47\u0e21 \u0e1a\u0e35 \u0e40\u0e04 \u0e40\u0e0b\u0e47\u0e19\u0e40\u0e15\u0e2d\u0e23\u0e4c)"
#         }, 
#         {
#         "lat": 13.692592864395428, 
#         "lng": 100.7517546755635, 
#         "name": "Suvarnabhumi Airport (BKK) (\u0e17\u0e48\u0e32\u0e2d\u0e32\u0e01\u0e32\u0e28\u0e22\u0e32\u0e19\u0e2a\u0e38\u0e27\u0e23\u0e23\u0e13\u0e20\u0e39\u0e21\u0e34)"
#         }, 
#         {
#         "lat": 13.694094212667782, 
#         "lng": 100.64799621619503, 
#         "name": "Seacon Square (\u0e0b\u0e35\u0e04\u0e2d\u0e19\u0e2a\u0e41\u0e04\u0e27\u0e23\u0e4c)"
#         }, 
#         {
#         "lat": 13.746825434811983, 
#         "lng": 100.53967275442842, 
#         "name": "CentralWorld (\u0e40\u0e0b\u0e47\u0e19\u0e17\u0e23\u0e31\u0e25\u0e40\u0e27\u0e34\u0e25\u0e14\u0e4c)"
#         }, 
#         {
#         "lat": 13.721107657779335, 
#         "lng": 100.77889370469212, 
#         "name": "Suvarnabhumi Plaza Market (\u0e15\u0e25\u0e32\u0e14\u0e19\u0e31\u0e14\u0e2a\u0e38\u0e27\u0e23\u0e23\u0e13\u0e20\u0e39\u0e21\u0e34)"
#         }, 
#         {
#         "lat": 13.727425722923163, 
#         "lng": 100.77803447578444, 
#         "name": "King Mongkut's Institute of Technology Ladkrabang (KMITL) (\u0e2a\u0e16\u0e32\u0e1a\u0e31\u0e19\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e1e\u0e23\u0e30\u0e08\u0e2d\u0e21\u0e40\u0e01\u0e25\u0e49\u0e32\u0e40\u0e08\u0e49\u0e32\u0e04\u0e38\u0e13\u0e17\u0e2b\u0e32\u0e23\u0e25\u0e32\u0e14\u0e01\u0e23\u0e30\u0e1a\u0e31\u0e07)"
#         }, 
#         {
#         "lat": 13.766502526037955, 
#         "lng": 100.64238068411997, 
#         "name": "The Mall Bangkapi (\u0e40\u0e14\u0e2d\u0e30\u0e21\u0e2d\u0e25\u0e25\u0e4c \u0e1a\u0e32\u0e07\u0e01\u0e30\u0e1b\u0e34)"
#         }, 
#         {
#         "lat": 13.74601377826572, 
#         "lng": 100.53440439922444, 
#         "name": "Siam Paragon (\u0e2a\u0e22\u0e32\u0e21\u0e1e\u0e32\u0e23\u0e32\u0e01\u0e2d\u0e19)"
#         }, 
#         {
#         "lat": 13.746599361537822, 
#         "lng": 100.52886169082879, 
#         "name": "BTS National Stadium (W1) (BTS \u0e2a\u0e19\u0e32\u0e21\u0e01\u0e35\u0e2c\u0e32\u0e41\u0e2b\u0e48\u0e07\u0e0a\u0e32\u0e15\u0e34)"
#         }, 
#         {
#         "lat": 13.745718697678194, 
#         "lng": 100.53425607660282, 
#         "name": "BTS Siam (CEN) (BTS \u0e2a\u0e22\u0e32\u0e21)"
#         }
#     ]
# for p in place:
#     print("-----")
#     print(p['name'])
#     for np in LocationDistance.findPlaceInRadius(p['lat'],p['lng'],1.2):
#         print("-"+np['name'])
# print(place)


findMax.getMaxByPlaceAll("4b0587fdf964a52034ab22e3")

from pymongo import MongoClient
from config import dbName
import datetime

client = MongoClient(dbName)

db = client.SocialData

def getMaxByPlaceAll(venueid):

    allCheckin = db.FQ_CHECKIN.find({"venueId":venueid}).sort("_id",1)
    startDate = datetime.datetime.now()
    for checkin in allCheckin:
        startDate = datetime.datetime.strptime(checkin['datetime'],"%a %b %d %Y %H:%M:%S GMT+0700 (%Z)").replace(hour=0, minute=0, second=0, microsecond=0)
        break
    #  = todayDate-datetime.timedelta(days=days-1)
    print(startDate)


    # max = {}
    # #pick data from 'days' before today
    # for checkin in allCheckin:
    #     thisDate = datetime.datetime.strptime(checkin['datetime'],"%a %b %d %Y %H:%M:%S GMT+0700 (%Z)")
    #     # print(thisDate)
    #     if thisDate >= startDate:
    #         # print(thisDate)
    #         thisDateStr = thisDate.strftime("%Y-%m-%d")
    #         round = timeToRound(thisDate.strftime("%H:%M"))-1
            
    #         # print(round)
    #         # if thisDate>=todayDate:
    #         #     if(round>20):
    #         #         print(thisDate.strftime("%H:%M"))
    #             # print(round)
    #         if thisDateStr not in inDaysCheckin:
    #             if thisDate < todayDate:
    #                 inDaysCheckin[thisDateStr] = ["-"]*288
    #                 inDaysCheckin[thisDateStr][round] = checkin['count']
    #             else:
    #                 # currentTime = datetime.datetime.now().strftime("%H:%M")
    #                 # inDaysCheckin[thisDateStr] = ["-"]*timeToRound(currentTime)   
    #                 # print(timeToRound(datetime.datetime.now().strftime("%H:%M")))
    #                 inDaysCheckin[thisDateStr] = ["-"]*(timeToRound(datetime.datetime.now().strftime("%H:%M"))-1)     
    #                 inDaysCheckin[thisDateStr].insert(round,checkin['count'])
    #         else:
    #             try:
    #                 oldCount = inDaysCheckin[thisDateStr][round]
    #                 if oldCount == "-":
    #                     inDaysCheckin[thisDateStr][round] = checkin['count']
    #                 else:
    #                     inDaysCheckin[thisDateStr][round] = (oldCount+checkin['count'])/2    
    #             except IndexError:
    #                 inDaysCheckin[thisDateStr].insert(round,checkin['count'])  
    # # for day in inDaysCheckin:
    # #     print(len(inDaysCheckin[day]))
    # countCheckin = {}
    # countCheckin['checkin'] = []
    # for date,dense in inDaysCheckin.items():    
    #     oneDay = {}
    #     oneDay['date'] = date
    #     oneDay['dense'] = dense
    #     countCheckin['checkin'].append(oneDay)
    # return countCheckin
    


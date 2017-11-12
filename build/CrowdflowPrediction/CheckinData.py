from pymongo import MongoClient
import datetime
import DenseTableFqCheckin

client = MongoClient("127.0.0.1")
db = client.SocialData
fqDb = db.FQ_CHECKIN
db2 = client.Predict

def timeToRound(timeStr):
    #time format HH:MM
    time = timeStr.split(":")
    secs = ((int(time[0])*60+int(time[1]))/5)+1
    return secs

def findNextDateTime():
    dateNow = datetime.datetime.now()
    round = timeToRound(dateNow.strftime("%H:%M"))
    dateNext = None
    if round+1>288:
        round=1
        dateNext = dateNow+ datetime.timedelta(days=1)
    else:
        round+=1 
        dateNext = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)   
    len = (round-1)*5
    dateNext = dateNext + datetime.timedelta(minutes=len)
    return dateNext

def findCurrentDateTimeRange():
    rangeDatetime = []
    dateNow = datetime.datetime.now()
    # print(dateNow)
    round = timeToRound(dateNow.strftime("%H:%M")) 
    dateStart = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)   
    len = (round-1)*5
    dateStart = dateStart + datetime.timedelta(minutes=len)
    rangeDatetime.append(dateStart)
    rangeDatetime.append(dateStart + datetime.timedelta(minutes=4))
    return rangeDatetime

def findPreviousDateTimeRange():
    rangeDatetime = []
    dateNow = datetime.datetime.now()
    # print(dateNow)
    round = timeToRound(dateNow.strftime("%H:%M")) 
    dateStart = dateNow.replace(hour=0, minute=0, second=0, microsecond=0)   
    len = (round-2)*5
    dateStart = dateStart + datetime.timedelta(minutes=len)
    rangeDatetime.append(dateStart)
    rangeDatetime.append(dateStart + datetime.timedelta(minutes=4))
    return rangeDatetime

def getCheckinByPlace(venueid,days):

    todayDate = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    startDate = todayDate-datetime.timedelta(days=days-1)
    allCheckin = fqDb.find({"venueId":venueid}).sort("_id",-1).limit(20500)
    # print(startDate)
    inDaysCheckin = {}
    #pick data from 'days' before today
    for checkin in allCheckin:
        thisDate = datetime.datetime.strptime(checkin['datetime'],"%a %b %d %Y %H:%M:%S GMT+0700 (%Z)")
        # print(thisDate)
        if thisDate >= startDate:
            # print(thisDate)
            thisDateStr = thisDate.strftime("%Y-%m-%d")
            round = timeToRound(thisDate.strftime("%H:%M"))-1
            
            # print(round)
            # if thisDate>=todayDate:
            #     if(round>20):
            #         print(thisDate.strftime("%H:%M"))
                # print(round)
            if thisDateStr not in inDaysCheckin:
                if thisDate < todayDate:
                    inDaysCheckin[thisDateStr] = ["-"]*288
                    inDaysCheckin[thisDateStr][round] = checkin['count']
                else:
                    # currentTime = datetime.datetime.now().strftime("%H:%M")
                    # inDaysCheckin[thisDateStr] = ["-"]*timeToRound(currentTime)   
                    # print(timeToRound(datetime.datetime.now().strftime("%H:%M")))
                    inDaysCheckin[thisDateStr] = ["-"]*(timeToRound(datetime.datetime.now().strftime("%H:%M"))-1)     
                    inDaysCheckin[thisDateStr].insert(round,checkin['count'])
            else:
                try:
                    oldCount = inDaysCheckin[thisDateStr][round]
                    if oldCount == "-":
                        inDaysCheckin[thisDateStr][round] = checkin['count']
                    else:
                        inDaysCheckin[thisDateStr][round] = (oldCount+checkin['count'])/2    
                except IndexError:
                    inDaysCheckin[thisDateStr].insert(round,checkin['count'])  
    # for day in inDaysCheckin:
    #     print(len(inDaysCheckin[day]))
    countCheckin = {}
    countCheckin['checkin'] = []
    for date,dense in inDaysCheckin.items():    
        oneDay = {}
        oneDay['date'] = date
        oneDay['dense'] = dense
        countCheckin['checkin'].append(oneDay)
    return countCheckin

def findMaxOfPlace(venueid):
    allMax = fqDb.find({"venueId":venueid}).sort("count",-1).limit(50)
    avgMax = 0
    for max1 in allMax:
        avgMax = avgMax + max1['count']
    avgMax = avgMax/50
    print(avgMax)
    return avgMax

def findAllVenue():
    allVenue = db.FQ_VENUE.find()
    venuelist = []
    for venue in allVenue:
        newVenue = {}
        newVenue['venueId'] = venue['id']
        newVenue['name'] = venue['name']
        newVenue['lat'] = venue['location']['lat']
        newVenue['lng'] = venue['location']['lng']
        venuelist.append(newVenue)
    return venuelist

def findVenueByVenueID(venue_id):
    venue = db.place2.find_one({'venue_id':venue_id})
    if venue != None:
        newVenue = {}
        newVenue['venueId'] = venue['venue_id']
        newVenue['name'] = venue['name']
        coord = (venue['geolocation']).split(",")
        newVenue['lat'] = coord[0]
        newVenue['lng'] = coord[1]
        return newVenue
    return None

def findVenueByName(name):
    venue = db.FQ_VENUE.find_one({"name_id":name})
    if venue != None:
        newVenue = {}
        newVenue['venueId'] = venue['id']
        newVenue['name'] = venue['name']
        newVenue['lat'] = venue['location']['lat']
        newVenue['lng'] = venue['location']['lng']
        return newVenue
    return None

def findVenueByLl(lat,lng):
    venue = db.FQ_VENUE.find_one({"location.lat":lat})
    if venue != None:
        newVenue = {}
        newVenue['venueId'] = venue['id']
        newVenue['name'] = venue['name']
        newVenue['lat'] = venue['location']['lat']
        newVenue['lng'] = venue['location']['lng']
        return newVenue
    return None

def getCurrentCheckinByPlace(venueid):
    rangeDatetime = findCurrentDateTimeRange()
    allCheckin = fqDb.find({"venueId":venueid}).sort("_id",-1).limit(1000)
    inTimeCheckins = []
    for checkin in allCheckin:
        thisDate = datetime.datetime.strptime(checkin['datetime'],"%a %b %d %Y %H:%M:%S GMT+0700 (%Z)")
        if(thisDate>=rangeDatetime[0] and thisDate<=rangeDatetime[1]):     
            # print(checkin)
            inTimeCheckins.append(checkin)
    avgCheckin = {}
    for inTimeCheckin in inTimeCheckins:
        if not (avgCheckin):
            avgCheckin = inTimeCheckin
        else:
            avgCheckin['count']= (avgCheckin['count']+inTimeCheckin['count'])/2
    avgCheckin['date'] = rangeDatetime[0].strftime("%Y-%m-%d")
    avgCheckin['time'] = rangeDatetime[0].strftime("%H:%M")
    return avgCheckin

def getPreviousCheckinByPlace(venueid):
    rangeDatetime = findPreviousDateTimeRange()
    allCheckin = fqDb.find({"venueId":venueid}).sort("_id",-1).limit(1000)
    inTimeCheckins = []
    for checkin in allCheckin:
        thisDate = datetime.datetime.strptime(checkin['datetime'],"%a %b %d %Y %H:%M:%S GMT+0700 (%Z)")
        if(thisDate>=rangeDatetime[0] and thisDate<=rangeDatetime[1]):     
            # print(checkin)
            inTimeCheckins.append(checkin)
    avgCheckin = {}
    for inTimeCheckin in inTimeCheckins:
        if not (avgCheckin):
            avgCheckin = inTimeCheckin
        else:
            avgCheckin['count']= (avgCheckin['count']+inTimeCheckin['count'])/2
    return avgCheckin

def findInRadiusVenue(minLat,maxLat,minLng,maxLng):
    return db.FQ_VENUE.find({
        "location.lat": {"$gte": minLat,"$lte": maxLat},
        "location.lng": {"$gte": minLng,"$lte": maxLng}
        })    

#####predict table
def savePredictCheckin(predict):
    # print(predict)
    # print(db2.DENSE_FQCHECKIN.count())
    db2.DENSE_FQCHECKIN.insert_one(predict)

def findPredictByPlace(lat,lng):
    return db2.DENSE_FQCHECKIN.find({"place.lat":lat,"place.lng":lng})

def getCurrentPredictByPlace(lat,lng):
    dateNext = findNextDateTime()
    last = db2.DENSE_FQCHECKIN.find_one({"place.lat":lat,"place.lng":lng,"date":dateNext.strftime("%Y-%m-%d"),"time":dateNext.strftime("%H:%M")})
    # for l in last:
    return last
    # return None
    
def savePredictFlow(predict):
    # print(predict)
    # print(db2.DENSE_FQCHECKIN.count())
    db2.FLOW_FQCHECKIN.insert_one(predict)

from math import cos, asin, sqrt
import math
import csv

def findDistance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def getBoundFromLL(lat,lng,radiusInKm):
    # R = 6371000 # earth radius in m
    # radius = 50 # m
    # latMin = lng - math.degrees(radius/R/math.cos(math.radians(lat)))
    # latMax = lng + math.degrees(radius/R/math.cos(math.radians(lat)))
    # lngMax = lat + math.degrees(radius/R)
    # lngMin = lat - math.degrees(radius/R)
    kmInLongitudeDegree = 111.320 * math.cos( lat / 180.0 * math.pi)
    deltaLat = float(radiusInKm) / 111.1;
    deltaLong = float(radiusInKm) / kmInLongitudeDegree;
    minLat = lat - deltaLat;  
    maxLat = lat + deltaLat;
    minLng = lng - deltaLong; 
    maxLng = lng + deltaLong;
    return [minLat,maxLat,minLng,maxLng]
    
# lat =[]
# lng = []
# name =[]
# distance=[]
# with open('place.csv', encoding="UTF-8") as f:
#     reader = csv.reader(f)
#     next(reader, None) 
#     for row in reader:
#         name.append(row[0])
#         lat.append(float(row[1]))
#         lng.append(float(row[2]))

# for i in range(len(name)):
#     for j in range(i+1,len(name)):
#         dis = []
#         dis.append(name[i])
#         dis.append(name[j])
#         dis.append(findDistance(lat[i],lng[i],lat[j],lng[j]))
#         distance.append(dis)

# print(distance)
# with open('distance.csv', 'w', newline='') as fp:
#     a = csv.writer(fp, delimiter=',')
#     a.writerows([['place1','place2','distance(km)']])    
#     a.writerows(distance)



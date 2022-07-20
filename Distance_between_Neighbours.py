import pandas as pd
import math

def findCentroids():
    data = pd.read_csv("taxi_zones_lat_long.csv", usecols=["the_geom", "OBJECTID"])

    centroids = []
    objID = data['OBJECTID'].tolist()
    objID = [int(k) for k in objID]
    x = data['the_geom'].tolist()

    for i in range(len(data)):
        x[i] = x[i].replace("MULTIPOLYGON (((", "")
        x[i] = x[i].replace('(', '')
        x[i] = x[i].replace(')', '')
        x[i] = x[i].replace(',', '')
        x[i] = x[i].split(" ")

        x[i] = [float(k) for k in x[i]]

        count = 0
        lattitudes = []
        longitudes = []
        for y in x[i]:
            if (count % 2 == 0):
                lattitudes.append(y)
                count = count + 1
            elif (count % 2 != 0):
                longitudes.append(y)
                count = count + 1
        centroid = ["{}".format(objID[i]), (sum(lattitudes) / len(lattitudes)),
                    (sum(longitudes) / len(longitudes))]
        centroids.append(centroid)
    return centroids

def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
  R = 6371
  dLat = deg2rad(lat2-lat1)
  dLon = deg2rad(lon2-lon1)
  a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c
  return d

def deg2rad(deg):
    return deg * (math.pi/180)

def findDistancesBtwNeighbouringCentroids():
    data = pd.read_csv("C&N-MANHATTAN_updated.csv")
    objID = data['Region ID'].tolist()
    list = []
    distances = []
    centroids = findCentroids()
    for i in range(len(objID)):
        list.append(data["{}".format(objID[i])].tolist())

    for i in range(len(list)):
        for j in range(len(list)):
            if (list[i][j] == 1.0):
                c1 = [];
                c2 = [];
                for k in range(len(centroids)):
                    if (objID[i] == int(centroids[k][0])):
                        c1 = centroids[k]
                    if (objID[j] == int(centroids[k][0])):
                        c2 = centroids[k]
                dist = getDistanceFromLatLonInKm(float(c1[1]), float(c1[2]), float(c2[1]), float(c2[2]))
                distances.append(["{},{}".format(objID[i], objID[j]), dist])

    return distances

distances=findDistancesBtwNeighbouringCentroids()
print(distances)

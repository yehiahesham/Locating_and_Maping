import googlemaps
import json
from pprint import pprint



gmaps = googlemaps.Client(key='')
my_distance= gmaps.distance_matrix(
'New Cairo City,Cairo Governorate',
'Sheraton, Sheraton Al Matar, Qism El-Nozha, Cairo Governorate')
cool_variable = my_distance['rows'][0]['elements'][0]
dur= cool_variable['duration']['text']
dis=cool_variable['distance']['text']
print ("Distance is "+ dis)
print ("duration is "+ dur)


#jsonResponse=json.loads(my_distance)
#jsonData = jsonResponse["rows"]
#for item in jsonData:
#    dis = item.get("distance")
#    dur = item.get("duration")
#    print dis + dur

#result= json.loads(my_distance)
#print (result['rows'])
#print my_distance[u'rows'][0]
#with open('data.json', 'w') as outfile:
#    json.dump(my_distance, outfile)
#with open('data.json') as data_file:
#    data = json.load(data_file)

#print "Source is "
#pprint(data[u'origin_addresses'][0])
#print "Destination is "
#pprint(data[u'destination_addresses'][0] +data[u'destination_addresses'][0])

import googlemaps
import json
from pprint import pprint
import sys

mykey=''
gmaps = googlemaps.Client(key=mykey)

def yehia ():
    print 'hello'


def distance_matrix(source,distination):
    global gmaps
    my_distance=  gmaps.distance_matrix(distination,source)
    return my_distance['rows'][0]['elements'][0]['distance']['text'],my_distance['rows'][0]['elements'][0]['duration']['text']


def getadress(Latlng): #returns address
    global gmaps
    my_address=gmaps.reverse_geocode(Latlng)
    print my_address
    for data in my_address:
        print "\n ---------- address ---------- "
        for address in data['address_components']:
             sys.stdout.write(address['short_name']+' ')
    print "\n"

def PlaceDetails(Latlng):
    global gmaps
    my_place=gmaps.places(Latlng)
    print my_place


def getLatlng(addr): #returns Latlng
    global gmaps
    my_longlat= gmaps.geocode(addr)
    return  my_longlat[0]['geometry']['location']['lat'],my_longlat[0]['geometry']['location']['lng']


if __name__ == "__main__":
    source='30.019200, 31.502364'
    distination='29.988083, 31.441536'

#    dis,dur=distance_matrix(source,distination)
    lat,lng =getLatlng('Facebook HQ, Hacker Way, Menlo Park, CA, United States')
    x=str(lat)+','+str(lng)
    getadress(x)
    PlaceDetails(x)

#    print ("Distance is "+ dis)
#    print ("duration is "+ dur)
    print "Latlng is : %f ,%f " % (lat, lng)

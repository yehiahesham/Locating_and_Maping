import googlemaps
import json
from pprint import pprint
import sys
from datetime import datetime
import time


mykey=''
gmaps = googlemaps.Client(key=mykey)


def distance_matrix(source,distination,mode=None,departure_time=None,arrival_time=None): #returns distance and time (default mode is driving)
#departure_time/arrival_time =>int or datetime.datetime,
    global gmaps
    my_distance=  gmaps.distance_matrix(distination,source,mode,departure_time,arrival_time)
    return my_distance['rows'][0]['elements'][0]['distance']['text'],my_distance['rows'][0]['elements'][0]['duration']['text']


def getadress(Latlng): #returns address
    global gmaps
    my_address=gmaps.reverse_geocode(Latlng)
    return my_address[0]['formatted_address']


def getLatlng(addr): #returns Latlng
    global gmaps
    my_longlat= gmaps.geocode(addr)
    return  my_longlat[0]['geometry']['location']['lat'],my_longlat[0]['geometry']['location']['lng']

print distance_matrix('37.419356, -122.093706','37.421899, -122.084147',mode="bicycling",departure_time=datetime.now())
print getadress('37.419356, -122.093706')
print getLatlng(getadress('37.419356, -122.093706'))

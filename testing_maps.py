import googlemaps
from pprint import pprint
import sys
from datetime import datetime
import time



class Py_GOOGLE_MAPS_API:
    """docstring for Py_GOOGLE_MAPS_API"""
    def __init__(self, _mykey):
        self.mykey =_mykey
        self.gmaps = googlemaps.Client(key=self.mykey)

    def distance_matrix(self,source,distination,mode=None,departure_time=None,arrival_time=None):
        my_distance=  self.gmaps.distance_matrix(distination,source,mode,departure_time,arrival_time)
        return my_distance['rows'][0]['elements'][0]['distance']['text'],my_distance['rows'][0]['elements'][0]['duration']['text']


    def getadress(self,Latlng): #returns address
        my_address=self.gmaps.reverse_geocode(Latlng)
        return my_address[0]['formatted_address']


    def getLatlng(self,addr): #returns Latlng
        my_longlat= self.gmaps.geocode(addr)
        return  my_longlat[0]['geometry']['location']['lat'],my_longlat[0]['geometry']['location']['lng']

    def returnMe(self):
        return self


p= Py_GOOGLE_MAPS_API('PUT_YOUR_KEY_HERE')
print p.distance_matrix('37.419356, -122.093706','37.421899, -122.084147',mode="bicycling",departure_time=datetime.now())
print p.getadress('37.419356, -122.093706')
print p.getLatlng(p.getadress('37.419356, -122.093706'))
print p.returnMe()
import googlemaps
from pprint import pprint
import sys
from datetime import datetime
import time

"""
In general , Google Maps Web Services are avaliable for  Java, Python, Go, and Node.js Clients. check: https://developers.google.com/maps/web-services/client-library

Py_GOOGLE_MAPS_API is a wrapper Python Class for the Python Google API.

Dependencies :
    1)Install the googlemaps python pkg inorder for the code to execute
    you can find it in github: https://github.com/googlemaps/google-maps-services-python

    2)Get a Google Maps API key , you can find it here: https://developers.google.com/maps/documentation/javascript/get-api-key.

Offcourse you need Python , but that is implied :P

Unfortunately, the Only GOOD refrence I was able to find was the javascript GOOGLE API you can find it here:
https://developers.google.com/maps/documentation/javascript/reference
"""

class Py_GOOGLE_MAPS_API:
    def __init__(self, _mykey):
    """constructer for Py_GOOGLE_MAPS_API class
        :param _mykey: Maps API key.Required.
        :type key: string

        ***Other inputs that can be added to the class constructer and to the client constructer,
        I didn't see the need for them ,are:

        client_id, client_secret, =>  use "client_id" and "client_secret", unless the GOOGLE API KEY is set.
        timeout, connect_timeout, read_timeout, =>
        retry_timeout, requests_kwargs,
        queries_per_second, channel
    """
        self.mykey =_mykey
        self.gmaps = googlemaps.Client(key=self.mykey)



    def distance_matrix(self,source,distination,mode=None,departure_time=None,arrival_time=None):
    """ Gets travel distance and time for a matrix of origins and destinations.
    Required:
    :param source/destination: One location and/or latitude/longitude values,
        from/to which to calculate distance and time. If you pass an address as
        a string, the service will geocode the string and convert it to a
        latitude/longitude coordinate to calculate directions.
    Type=> each is a single location, where a location is a string.

    Optional:
    :param mode: Specifies the mode of transport to use when calculating directions. Valid values are "driving", "walking", "transit" or "bicycling".
    Type mode=> string
                    Note: you can't specify both departure_time and arrival_time.
    :param departure_time: Specifies the desired time of departure.
    Type=>int or datetime.datetime

    :param arrival_time: Specifies the desired time of arrival for transit
        directions.
    Type=>int or datetime.datetime

    Returns:
    :return type: returns two strings, Distance and Time

    ***Other inputs that can be added  and to the distance_matrix function,
    I didn't see the need for them ,are:
    language => The language in which to return results.Type=> string

    Avoid=> Indicates that the calculated route(s) should avoid indicated features. Valid values are "tolls", "highways" or "ferries". Type=>string.
    Units=> Specifies the unit system to use when displaying results.Valid values are "metric" or "imperial".Type=>string. defualt is KM
    Transit_mode=> Specifies one or more preferred modes of transit.
        This parameter may only be specified for requests where the mode is
        transit. Valid values are "bus", "subway", "train", "tram", "rail".
        "rail" is equivalent to ["train", "tram", "subway"].Type=> string or list of strings

    Transit_routing_preference=> Specifies preferences for transit requests. Valid values are "less_walking" or "fewer_transfers". Type=>string
    Traffic_model=> Specifies the predictive travel time model to use. Valid values are "best_guess" or "optimistic" or "pessimistic".
    The traffic_model parameter may only be specified for requests where the travel mode is driving, and where the request includes a departure_time containing one origin paired with each destination.
    """
        my_distance=self.gmaps.distance_matrix(distination,source,mode,departure_time,arrival_time)
        return my_distance['rows'][0]['elements'][0]['distance']['text'],my_distance['rows'][0]['elements'][0]['duration']['text']


    def getadress(self,Latlng): #returns address
    """
    getadress is the process of converting geographic coordinates Lat & lng into a
    human-readable address.

    :param latlng: The latitude/longitude value.Type=>  string, dict, list, or tuple
    :return type: single Reverse geocoding result, in a formatted address.


    ***Other inputs that can be added  and to the geocode function,
    I didn't see the need for them ,are:

    Result_type and Location_type => each are One or more address types to restrict results to. Type=>  string or list of strings
    language => The language in which to return results.Type=> string
    """
        my_address=self.gmaps.reverse_geocode(Latlng)
        return my_address[0]['formatted_address']



    def getLatlng(self,addr): #returns Latlng
    """
    Geocoding is the process of converting addresses like
    (``"1600 Amphitheatre Parkway, Mountain View, CA"``) into geographic
    coordinates like (latitude: 37.423021 and longitude: -122.083739), which you
    can use to place markers or position the map.

    :param addr: The address to geocode.Type=> string
    :return type:single  geocoding result.

    ***Other inputs that can be added to the class constructr and to the geocode function,
         I didn't see the need for them ,are:

    Components=> A component filter for which you wish to obtain a geocode. Type=>  dict
    Bounds=>    The bounding box of the viewport within which to bias geocode results more prominently.Type => string or dict with northeast and southwest points.
    Region=>    The region code, specified as a ccTLD ,two-character value.Type=> string
    language => The language in which to return results.Type=> string
    """
        my_longlat= self.gmaps.geocode(addr)
        return  my_longlat[0]['geometry']['location']['lat'],my_longlat[0]['geometry']['location']['lng']

    def returnMe(self):
    #Retruns a Copy of the constructed object, to have dupilcates if desired instead of constructing a new object
        return self

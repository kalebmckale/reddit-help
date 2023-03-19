import numpy as np

def matrix(x, y):
    return np.zeros([x, y], dtype=np.int)

def matrix2(x, y):
    return np.array([[0] * y] * x)\
    
    
"""
Is this .json a dict or a list of dict? And how do I get Pandas (or Pyspark) to read it?

Hello, I have a .json I need to do some cleaning with either Pandas or Pyspark. I have tried using pandas.read_json and messing around with the parameters to no avail (the error is: ValueError: arrays must all be same length). My Stackoverflow question: https://stackoverflow.com/questions/68448047/how-do-i-get-pandas-read-json-to-recognize-this-api-return-as-a-valid-json

Had a comment mentioning I need to construct a template; here is an example.

    import requests
    
    url = 'http://maps.googleapis.com/maps/api/directions/json'
    
    params = dict(
        origin='Chicago,IL',
        destination='Los+Angeles,CA',
        waypoints='Joplin,MO|Oklahoma+City,OK',
        sensor='false'
    )
    
    resp = requests.get(url=url, params=params)
    data = resp.json() # Check the JSON Response Content documentation below

1) What exactly is params = dict() doing? 

2) If I have to re-write every value pairing than what's the point? 

3) And how do I deal with "features:" being nested and having a lot of keys stuffed inside of it?

Here is the .json:

    {
       "type":"FeatureCollection",
       "query":[
          -73.989,
          40.733
       ],
       "features":[
          {
             "id":"address.5528394502635160",
             "type":"Feature",
             "place_type":[
                "address"
             ],
             "relevance":1,
             "properties":{
                "accuracy":"rooftop"
             },
             "text":"East 13th Street",
             "place_name":"120 East 13th Street, New York, New York 10003, United States",
             "center":[
                -73.98893045,
                40.73295105
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -73.98893045,
                   40.73295105
                ]
             },
             "address":"120",
             "context":[
                {
                   "id":"neighborhood.2103290",
                   "text":"Greenwich Village"
                },
                {
                   "id":"postcode.13482670360296810",
                   "text":"10003"
                },
                {
                   "id":"locality.12696928000137850",
                   "wikidata":"Q11299",
                   "text":"Manhattan"
                },
                {
                   "id":"place.2618194975964500",
                   "wikidata":"Q60",
                   "text":"New York"
                },
                {
                   "id":"district.12113562209855570",
                   "wikidata":"Q500416",
                   "text":"New York County"
                },
                {
                   "id":"region.17349986251855570",
                   "wikidata":"Q1384",
                   "short_code":"US-NY",
                   "text":"New York"
                },
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"neighborhood.2103290",
             "type":"Feature",
             "place_type":[
                "neighborhood"
             ],
             "relevance":1,
             "properties":{
                
             },
             "text":"Greenwich Village",
             "place_name":"Greenwich Village, New York, New York 10003, United States",
             "bbox":[
                -74.005282,
                40.72586,
                -73.98734,
                40.73907
             ],
             "center":[
                -74.0029,
                40.7284
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -74.0029,
                   40.7284
                ]
             },
             "context":[
                {
                   "id":"postcode.13482670360296810",
                   "text":"10003"
                },
                {
                   "id":"locality.12696928000137850",
                   "wikidata":"Q11299",
                   "text":"Manhattan"
                },
                {
                   "id":"place.2618194975964500",
                   "wikidata":"Q60",
                   "text":"New York"
                },
                {
                   "id":"district.12113562209855570",
                   "wikidata":"Q500416",
                   "text":"New York County"
                },
                {
                   "id":"region.17349986251855570",
                   "wikidata":"Q1384",
                   "short_code":"US-NY",
                   "text":"New York"
                },
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"postcode.13482670360296810",
             "type":"Feature",
             "place_type":[
                "postcode"
             ],
             "relevance":1,
             "properties":{
                
             },
             "text":"10003",
             "place_name":"New York, New York 10003, United States",
             "bbox":[
                -73.9996058238451,
                40.7229310019,
                -73.9798620096375,
                40.7396749960342
             ],
             "center":[
                -73.99,
                40.73
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -73.99,
                   40.73
                ]
             },
             "context":[
                {
                   "id":"locality.12696928000137850",
                   "wikidata":"Q11299",
                   "text":"Manhattan"
                },
                {
                   "id":"place.2618194975964500",
                   "wikidata":"Q60",
                   "text":"New York"
                },
                {
                   "id":"district.12113562209855570",
                   "wikidata":"Q500416",
                   "text":"New York County"
                },
                {
                   "id":"region.17349986251855570",
                   "wikidata":"Q1384",
                   "short_code":"US-NY",
                   "text":"New York"
                },
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"locality.12696928000137850",
             "type":"Feature",
             "place_type":[
                "locality"
             ],
             "relevance":1,
             "properties":{
                "wikidata":"Q11299"
             },
             "text":"Manhattan",
             "place_name":"Manhattan, New York, United States",
             "bbox":[
                -74.047313153061,
                40.679573,
                -73.907,
                40.8820749648427
             ],
             "center":[
                -73.9597,
                40.7903
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -73.9597,
                   40.7903
                ]
             },
             "context":[
                {
                   "id":"place.2618194975964500",
                   "wikidata":"Q60",
                   "text":"New York"
                },
                {
                   "id":"district.12113562209855570",
                   "wikidata":"Q500416",
                   "text":"New York County"
                },
                {
                   "id":"region.17349986251855570",
                   "wikidata":"Q1384",
                   "short_code":"US-NY",
                   "text":"New York"
                },
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"place.2618194975964500",
             "type":"Feature",
             "place_type":[
                "place"
             ],
             "relevance":1,
             "properties":{
                "wikidata":"Q60"
             },
             "text":"New York",
             "place_name":"New York, New York, United States",
             "bbox":[
                -74.25909,
                40.477399,
                -73.700272,
                40.917577
             ],
             "center":[
                -73.9866,
                40.7306
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -73.9866,
                   40.7306
                ]
             },
             "context":[
                {
                   "id":"district.12113562209855570",
                   "wikidata":"Q500416",
                   "text":"New York County"
                },
                {
                   "id":"region.17349986251855570",
                   "wikidata":"Q1384",
                   "short_code":"US-NY",
                   "text":"New York"
                },
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"district.12113562209855570",
             "type":"Feature",
             "place_type":[
                "district"
             ],
             "relevance":1,
             "properties":{
                "wikidata":"Q500416"
             },
             "text":"New York County",
             "place_name":"New York County, New York, United States",
             "bbox":[
                -74.047227,
                40.682932,
                -73.907,
                40.879278
             ],
             "center":[
                -74,
                40.7167
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -74,
                   40.7167
                ]
             },
             "context":[
                {
                   "id":"region.17349986251855570",
                   "wikidata":"Q1384",
                   "short_code":"US-NY",
                   "text":"New York"
                },
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"region.17349986251855570",
             "type":"Feature",
             "place_type":[
                "region"
             ],
             "relevance":1,
             "properties":{
                "wikidata":"Q1384",
                "short_code":"US-NY"
             },
             "text":"New York",
             "place_name":"New York, United States",
             "bbox":[
                -79.8578350999901,
                40.4771391062446,
                -71.7564918092633,
                45.0239286969073
             ],
             "center":[
                -75.4652471468304,
                42.751210955
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -75.4652471468304,
                   42.751210955
                ]
             },
             "context":[
                {
                   "id":"country.19678805456372290",
                   "wikidata":"Q30",
                   "short_code":"us",
                   "text":"United States"
                }
             ]
          },
          {
             "id":"country.19678805456372290",
             "type":"Feature",
             "place_type":[
                "country"
             ],
             "relevance":1,
             "properties":{
                "wikidata":"Q30",
                "short_code":"us"
             },
             "text":"United States",
             "place_name":"United States",
             "bbox":[
                -179.9,
                18.8163608007951,
                -66.8847646185949,
                71.4202919997506
             ],
             "center":[
                -97.9222112121185,
                39.3812661305678
             ],
             "geometry":{
                "type":"Point",
                "coordinates":[
                   -97.9222112121185,
                   39.3812661305678
                ]
             }
          }
       ],
       "attribution":"NOTICE: © 2021 Mapbox and its suppliers. All rights reserved. Use of this data is subject to the Mapbox Terms of Service (https://www.mapbox.com/about/maps/). This response and the information it contains may not be retained. POI(s) provided by Foursquare."
    }

I'm a little bit lost despite looking at the examples, appreciate any pointers or an alternative method.

"""
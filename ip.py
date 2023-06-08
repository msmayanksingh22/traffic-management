import re
import json
from urllib.request import urlopen

def ip_loc():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    city = data['city']
    country=data['country']
    region=data['region']

    print ('Country : {1} \nRegion : {0} \nCity : {2}'.format(region,country,city))

    return city


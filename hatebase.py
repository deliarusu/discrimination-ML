import requests
import json
import sys

# make request to hatebase, note the paging
try:
    # fill in API Key
    r = requests.get('http://api.hatebase.org/v3-0/xxx...x/vocabulary/json/a'
                     'bout_language%3D1%7Clanguage%3D1')
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

# read json request output
try:
    d = json.loads(r.text)
    data = d.get('data')
    print(data)
    datapoints = data.get('datapoint')
    for dpts in datapoints:
        print(dpts)
        print(dpts.get('language'), dpts.get('meaning'))

except ValueError as e:
    print(e)
    sys.exit(1)

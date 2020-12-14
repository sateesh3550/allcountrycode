#!/usr/bin/python
import json
import sys

with open('data.json') as f:
  data = json.load(f)

## Get input parameters from cmd line argument
list = sys.argv
## Handling with Try Catch to avoid code break when country code is not found
#try:
j = 0
    # iterating through cmd line argument input
for i in list:
    if j == 0:
        j = j+1;
    else:
        try:
            print(i+' '+data['data'][i]['name'])
        except KeyError:
            print(i+' '+"Country Code Not Found in API JSON")
#except KeyError:
#    print(i+' '+"Country Code Not Found in API JSON")

#print(sys.argv[0])
#print(data['data'][sys.argv[0]]['name'])

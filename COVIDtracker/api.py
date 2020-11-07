import json
import requests

def finder(state, district):
    req = requests.get("https://api.covid19india.org/state_district_wise.json")
    data = req.json()
    try:
        return {
        'ErrorCode' : 0,
        'state' : state,
        'district': district,
        'active': data[state]["districtData"][district]["active"],
        'confirmed': data[state]["districtData"][district]["confirmed"],
        'deceased' : data[state]["districtData"][district]["deceased"],
        'recovered': data[state]["districtData"][district]["recovered"]
        }
    except KeyError:
        return {
        'ErrorCode' : 1
        }
    except:
        return {
        'ErrorCode' : 2
        }

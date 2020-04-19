import requests
import json
from datetime import datetime

def pjson(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print()
pjson(response.json())

params = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=params)
print()
print(response.status_code)
print()
pjson(response.json())

pass_times = response.json()['response']
rise_times = []
for i in pass_times:
    rise_times.append(i['risetime'])
print()
print(rise_times)

# These times are difficult to understand – they are in a format known as timestamp or epoch.
# Essentially the time is measured in the number of seconds since January 1st 1970.
times = []
for rt in rise_times:
    times.append(datetime.fromtimestamp(rt))

print()
[print(i) for i in times]
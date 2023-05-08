import json
import time
from datetime import datetime

f=open('Tracking_Cabinets.json')
Cabinets_data=json.load(f)

Cabinets_list=Cabinets_data['cabinets']

print(Cabinets_list[0]['Stamp_time'])
print(str(datetime.now()))

initial_hour=Cabinets_list[0]['Stamp_time'][11:13]
print(int(initial_hour))
      

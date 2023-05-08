import json


with open('Tracking_Cabinets.json','r+') as fi:
    Cabinets_data=json.load(fi)
    Cabinets_data['cabinets'][0]['Current_place']="Mechanical assembly"
    fi.seek(0)
    json.dump(Cabinets_data,fi,indent=4)

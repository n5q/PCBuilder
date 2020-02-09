## DUMP DATA FROMPCPARTPICKER API INTO JSON FILE

from pcpartpicker import API
from json import loads
api = API()

parts = []

for i in parts:
    j = api.retrieve(i)
    j = j.to_json()
    with open(i + ".json", "w+") as file:
        file.write((j))

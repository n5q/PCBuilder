## DUMP DATA FROMPCPARTPICKER API INTO JSON FILE

from pcpartpicker import API
from json import loads
api = API()

# parts = ["cpu","memory","video-card"]

# for i in parts:
#     j = api.retrieve(i)
#     j = j.to_json()
#     with open(i + ".json", "w+") as file:
#         file.write((j))
j = api.retrieve_all()
j = j.to_json()
with open("all.json", "w+") as file:
    file.write((j))
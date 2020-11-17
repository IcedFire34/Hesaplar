# -*- coding: utf-8 -*-
import json

data = '{"adı" : "Ömer" ,"soyadı" : "bozkaya"}'

y=json.loads(data)
print(y["adı"])

müsteri = {
           "adı":"eslem",
           "soyadı":"öztürk"       
          }

müsterijson = json.dumps(müsteri)
print(müsteri)

print(json.dumps("omer"))
import json,logging
import requests
data=requests.get("https://jsonplaceholder.typicode.com/todos")
try:
    ExtractedData=data.json()
    li=[x for x in ExtractedData if x["completed"]==True]
    print(li)
except:
    logging.error("incorrect data")
finally:
    print("Thankyou")
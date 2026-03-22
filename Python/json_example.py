import json
# json.dumps convert python object to json string
obj ={"name": "Alice","company": "IBM" , "salary":5000}
s= json.dumps(obj)
print(s)

# json.loads convert json string to python object
d=json.loads(s)
print(d)
type(d)









file = open("data.json","w")
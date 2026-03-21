import json
obj ={"name": "Alice","company": "IBM" , "salary":5000}
s= json.dumps(obj)
# json.dumps convert python object to json string
print(s)
d=json.loads(s)
print(d)
# json.loads convert json string to python object
type(d)


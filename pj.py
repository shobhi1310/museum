import json

data = {}
data['people'] = []
data['people'].append({
    'name':'Scott',
    'website':'stackabuse.com',
    'from':'Nebraska'
})
data['people'].append({
    'name':'Larry Page',
    'website':'google.com',
    'from':'Michigan'
})

y = json.dumps(data,indent=4)
print(y)

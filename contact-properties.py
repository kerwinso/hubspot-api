import os, requests

hapikey = os.environ['HAPIKEY']
url = 'https://api.hubapi.com/properties/v1/contacts/properties?hapikey=' + hapikey

r = requests.get(url=url)
data = r.json()

with open('hubspot-contact-properties.tsv', 'w') as f:
    f.write("name\tdescription\n")
    for i in data:
        print(i['name'], i['description'])
        line = i['name'] + '\t' + i['description']
        f.write(line +"\n")

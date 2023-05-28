import json

with open('/Users/alex/Downloads/countries.json', 'r', encoding='utf-8') as f:
    country = json.load(f)
    # print(country)


for i in country:
    if 'a' in i['name']:
        print(i['name'])

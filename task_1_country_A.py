import json

with open('/Users/alex/Downloads/countries.json', 'r', encoding='utf-8') as f:
    country = json.load(f)
    # print(country)

count_1 = 0
for i in country:
    if 'a' in i['name'].lower():
        count_1 += 1
        print(i['name'])
print(count_1)

# count_2 = 0
# for city in country:
#     if city['name'].lower().find('a') != -1:
#         count_2 += 1
#         print(city['name'])

# print(count_2)

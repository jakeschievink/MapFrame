import pycountry, json

with open('./cities.json/cities.json') as f: 
    cities = json.load(f)

for city in cities:
    try:
        print("processing "+city['name'])
        city_cc = city['country']
        country_name = pycountry.countries.lookup(city_cc).name
        city['country_name'] = country_name
        city["country_code"] = city_cc
    except LookupError: 
        print("Couldn't Find" + city_cc)



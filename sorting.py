locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia'] = {'India':['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa']= {'Egypt':['Cairo']}
locations['Asia']['China']= ['Shanghai'] 

usa_cities = sorted(locations['North America']['USA'])
for city in usa_cities:
    print(city)

Asia_cities = []

for countries, cities in locations['Asia'].items():
    city_country = cities[0]+ " - " + countries
    Asia_cities.append(city_country)
asia_sorted = sorted(Asia_cities)
for city in asia_sorted:
    print(city)
from flask import Flask, request, render_template, jsonify
import glob, random, json, requests, pdb, sqlite3, datagrabber
app = Flask(__name__)

def get_random_city():
    json_cities = open('./citieslatlong.json').read()
    dict_cities = json.loads(json_cities)
    chosen_city = random.choice(dict_cities)
    return chosen_city

city_info=get_random_city()
dg = datagrabber.DataGrabber()

def k_to_f(k):
    return ((k - 273) * 1.8 ) + 32

def add_city(cities):
    conn = sqlite3.connect('./custom_cities.db')
    cur = conn.cursor()
    geoname_city=dg.get_geoname_data(cities[0])
    name = geoname_city['features'][0]['properties']['address']
    country = geoname_city['features'][0]['properties']['country']
    sub_country = geoname_city['features'][0]['properties']['state']
    population = geoname_city['features'][0]['properties']['population']
    country_code = geoname_city['features'][0]['properties']['country_code']
    description = geoname_city['features'][0]['properties']['description']
    lat = geoname_city['features'][0]['properties']['lat']
    lng = geoname_city['features'][0]['properties']['lng']

    sql_string ="INSERT INTO cities(name, country, sub_country, country_code, population, description, lat, lng) VALUES('"+name+"', '"+country+"', '"+sub_country+"', '"+country_code+"', '"+str(population)+"', '"+description+"', '"+lat+"', '"+lng+"')" 
    cur.execute(sql_string)
    conn.commit()
    conn.close()
    return cur.lastrowid

def get_city_list_from_database():
    conn = sqlite3.connect('./custom_cities.db')
    cur = conn.cursor()
    sql_string = "SELECT * FROM cities"
    cur.execute(sql_string)
    cities = cur.fetchall()
    conn.close()
    return cities

def get_random_city_from_database():
    conn = sqlite3.connect('./custom_cities.db')
    cur = conn.cursor()
    sql_string = "SELECT * FROM cities"
    cur.execute(sql_string)
    cities = cur.fetchall()
    city = random.choice(cities)
    conn.close()
    random_city_info={
            "name": city[0],
            "country_name": city[1],
            "sub_country":city[2],
            "country_code":city[3],
            "population":city[4],
            "description":city[5],
            "lat":city[6],
            "lng":city[7]
            }

    return random_city_info

@app.route("/",methods = ['POST', 'GET'])
def mapframe():
    if request.method == 'POST':
        if request.form['new_map_button']:
            user_selected_cities = request.form['cities'].split(',')
            add_city(user_selected_cities)
            new_city()
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/city")
def city():
    return render_template("interactive_city.html")


    
@app.route("/new_city")
def new_city():
    global city_info
    city_info = get_random_city_from_database()
    weather_response = json.loads(get_weather())
    weather = weather_response["weather"][0]["main"]
    temperature = str(int(k_to_f(weather_response["main"]["temp"])))
    city_info["weather"] = weather
    city_info["temperature"] = temperature
    return jsonify(city_info)

@app.route("/city_list")
def city_list():
    city_list = get_city_list_from_database()
    return jsonify(city_list)

@app.route("/current_city_data")
def city_data():
    global city_info
    weather_response = json.loads(get_weather())
    weather = weather_response["weather"][0]["main"]
    temperature = str(int(k_to_f(weather_response["main"]["temp"])))
    city_info["weather"] = weather
    city_info["temperature"] = temperature
    return jsonify(city_info)

@app.route("/get_weather")
def get_weather():
    global city_info
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+city_info["lat"]+"&lon="+city_info["lng"]+"&APPID=5b78504886ddcfc0bc5d2dc0129d0d82"
    response = requests.get(url)
    return response.text
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

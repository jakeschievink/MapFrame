from flask import Flask, request, render_template, jsonify
import glob, random, json, requests, pdb
app = Flask(__name__)

def get_random_city():
    json_cities = open('./citieslatlong.json').read()
    dict_cities = json.loads(json_cities)
    chosen_city = random.choice(dict_cities)
    return chosen_city

city_info=get_random_city()

def k_to_f(k):
    return ((k - 273) * 1.8 ) + 32

@app.route("/",methods = ['POST', 'GET'])
def mapframe():
    if request.method == 'POST':
        if request.form['new_map_button']:
            new_city()
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/city")
def city():
    return render_template("interactive_city.html")

@app.route("/new_city")
def new_city():
    global city_dir
    global city_info
    city_info = get_random_city()
    weather_response = json.loads(get_weather())
    weather = weather_response["weather"][0]["main"]
    temperature = str(int(k_to_f(weather_response["main"]["temp"])))
    city_info["weather"] = weather
    city_info["temperature"] = temperature
    return jsonify(city_info)

@app.route("/city_data")
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

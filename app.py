from flask import Flask, request, render_template, jsonify
import glob, random, json, requests, pdb
app = Flask(__name__)
cities = glob.glob("./static/data_maps/*/") 
image_pos=0
city_dir=random.choice(cities)

def get_city_data():
    json_file = open(city_dir+"city_data.json").read()
    data = json.loads(json_file)
    return data

city_info=get_city_data()

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

@app.route("/offline_city")
def offline_city():
    return render_template("city.html")

@app.route("/new_city")
def new_city():
    global city_dir
    global city_info
    city_dir = random.choice(cities) 
    city_info = get_city_data()
    weather_response = json.loads(get_weather())
    weather = weather_response["weather"][0]["main"]
    temperature = str(int(k_to_f(weather_response["main"]["temp"])))
    city_info["weather"] = weather
    city_info["temperature"] = temperature
    return jsonify(city_info)

@app.route("/city_data")
def city_data():
    global city_info
    city_info=get_city_data()
    weather_response = json.loads(get_weather())
    weather = weather_response["weather"][0]["main"]
    temperature = str(int(k_to_f(weather_response["main"]["temp"])))
    city_info["weather"] = weather
    city_info["temperature"] = temperature
    return jsonify(city_info)

@app.route("/city_url")
def city_url():
    global image_pos
    global city_dir
    global city_info
    images = ["1.jpg","2.jpg","3.jpg","6.jpg"]
    image_dir = city_dir+images[image_pos]
    if image_pos < 3:
        image_pos += 1  
    else:
        image_pos = 0
    return image_dir

@app.route("/get_weather")
def get_weather():
    global city_info
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+city_info["lat"]+"&lon="+city_info["lng"]+"&APPID=5b78504886ddcfc0bc5d2dc0129d0d82"
    response = requests.get(url)
    return response.text
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

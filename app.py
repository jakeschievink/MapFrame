from flask import Flask, request, render_template, jsonify
import glob, random, json
app = Flask(__name__)
cities = glob.glob("./static/data_maps/*/") 
image_pos=0
city_dir=random.choice(cities)

def get_city_data():
    json_file = open(city_dir+"city_data.json").read()
    data = json.loads(json_file)
    return data

city_info=get_city_data()

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
    return render_template("city.html")

@app.route("/new_city")
def new_city():
    global city_dir
    global city_info
    city_dir = random.choice(cities) 
    city_info = get_city_data()
    return jsonify(city_info)

@app.route("/city_data")
def city_data():
    global city_info
    city_info=get_city_data()
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

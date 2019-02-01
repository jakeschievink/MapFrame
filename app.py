from flask import Flask, request, render_template
import glob, random
app = Flask(__name__)
cities = glob.glob("./static/citymaps/*/") 
image_pos=0
ciry_dir=random.choice(cities)
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
    city_dir = random.choice(cities) 
    images = ["1.jpg","2.jpg","3.jpg","6.jpg"]
    image_dir = city_dir+images[0]
    return render_template("city.html", image_dir=image_dir)

@app.route("/new_city")
def new_city():
    global city_dir
    city_dir = random.choice(cities) 
    print(city_dir)
    return city_dir

@app.route("/city_url")
def city_url():
    global image_pos
    global city_dir
    images = ["1.jpg","2.jpg","3.jpg","6.jpg"]
    image_dir = city_dir+images[image_pos]
    if image_pos < 3:
        image_pos += 1  
    else:
        image_pos = 0
    return image_dir

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

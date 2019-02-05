from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageFont, ImageDraw
import json, random, os


image_size = (1024,1280)
class MapImageGrabber():
    def __init__(self):
        self.image_dir = './static/data_maps/'
        with open('./citieslatlong.json') as f:
            self.cities = json.load(f)


    def set_markers(self, staticmap, zoom_level,random_city):
        marker=CircleMarker((float(random_city['lng']), float(random_city['lat'])), 'black', 10)
        marker2=CircleMarker((float(random_city['lng'])+zoom_level, float(random_city['lat'])+zoom_level), 'black', 0)
        marker3=CircleMarker((float(random_city['lng'])-zoom_level, float(random_city['lat'])-zoom_level), 'black', 0)
        staticmap.add_marker(marker)
        staticmap.add_marker(marker2)
        staticmap.add_marker(marker3)

    def get_map_obj_with_center_mark(self, random_city,x_size=image_size[0],y_size=image_size[1],zoom=0.2):
        static_map=StaticMap(x_size,y_size,200,200, url_template="https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=125aa6ccc74f432ea81716925aa374ca" )
        self.set_markers(static_map, zoom, random_city)
        return static_map

    def save_map(self, map_to_save, random_city, zoom):
        name = random_city['name']
        try:
            os.mkdir(self.image_dir+"/"+name)
        except: pass
        ready_map = map_to_save.render()
        ready_map.save(self.image_dir+name+'/%s.jpg' % zoom)

    def save_maps_of_different_zoom_levels(self):
        random_city = self.cities[random.randint(0,len(self.cities))]
        random_city_name = random_city['name']
        random_city_country = random_city['country_name']
        close_map = self.get_map_obj_with_center_mark(random_city, zoom=0.02)
        self.save_map(close_map,random_city,"1")
        further_map = self.get_map_obj_with_center_mark(random_city, zoom=0.2)
        self.save_map(further_map,random_city,"2")
        furthest_map = self.get_map_obj_with_center_mark(random_city, zoom=2)
        self.save_map(furthest_map,random_city,"3")
        far_far__map = self.get_map_obj_with_center_mark(random_city, zoom=6)
        self.save_map(far_far__map,random_city, "6")
        with open(self.image_dir+random_city_name+'/city_data.json', 'w') as outfile:
            json.dump(random_city, outfile)

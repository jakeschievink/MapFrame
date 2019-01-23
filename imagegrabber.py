from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageFont, ImageDraw
import json, random, os, tkinter

root = tkinter.Tk()
font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-BoldOblique.ttf", 18)

with open('./cities.json/cities.json') as f:
    cities = json.load(f)

image_size = (root.winfo_screenwidth,root.winfo_screenheight)


def set_markers(staticmap, zoom_level,random_city):
    marker=CircleMarker((float(random_city['lng']), float(random_city['lat'])), 'black', 10)
    marker2=CircleMarker((float(random_city['lng'])+zoom_level, float(random_city['lat'])+zoom_level), 'black', 0)
    marker3=CircleMarker((float(random_city['lng'])-zoom_level, float(random_city['lat'])-zoom_level), 'black', 0)
    staticmap.add_marker(marker)
    staticmap.add_marker(marker2)
    staticmap.add_marker(marker3)

def get_map_obj_with_center_mark(random_city,x_size=image_size[0],y_size=image_size[1],zoom=0.2):
    static_map=StaticMap(x_size,y_size,200,200, url_template="https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=125aa6ccc74f432ea81716925aa374ca" )
    set_markers(static_map, zoom, random_city)
    return static_map

def save_labeled_map(map_to_save, random_city, zoom):
    img_dir = './citymaps/'
    name = random_city['name']
    try:
        os.mkdir(img_dir+"/"+name)
    except: pass
    ready_map = map_to_save.render()
    ready_map.save('/tmp/%smap.jpg' % name)
    img = Image.open('/tmp/%smap.jpg' % name)
    text=name+", "+random_city['country_name']
    decorate_image(img, text)
    print("saving")
    img.save(img_dir+name+'/%s.jpg' % zoom)

def save_maps_of_different_zoom_levels():
    random_city = cities[random.randint(0,len(cities))]
    random_city_name = random_city['name']
    random_city_country = random_city['country_name']
    close_map = get_map_obj_with_center_mark(random_city, zoom=0.02)
    save_labeled_map(close_map,random_city,"1")
    further_map = get_map_obj_with_center_mark(random_city, zoom=0.2)
    save_labeled_map(further_map,random_city,"2")
    furthest_map = get_map_obj_with_center_mark(random_city, zoom=2)
    save_labeled_map(furthest_map,random_city,"3")
    far_far__map = get_map_obj_with_center_mark(random_city, zoom=6)
    save_labeled_map(far_far__map,random_city, "6")

def decorate_image(img,text):
    draw = ImageDraw.Draw(img)
    x=100
    y=100
    shadow_color=(255,255,255) 
    draw.text((x-1, y-1), text, font=font, fill=shadow_color)
    draw.text((x+1, y-1), text, font=font, fill=shadow_color)
    draw.text((x-1, y+1), text, font=font, fill=shadow_color)
    draw.text((x+1, y+1), text, font=font, fill=shadow_color)
    draw.text((x,y), text, (0,0,0),font=font)
    


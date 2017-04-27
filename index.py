import picamera

from colorthief import ColorThief

import requests

camera = picamera.PiCamera()
#camera.resolution = (1024, 768)
camera.resolution = (640, 480)
camera.start_preview()

from time import sleep

file_name = "image_temp.png"

server_url = "https://waitnomore.herokuapp.com/bathroom_status"

def take_picture():
    print "Taking picture..."
    camera.capture(file_name)

def check_dominate_color():
    print "capturing dominant color"
    color_thief = ColorThief(file_name)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=10)
    print dominant_color
    r, g, b = dominant_color

    if r > 100:
        return "occupied"
    return "available"

    if r > g and r > b:
        ## color is red
        return "occupied"

    return "available"

    # build a color palette
    #palette = color_thief.get_palette(color_count=6)
    #print palette

def report_status(dominate_color):
    print "reporting status: {}".format(dominate_color)
    r = requests.post(server_url, json={"status": dominate_color} )
    print r.status_code
    print r.content

sleep(2)
while True:
    ## Take picture
    take_picture()

    ## Determine if red or green
    dominate_color = check_dominate_color()

    ## Make request to server if red or green
    try:
        report_status(dominate_color)
    except Exception as e:
        print e
        pass

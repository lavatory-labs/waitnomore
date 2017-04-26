import picamera

from colorthief import ColorThief

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

from time import sleep

file_name = "image_temp.png"

def take_picture():
    print "Taking picture..."
    camera.capture(file_name)


def check_dominate_color():
    color_thief = ColorThief(file_name)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=10)
    print dominant_color
    r, g, b = dominant_color

    print dominant_color
    if r > g:
        return "red"
    elif g > r:
        return "green"
    else:
        return "error"

    # build a color palette
    #palette = color_thief.get_palette(color_count=6)
    #print palette

sleep(2)
while True:
    ## take picture
    take_picture()

    ## Determine if red or green
    dominate_color = check_dominate_color()
    print dominate_color

    ## make request to server if red or green

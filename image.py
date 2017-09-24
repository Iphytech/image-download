import random
# module that will aid us download image from the web
import urllib.request

# function that will collect the image url to be downloaded
def download_image(url):

    name = random.randrange(1, 1000)

    full_name = str(name) + ".png"

    # function to save the image passed
    urllib.request.urlretrieve(url, full_name)

# url of the image to be downloaded
# you can also duplicate the function and add as many image urls as you wish
download_image("https://cdn.pixabay.com/photo/2017/01/06/19/15/soap-bubble-1958650_960_720.jpg")


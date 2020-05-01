from os import listdir, remove
from os.path import expanduser
from shutil import copy
from PIL.Image import open as PIL_open

assets_path = expanduser("~") + "/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
assets_converted_path = expanduser("~") + "/Pictures/Winodws Assets/Assets Converted/"

filter_logos = True  # determines whether the program should remove images that look like logos

for f in listdir(assets_path):
    copy(assets_path + f, assets_converted_path + f + ".png")
    if filter_logos:
        img = PIL_open(assets_converted_path + f + ".png")
        size = img.size
        img.close()
        if size[0] == size[1]:  # if the image is square its likely to be a logo
            remove(assets_converted_path + f + ".png")
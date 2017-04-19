import ctypes
import os


def find_path(folder="pics", image="pic.jpg"):
    drive = os.getcwd()
    return os.path.join(drive, folder, image)


def set_desktop():

    image_path = find_path()
    SPI_SETDESKWALLPAPER = 20
    response = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

    if not response:
        print("Couldn't find image.")

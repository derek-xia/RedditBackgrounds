import requests
import windows


def save_pic(url):
    image_path = windows.find_path()

    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print("'There was a problem: %s" % (exc))

    file = open(image_path, "wb")
    for chunk in res.iter_content(128):
        file.write(chunk)

    file.close()

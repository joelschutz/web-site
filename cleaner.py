"""

This is a simple function to clean the jsons archive so the application can get new images. Since Heroku
kills your program after a while and start it again every time, this test will be made almost everytime a
new connection to the seerver is made.

"""
import os

def jsons_cleaner():
    folder_path = './portifolio/jsons'
    folder = os.listdir(folder_path)
    if len(folder) > 20:
        for f in folder:
            os.remove(f)

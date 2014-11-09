import shutil
import requests

url = 'http://img-9gag-lol.9cache.com/photo/anXOZ9V_460sa_v1.gif'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
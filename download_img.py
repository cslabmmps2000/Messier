import requests
import shutil

URL = "https://osricdienda.com/messier-api/images/M{num}.jpg"
for i in range(1, 111):
    res = requests.get(URL.format(num=i), stream=True)
    f = open(f'Image Files/Messier_{i}.jpg', 'wb')
    shutil.copyfileobj(res.raw, f)
    f.close()

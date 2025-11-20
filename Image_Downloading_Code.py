import requests as req
import shutil as shush
import time

URLs = f"https://osricdienda.com/messier-api/images/M{num}.jpg"
for i in range(1, 111):
    print(f"Downloading Image for Messier {i}")
    Response = req.get(URLs(num=i), stream=True)
    f = open(f'Image Files/Messier_{i}.jpg', 'wb')
    shush.copyfileobj(Response.raw, f)
    f.close()

print("All Images successfully Downloaded! :D")
time.sleep(1)
exit()
#Thanks! :D
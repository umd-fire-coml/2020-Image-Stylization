import requests
import shutil
import os
from requests.auth import HTTPBasicAuth
os.chdir("../")
if os.system("mkdir data") != 0:
    print("Error while creating data directory")
    quit()

os.chdir("data")

for i in range(1, 61):
    url = "https://raw.githubusercontent.com/aw183052/image_stylization_data/master/data/input/in" + str(i) + ".png"
    r = requests.get(url, auth=HTTPBasicAuth('user', 'pass'), stream=True)
    if r.status_code == 200:
        with open("in" + str(i) + ".png", 'wb') as handler:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, handler)
    else:
        print("Error while downloading in" + str(i) + ".png\n")
        quit()

print("data downloaded successfully")
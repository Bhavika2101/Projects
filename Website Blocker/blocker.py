import time
from datetime import datetime as dt

ho = "hosts"
temp = r"E:\Python Apps\App3\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "35.156.90.191"
webList = ["www.netflix.com","netflix.com", "www.primevideo.com", "www.hotstar.com","primevideo.com","hotstar.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <  dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours!!")
        with open(ho , 'r+') as file:
            con=file.read() 
            for web in webList:
                if web in con:
                    pass
                else:
                    file.write(redirect + " " + web + "\n")
    else:
        with open(ho , 'r+') as file:
            con=file.readlines()
            file.seek(0)
            for line in con:
                if not any(web in line for web in webList):
                    file.write(line)
            file.truncate()
        print("fun hours!!")
    time.sleep(5)

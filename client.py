__author__ = 'jmh081701'
import  requests
import  time
import  os
from multiprocessing import  Process
import  copy
import json
req_json={
    "timestamp":0,
    "info":""
}
def fox():
    fox=os.popen("firefox http://210.77.16.21")
while True:
    #fox=os.popen("firefox http://210.77.16.21")
    p=Process(target=fox)
    p.start()
    posturl="http://67.218.148.94:801/post/osinfo"
    time.sleep(5)
    p.terminate()
    p.join()
    req=copy.deepcopy(req_json)
    req['timestamp']=time.time()
    ip = os.popen("ifconfig eth0")
    msg =ip.readlines()
    req['info']=str(msg)
    headers = {"Content-Type": "application/json"}
    requests.post(url=posturl,data=json.dumps(req),headers=headers)
    print("post well")
    print(req)
    time.sleep(30)

__author__ = 'jmh081701'
import  requests
import  time
import  os
import  copy
req_json={
    "timestamp":0,
    "info":""
}
while True:
    os.popen("firefox http://210.77.16.21")
    posturl="http://67.218.148.94:801/post/osinfo"
    time.sleep(5)
    os.close()
    req=copy.deepcopy(req_json)
    req['timestamp']=time.time()
    ip = os.popen("ifconfig eth0")
    msg =ip.readall()
    req['info']=str(msg)
    requests.post(url=posturl,json=req)
    sleep(30)

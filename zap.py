import time
from zapv2 import ZAPv2
print("Enter 1 for spidering")
print("Enter 2 for active scan")
print("Enter 3 for passive scan")
n = int(input())
target = 'https://graphql.org/swapi-graphql'
apikey = '123456'
zap = ZAPv2(apikey=apikey,proxies={'http':'http://localhost:8081','https':'http://localhost:8081'})
zap.urlopen(target)
if n==1:
    scanID = zap.spider.scan(target)
    zap.spider.scan(url=target, apikey=apikey)
    time.sleep(5)
    while(int(zap.spider.status(scanID))<100):
        print('Spider progress %: ' + zap.spider.status(scanID))
        time.sleep(5)
    print('Spider completed')
    with open ('report-spider.html', 'w') as f:f.write(zap.core.htmlreport(apikey = 'apikey'))
if n==3:
    while(int(zap.pscan.records_to_scan)>0):
        print('Pscan records: ' +zap.pscan.records_to_scan)
        time.sleep(5)
    print('Passive scan completed')
    with open ('report-passive.html', 'w') as f:f.write(zap.core.htmlreport(apikey = 'apikey'))
if n==2:
    
    zap.ascan.scan(url=target,apikey=apikey)
    time.sleep(5)
    while(int(zap.ascan.status()) < 100):
        print ('Ascan progress %: ' + zap.ascan.status())
        time.sleep(5)
    print('Active Scan completed')
    with open ('report-active.html', 'w') as f:f.write(zap.core.htmlreport(apikey = 'apikey'))






















#target = 'http://127.0.0.1:5000/difficulty/hard'

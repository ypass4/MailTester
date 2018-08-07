import requests
from termcolor import colored
import time
i = 0
j = 0
session = requests.Session()
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0","Referer":"http://mailtester.com/testmail.php","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded"}
cookies = {"CMT_user":"420ff707-e984-45c3-aaef-aabe5e82c576","_gat":"1","_ga":"GA1.2.680913877.1509000237","CMT_version":"0.3.49","interstitialCallsCount":"0","__gads":"ID=a641096215fe70d1:T=1509000238:S=ALNI_MZc7cs0yuWNfmMO83xkOtFvbbn2rQ","_gid":"GA1.2.631912963.1510118207"}
with open('not-analysed.txt') as email_list , open('verified.txt','w') as v_file , open('not-verified.txt','w') as nv_file:
    for line in email_list.readlines() :
        line = line.strip()
        paramsPost = {"lang":"en","email":line}
        response = session.post("http://mailtester.com/testmail.php", data=paramsPost, headers=headers,cookies=cookies)
        if int(response.content.find("E-mail address is valid")) == -1 :
            i = i+1
            nv_file.write(line+'\n')
            print(colored(line,'red'))
        else:
            j = j+1
            v_file.write(line+'\n')
            print(colored(line,'green'))
        time.sleep(1)
print(colored("not-verified: %s" %(i),'red'))
print(colored("verified: %s" %(j),'green'))
print(colored("total: %s" %(j+i),'blue'))

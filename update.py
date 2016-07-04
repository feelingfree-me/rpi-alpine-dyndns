import requests
import time
import json
import os
import sys
    

username = os.getenv('username')
password = os.getenv('password')
hostname = os.getenv('hostname')
delay =  int(os.getenv('delay', '15'))

dynupdate = "https://members.dyndns.com/nic/update"
ip = '0.0.0.0'


def getIP():
    global ip
    res = requests.get('http://ipinfo.io')
    if res.status_code is not 200:
        print_time("[Error] - can not get connection")
        return None
    res = res.json()['ip']
    if res is None:
        print_time("[Error] - can not find IP")
        return None
    ip = res
    print_time("IP address " + ip)
    return True


# update dyndns
def update(hostname, ip):
    print_time("Updating...")
    headers = {'user-agent': 'Mozilla/5.0'}
    dyn = requests.get( dynupdate, \
                        headers=headers, \
                        auth=(username, password), \
                        params={'hostname': hostname, \
                                'myip': ip, \
                        })

    if dyn.status_code is not 200:
        print_time("Update failed. HTTP Code: " + str(dyn.status_code))
    if "good" in dyn.text:
        print_time("Update successful..")
    else:
        print_time("Update unsuccessful: " + dyn.text.strip())
    print("-----------------------------------")

def main():
    if username is None or password is None or hostname is None:
        print("Please check variable: username, password and hostname.")
        sys.exit(0)
    while True:
        if getIP():
            update(hostname, ip)
        time.sleep( delay * 60 )

def print_time(text):
    print(time.strftime("%-d/%-m/%Y, %I:%M %p", time.localtime()), text)


if __name__ == '__main__':
  main()
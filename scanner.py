import requests
import threading
import sys
import random
import json

def scan_ip(ip):
    
    print(ip)

    try:
        request = requests.get("http://" + ip, timeout = 3)
        
        cip = {
            "ip": ip,
            "status": str(request.status_code),
            "headers": str(request.headers),
            "data": str(request.content)
            }

        global code
        code[ip] = cip

    except: print("")

    sys.exit(0)

with open("websites.txt") as ips:
    ip = ips.read()

ip_list = ip.split("\n")
full_list = []

for i in ip_list:
    if len(i) != 0:
        full_list.append(i.split(":")[0].strip())

code = {}

max_threads = 1024
threads = []

for i in range(max_threads):
    cip = random.choice(full_list)
    full_list.remove(cip)
    
    threads.append(threading.Thread(target = scan_ip, args = [cip]))

    started = False

    threads[i].start()

while len(full_list) > 0 and threading.activeCount() != 0:
    print(len(full_list))
    try:
        cip = random.choice(full_list)
        full_list.remove(cip)
        if len(threads) <= max_threads:
            threads.append(threading.Thread(target = scan_ip, args=[cip]))
            threads[-1].start()

        else:
            threads = []

    except:
        pass

print("Ready to write!")

while threading.activeCount() != 1:
    print("Waiting for", threading.activeCount() - 1, "threads to finish")

with open("websites.json", "w") as jsonfile:
    json.dump(code, jsonfile)
    
print("Written!")

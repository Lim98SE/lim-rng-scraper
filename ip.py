import random
import requests
import threading
import sys
import time

test_threads = []
max_threads = 12

def test_website(thread):
    # print(threading.get_ident())
    ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    # print("Testing", ip)

    try:
        req = requests.get("http://" + ip, timeout = 3)

        print(ip, "returned", req.status_code)

        if req.status_code == 200:

            with open("websites.txt", "a") as file:
                file.write("\n" + ip + ": " + str(req.status_code) + "\n")

        else:
            with open("bad_websites.txt", "a") as file:
                file.write("\n" + ip + ": " + str(req.status_code) + "\n")

    except:
        bad(ip)

    global test_threads

    try:
        test_threads.pop(thread)

    except:
        pass

    time.sleep(0.5)
    sys.exit()

def bad(ip):
    print("None found")

for i in range(max_threads):
    test_threads.append(threading.Thread(target = test_website, args = [i]))

    started = False

    test_threads[i].start()

while True:
    try:
        if len(test_threads) <= max_threads:
            test_threads.append(threading.Thread(target = test_website, args=[len(test_threads) - 1]))
            test_threads[-1].start()

    except:
        pass

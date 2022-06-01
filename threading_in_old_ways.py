from re import L
import threading
import time


start = time.perf_counter() #initalize the starting time

def do_anything(second):
    print(f'Sleeping for {second} seconds(s)...')
    time.sleep(1) # sleeps for 1sce
    print('Done Sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_anything, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter() ##initalize the finishing time

print(f'Finished in {round(finish - start, 2)} sceonds') #calculates the time took to run the code
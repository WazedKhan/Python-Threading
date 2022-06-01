# This scripts contains an example of non-threading code

import time


start = time.perf_counter() #initalize the starting time

def do_anything():
    print('Programs starting......')
    time.sleep(1) # sleeps for 1sce
    print('Wakes ups -------')


do_anything()

finish = time.perf_counter() ##initalize the finishing time

print(f'Finished in {round(finish - start, 2)} sceonds') #calculates the time took to run the code
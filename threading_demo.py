import concurrent.futures
import time


start = time.perf_counter() #initalize the starting time

def do_anything(second):
    print(f'Sleeping for {second} seconds(s)...')
    time.sleep(1) # sleeps for 1sce
    return f'Done Sleeping... {second}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    """ Future object: its basically encapsulate's the execution of a function after
        its been scheduled so we can chcek that its running or if its done also chcek result"""
    secs = [1, 2, 5, 6, 4]
    # results = [executor.submit(do_anything, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = executor.map(do_anything, secs)

    for result in results:
        print(result)



finish = time.perf_counter() ##initalize the finishing time

print(f'Finished in {round(finish - start, 2)} sceonds') #calculates the time took to run the code
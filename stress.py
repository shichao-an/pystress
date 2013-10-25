from multiprocessing import Process
import os
import sys
import time


def stress():
    a = 100.01
    b = 99.99
    c = None
    print 'process id:', os.getpid()
    while True:
        c = a * b
    return c


if __name__ == "__main__":
    procs = []
    for i in range(5):
        p = Process(target=stress)
        p.start()
        procs.append(p)

    time.sleep(int(sys.argv[1]))
    
    for p in procs:
        p.terminate()

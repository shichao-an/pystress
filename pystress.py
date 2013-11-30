__version__ = '0.2.1'

from multiprocessing import Process, active_children, cpu_count, Pipe
import os
import signal
import sys
import time


FIB_N = 100
DEFAULT_TIME = 60
try:
    DEFAULT_CPU = cpu_count()
except NotImplementedError:
    DEFAULT_CPU = 1


def loop(conn):
    proc_info = os.getpid()
    conn.send(proc_info)
    conn.close()
    while True:
        fib(FIB_N)


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def sigint_handler(signum, frame):
    procs = active_children()
    for p in procs:
        p.terminate()
    os._exit(1)


signal.signal(signal.SIGINT, sigint_handler)


def get_args():
    exec_time = DEFAULT_TIME
    proc_num = DEFAULT_CPU
    if len(sys.argv) > 3:
        raise
    if len(sys.argv) == 2:
        exec_time = int(sys.argv[1])
    if len(sys.argv) == 3:
        exec_time = int(sys.argv[1])
        proc_num = int(sys.argv[2])

    return exec_time, proc_num


def _main():
    try:
        exec_time, proc_num = get_args()
    except:
        msg = "Usage: pystress [exec_time] [proc_num]\n"
        sys.stderr.write(msg)
        sys.exit(1)
    procs = []
    conns = []
    for i in range(proc_num):
        parent_conn, child_conn = Pipe()
        p = Process(target=loop, args=(child_conn,))
        p.start()
        procs.append(p)
        conns.append(parent_conn)

    for conn in conns:
        try:
            print conn.recv()
        except EOFError:
            continue

    time.sleep(exec_time)

    for p in procs:
        p.terminate()


if __name__ == "__main__":
    _main()

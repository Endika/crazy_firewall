"""Crazy FIREWAL."""
import Queue
import os
from threading import Thread
from random import randint
import time

q = Queue.Queue()


def listen_port(q, number):
    """Listen specific port."""
    print ("PORT {} open".format(number))
    os.system('nc -l {}'.format(number))
    q.put(number)


def open_random_port(limit):
    """Open random ports."""
    command = '''
        netstat -plutn |
        grep "LISTEN" |
        grep -oh ":[0-9]*" |
        grep -v -e "^:$" | tr -d ":"'''
    ports_list = os.popen(command).read().split('\n')[:-1]
    ports_list = [int(i) for i in ports_list]
    for i in range(limit):
        port = False
        while True:
            port = randint(0, 65535)
            if port not in ports_list:
                break
        worker = Thread(target=listen_port, args=(q, port))
        worker.setDaemon(True)
        worker.start()
        ports_list.append(port)


open_random_port(500)  # Caution

while True:
    print "Check..."
    for i in range(q.qsize()):
        print ('ALERT IN {} PORT'.format(q.get()))
        open_random_port(1)
    time.sleep(5)

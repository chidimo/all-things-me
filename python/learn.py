import os
import numpy as np
from time import time
from multiprocessing import Process, Queue
# from threading import Thread, Lock
# from time import sleep

def calculate_random(number_points):
    for i in range(10, number_points):
        data = np.random.random(i)
        fft = np.fft.fft(data)
    return fft

def move_from_in_to_out(q_in, q_out):
    while not q_in.empty():
        data = q_in.get()
        q_out.put(data)


if __name__ == "__main__":
    os.system('clear')
    q_in = Queue()
    q_out = Queue()

    for i in range(1000):
        q_in.put(i)

    p = Process(target=move_from_in_to_out, args=(q_in, q_out))
    p2 = Process(target=move_from_in_to_out, args=(q_out, q_in))
    p.start()
    p.join()
    p2.start()

    print('Q_in is empty: {}'.format(q_in.empty()))

    while not q_out.empty():
        print(q_out.get())

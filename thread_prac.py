from threading import Thread
import time


def func_thread1():
    for i in range(100):
        # time.sleep(1)
        print("first thread", i)

def func_thread2():
    for i in range(100):
        # time.sleep(1)
        print("second thread", i)

def main_func():
    start = time.time()
    thread_one = Thread(target=func_thread1)
    thread_two= Thread(target=func_thread2)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
    # func_thread1()
    # func_thread2()
    end = time.time()
    diff = end - start
    print(diff)
main_func()
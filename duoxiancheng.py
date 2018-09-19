from threading import Thread
import time


def func1(x, y):
    for i in range(x, y):
        print(i, end='')
    print()
    time.sleep(10)


t1 = Thread(target=func1, args=(15, 20))
t1.start()
t1.join(5)
t2 = Thread(target=func1, args=(5, 10))
t2.start()

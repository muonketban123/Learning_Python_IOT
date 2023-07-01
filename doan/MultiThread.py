from threading import Thread
import time

# <name_thread> = Thread(target = <funtion>)
# <name_thread>.start()

def printName():
    while True:
        print('toàn')
        time.sleep(5)
    print(text)

def printAddress():
    while True:
        print('quỳnh')
        time.sleep(10)
    print(text)

thread1 = Thread(target = printName)
thread1.start()

thread2 = Thread(target = printAddress)
thread2.start()

while True:
    print("My thread")
    time.sleep(1)
import time

def happy_b():
    return "Happy birthday to you"

print(happy_b())

def count(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("DONE!")

count(0, 5)
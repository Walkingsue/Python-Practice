import time
my_time = int(input("Enter your time: "))
for x in range(my_time, 0, -1):
    hours = x // 3600
    minutes = (x % 3600) // 60
    seconds = x % 60
    print(f"{hours:02}: {minutes:02}: {seconds:02}")
    time.sleep(1)
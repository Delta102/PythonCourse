import time
old = time.time()
timeSuspend = 5
print("Program Start")
time.sleep(timeSuspend)
print("Program Ends")
current = time.time()
print(f'Time taken is {current-old}')
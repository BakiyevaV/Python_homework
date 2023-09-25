import threading

numbers = tuple(range(50))
aver = 0
lock = threading.Lock()
thread_num = 5
def get_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    global aver
    lock.acquire()
    aver += sum / len(numbers)
    lock.release()

for i in range(thread_num):
    start = i * 10
    stop = (i + 1) * 10
    thread = threading.Thread(target = get_average, args = [(numbers[start:stop])])
    thread.start()
    thread.join()


aver = aver/thread_num
print(aver)
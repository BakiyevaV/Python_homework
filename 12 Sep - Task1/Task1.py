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
    #VN: Здорово, что вы не забыли про блокировку!
    lock.acquire()
    aver += sum / len(numbers)
    lock.release()

#VN: Этот цикл лучше всего вынести в отдельную функцию с аргументами numbers и thread_num
for i in range(thread_num):
    #VN: вместо явной константы 10 длину среза для потоков лучше вычислять. Иначе ваше 
    # решение очень сильно сильно зависит от конкретной длины numbers, и для другой длины будет падать
    start = i * 10
    stop = (i + 1) * 10
    thread = threading.Thread(target = get_average, args = [(numbers[start:stop])])
    thread.start()
    thread.join()


aver = aver/thread_num
print(aver)
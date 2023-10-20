import hashlib
import string
import random
# from logger import log
import time
def get_time(func):
    def wrapper(self):
        start_time = time.time()
        print("Время начала ",start_time)
        # log.log_i("Время начала ",start_time)
        func(self)
        end_time = time.time()
        # log.log_i("Время окончания ",end_time)
        print("Время окончания ",end_time)
        res = end_time - start_time
        # log.log_i(f"Результат: {res} секунд ({res//60} минут {res%60} секунд)")
        print(f"Результат: {res} секунд ({res//60} минут {res%60} секунд)")
        print("Результат ",res)
    return wrapper

class Hacker():
    def __init__(self, sample, length, input_list):
        self.sample = sample
        self.length = length
        self.input_list = input_list


    @get_time
    def hack_the_pass(self):
        self.tries = 0
        self.run = True
        while self.run:
            # log.log_d("Зашли в цикл")
            variant= self.get_variant()
            # log.log_i("Получили вариант ",variant)
            result = self.hash_variant(variant)
            # log.log_i("Получили результат ",result)
            self.tries += 1
            if (result == self.sample):
                self.run = False
                # log.log_t("Пароль: ", variant[0], "попыток: ", self.tries)
                print("Пароль: ", variant[0], "попыток: ", self.tries)


    def get_variant(self):
        variant = ""
        var_list = []
        for _ in range(self.length):
            sign = random.choice(self.input_list)
            variant += sign
        var_list.append(variant)
        return var_list
    
    def hash_variant(self, variant):
        varnt = variant[0]
        # log.log_i("Вариант для хэширования ",varnt)
        hash_object = hashlib.md5(varnt.encode("UTF-8"))
        result = hash_object.hexdigest()
        return result




input_list = list(string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "~!@#$%^&*()_+-=")

h1 = Hacker("f232b847c44bd9992dd04efe19597ee6", 8, input_list)
h1.hack_the_pass()


# Время начала  1697731083.650517
# Пароль:  7&UP попыток:  33677737
# Время окончания  1697731162.000737
# Результат: 78.35021996498108 секунд (1.0 минут 18.35021996498108 секунд)



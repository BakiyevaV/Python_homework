import json

class Car:
    def __init__(self, trademark, color, source, destination ,speed,fuel_tank_volume,oil_tank_volume,  fuel_vol=0, oil_vol=0,mileage = 0, betw_reoil = 0):
        self.trademark = trademark
        self.color = color
        self.mileage = mileage
        self.fuel_vol = fuel_vol
        self.oil_vol = oil_vol
        self.fuel_tank_volume = fuel_tank_volume
        self.oil_tank_volume = oil_tank_volume
        self.betw_reoil = betw_reoil
        self.source = source
        self.destination = destination 
        self.speed = speed

    def move(self):
        distance = 0
        kilometers = int(len(self.source) + len(self.destination))
        kilometers *=20
        time = kilometers / self.speed
        min_fuel_vol = self.fuel_tank_volume * 0.02
        min_oil_vol = self.oil_tank_volume * 0.09
        while distance < kilometers:
            if self.fuel_vol <= 0:
                result = "Нет топлива. Стоим!"
                break
            if self.oil_vol <= 0:
                result = "Поломка двигателя!"
                break
            distance += 1
            self.mileage += 1 
            self.fuel_vol = max(0, self.fuel_vol - 0.15)
            self.oil_vol = max(0, self.oil_vol - 0.005)
            self.betw_reoil += 1 
            if self.fuel_vol <= min_fuel_vol:
                fuel_add_ask = input("Уровень топлива снизился до критической отметки и составляет %s л. Будем заправляться?" %self.fuel_vol)
                if fuel_add_ask.lower() in ["да","д","yes"]:
                    self.add_fuel()                        
                    
            if  self.oil_vol <= min_oil_vol:
                add_oil_ask = input("Уровень масла снизился до критической отметки и составил %s. Будем доливать?" %self.oil_vol)
                if add_oil_ask.lower() in ["да","д","yes"]:
                    self.add_oil()
            
            if self.betw_reoil>= 3000:
                result = f"Вы не меняли масло:{self.betw_reoil} км. Двигатель сломался!"
                break
                           

        else:     
            result = f"""Выехали из {self.source} -----------------------> Приехали в {self.destination}.\ 
        В пути были {time}ч.;\ 
        Скорость {self.speed};\ 
        Расстояние {kilometers} км.;\ 
        Осталось топлива: {self.fuel_vol};\ 
        Осталось масла: {self.oil_vol}
        Пробег: {self.mileage} км.
        Км с последней замены масла:{self.betw_reoil}"""

        return result


    def add_fuel(self):
        add_fuel_vol = int(input("Сколько будем заправлять?"))
        fuel_sum = add_fuel_vol + self.fuel_vol
        if fuel_sum > self.fuel_tank_volume:
            dif_fuel = fuel_sum - self.fuel_tank_volume
            self.fuel_vol = self.fuel_tank_volume
            print( f"Бак полный({self.fuel_vol} л.). Вылилось {dif_fuel}")
            
        elif fuel_sum <= self.fuel_tank_volume:
            self.fuel_vol += add_fuel_vol
            print( f"Отлично!Уровень топлива {self.fuel_vol}")
            
    
    def add_oil(self):
        add_oil_vol = int(input("Сколько будем заправлять масла?"))
        sum = add_oil_vol + self.oil_vol
        if sum > self.oil_tank_volume:
            self.oil_vol = self.oil_tank_volume
            dif_oil = sum - self.oil_tank_volume
            print(f"Уровень масла - 100%({self.oil_vol} л. ). Вылилось {dif_oil}")
        elif sum <= self.oil_tank_volume:
            self.oil_vol += add_oil_vol
            print( f"Отлично!Уровень масла {self. oil_vol}")


    def check_oil_change(self):
        if self.betw_reoil < 1000:
            dif_reoil = 1000 - self.betw_reoil
            result = f"До желательной замены масла осталось {dif_reoil}"
        elif self.betw_reoil >= 1000 and  self.betw_reoil <= 1300:
            reoil_ask = input(f"С момента последней замены масла вы проехали:{self.betw_reoil}. Будете менять масло?")
            if reoil_ask.lower() in ["да","д","yes"]:
                self.reoil()
                result = "Отлично!"
            else:
                result ="Это не хорошо!"

        elif self.betw_reoil > 1300 and self.betw_reoil < 3000:
            dif_reoil = self.betw_reoil - 1000
            reoil_ask2 = input (f"Не тяни с заменой масла!Ты проехал {dif_reoil} больше нормы в - 1000 км.\n Может произойти поломка двигателя. Ты хочешь заменить масло?")
            if reoil_ask2.lower() in ["да","д","yes"]:
                self.reoil()
                result = "Вовремя успели"
            else:
                result ="Это не хорошо!"

        elif self.betw_reoil >= 3000:
            result = "Поздно!"
        return result    
    
    def reoil(self):
        self.oil_vol = self.oil_tank_volume
        self.betw_reoil = 0
        result =  print (f"Поменяли масло. Текущий уровень масла: {self.oil_vol}")
        return result


    def save_data(self, filename):
        data = {
            'mileage': self.mileage,
            'fuel_vol': self.fuel_vol,
            'oil_vol': self.oil_vol,
            'betw_reoil':self.betw_reoil
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    def load_data(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.mileage = data['mileage']
            self.fuel_vol = data['fuel_vol']
            self.oil_vol = data['oil_vol']
            self.betw_reoil = data ['betw_reoil']
#При первом запуске использовать код указанный ниже. Должен появиться json файл. Где будут переданные значения. 
mustang = Car("Ford", "Черный","Алматы","Астана",100, 70, 7, 70, 7)
mustang.save_data('data.json')
print(mustang.fuel_vol, mustang.oil_vol, mustang.mileage)
print(mustang.move)
print(mustang.check_oil_change())

# После создания файла активировать часть кода указанную ниже взамен верхней в целях актуализации данных.
# mustang = Car("Ford", "Черный","Алматы","Астана",100, 70, 7, 70, 7)
# mustang.load_data('data.json')
# print(mustang.fuel_vol, mustang.oil_vol, mustang.mileage)
# print(mustang.move())
# mustang.save_data('data.json')
# print(mustang.check_oil_change())
# mustang.save_data('data.json')

# impala = Car("Chevrolet", "Черный","Брюссель","Мадрид",70, 70, 8, 70, 8)
# impala.save_data('data.json')
# print(impala.fuel_vol, impala.oil_vol, impala.mileage)
# print(impala.move)
# print(impala.check_oil_change())

# impala = Car("Chevrolet", "Черный","Брюссель","Мадрид",70, 70, 8, 70, 8)
# impala.load_data('data.json')
# print(impala.fuel_vol, impala.oil_vol, impala.mileage)
# print(impala.move())
# impala.save_data('data.json')
# print(impala.check_oil_change())
# impala.save_data('data.json')
 
# gtr = Car("Nissan", "Черный","Ницца","Монако",180, 60, 6, 30, 3)
# gtr.save_data('data.json')
# print(gtr.fuel_vol, gtr.oil_vol, gtr.mileage)
# print(gtr.move)
# print(gtr.check_oil_change())

# gtr = Car("Nissan", "Черный","Ницца","Монако",180, 60, 6, 30, 3)
# gtr.load_data('data.json')
# print(gtr.fuel_vol, gtr.oil_vol, gtr.mileage)
# print(gtr.move())
# gtr.save_data('data.json')
# print(gtr.check_oil_change())
# gtr.save_data('data.json')

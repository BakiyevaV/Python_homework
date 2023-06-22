import datetime
class Dog:

    def __init__ (self,name, breed, color,birth_date, height, weight, walking_time_norm, min_1time_eat_norm, min_1time_drink_norm, bladder_vol = 450, bladder_water_vol= 0, birth_day = 0, birth_month = 0, birth_year=0, age = 0, age_status = 0, walked_time =0):
        self.name = name
        self.breed = breed
        self.color = color
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
        self.walking_time_norm = walking_time_norm
        self.min_1time_eat_norm = min_1time_eat_norm
        self.min_1time_drink_norm = min_1time_drink_norm
        self.bladder_vol = bladder_vol
        self.bladder_water_vol = bladder_water_vol
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.age = age
        self.age_status = age_status
        self.walked_time = walked_time


    
    def eat (self):
        self.food_eaten = 0
        while self.food_eaten < self.min_1time_eat_norm:
            food = input("Сколько еды дать собаке в граммах? ")
            if food in ["0","нет","н"]:
                return "Гав (Жадина!)"
            else: 
                food = int(food) 
                self.food_eaten += food
                if self.food_eaten >= self.min_1time_eat_norm:
                    return "Гав (Спасибо за еду!)"
    
    def drink (self):
        self.water_drank = 0
        while self.water_drank < self.min_1time_drink_norm:
            water = input("Сколько воды дать собаке в мл.? ")
            if water in ["0","нет","н"]:
                return "Гав (Жадина!)"
            else: 
                water = int(water) 
                self.water_drank += water         
        self.piss_request() 
        return "Гав (Спасибо за воду!)" 
               
           
                    
    def piss_request(self):
        self.bladder_water_vol = self.water_drank * 0.4
        if self.bladder_vol < self.bladder_water_vol:
            user_decision = input ("Гав-гав (Я хочу пи! Пойдем на прогулку ?)")
            if user_decision in ["ок","да","д"]:
                self.walk()
                if self.walked_time > self.walking_time_norm:
                    print(self.piss_action())
            if user_decision in ["нет","н"] or self.walked_time < self.walking_time_norm:
                print(self.piss_action(),"Без твоего согласия")
    
    def piss_action(self):
        self.bladder_water_vol = 0
        return "Гав (Я все сделал!)"

                
    def walk(self):
        self.walked_time = 0
        while self.walked_time < self.walking_time_norm:
            walking_time = input("Сколько часов мы будем гулять?")
            if walking_time in ["0","нет","н"]:
                print("Гав-Гав(Не дам тебе спать ночью!)")
                break
            walking_time = int(walking_time)
            self.walked_time += walking_time
        return self.walked_time

    def growth_weight (self): 
        if self.weight < 90 and self.food_eaten > self.min_1time_eat_norm and self.walked_time < self.walking_time_norm:
            self.weight += 1
        return self.weight
    
    def growth_height (self): 
        if self.height < 75 and self.food_eaten > self.min_1time_eat_norm:
            self.height += 1
        return self.height
    
    def info(self):
        self.birth_day,self.birth_month, self.birth_year = map(int, self.birth_date.split('-'))
        today = datetime.date.today()
        self.age = (((today.year - self.birth_year)*365) + ((today.month - self.birth_month)*30)+(today.day - self.birth_day))//365
        if self.age < 1:
            self.age_status = "Щенок"
        elif self.age >= 1:
            self.age_status = "Взрослая собака"
        info = f"""{self.age_status}:\ 
            Имя: {self.name};\ 
            Порода: {self.breed};\ 
            Окрас: {self.color};\ 
            Дата рождения: {self.birth_date};\ 
            Возраст: {self.age};\ 
            Вес: {self.growth_weight()};\ 
            Рост: {self.growth_height()};\ 
            """
        return info
        
        
# dog1 = Dog("Локи", "Доберман" ,"черный","21-03-2020",70, 50, 2, 400, 400, 450)
# print(dog1.eat())
# print(dog1.drink())
# print(dog1.info())

# dog2 = Dog("Алиса", "Тойтерьер" ,"белый","21-03-2023",15, 1.7, 1.5, 150, 200, 120)
# print(dog2.eat())
# print(dog2.drink())
# print(dog2.info())

dog3 = Dog("Бетховен", "Сембернар" ,"Черная","04-06-2012",120, 80, 3, 600, 600, 450)
print(dog3.eat())
print(dog3.drink())
print(dog3.info())





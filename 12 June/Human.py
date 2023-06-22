from datetime import datetime 
from random import randint 
class Human():
    def __init__(self, name, gender, birth_place, spouse, birth_year=0, birth_month=0, birth_date=0, weight=0, height=0, birth_status=True, age=0, work_status=False,family_status=False, age_status = ""):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.age = age
        self.age_status = age_status
        self.birth_status = birth_status
        self.weight = weight
        self.height = height
        self.work_status = work_status
        self.spouse = spouse
        self.family_status = family_status

    def birth(self):
        if self.birth_status == True:
            self.weight = randint(1, 5)
            self.height = randint(30, 55)
            self.birth_year = randint(1950, 2023)
            self.birth_month = randint(1, 12)
            self.birth_date = randint(1, 31)
            if self.birth_year == 2023:
                self.birth_month = randint(1, 6)
                self.age = 0

        return (self.weight,self.height,self.birth_year,self.birth_month,self.birth_date)

    def get_age(self):
        current_datetime=datetime.now()
        current_datetime_str=str(current_datetime)
        year=int(current_datetime_str[0:4])
        month=int(current_datetime_str[5:7])
        date=int(current_datetime_str[8:10])
        
        dif_year=year-self.birth_year 
        dif_month=month-self.birth_month 
        dif_date=date-self.birth_date 
        
        self.age=(dif_date+(dif_month*30)+(dif_year*12*30))//365
        
        return self.age   
    
    def growth(self, current_age=0):
        if self.gender == "Женский пол" and current_age <= 25:
            if self.weight > 75 or self.height > 180 or current_age >= self.get_age():
                return self.weight, self.height
            else:
                self.weight += 2
                self.height += 5
                return self.growth(current_age + 1)
        elif self.gender == "Мужской пол" and current_age < 30:
            if self.weight > 100 or self.height > 195 or current_age >= self.get_age():
                return self.weight, self.height
            else:
                self.weight += 3
                self.height += 6
                return self.growth(current_age + 1)

    def get_family_status(self):
        if self.age>=18 and self.spouse!=None and self.spouse!="":
            if self.gender == "Женский пол":
                self.family_status= "Замужем"
            else:
                self.family_status= "Женат"
        elif self.age < 18 or self.spouse == None or self.spouse == "" :
            if self.gender == "Женский пол":
                self.family_status= " Не замужем"
            else:
                self.family_status= "Не женат"
        return self.family_status     
    
    def work(self):
        if self.age>= 18:
            self.work_status = "Трудоустроен"
        elif self.age < 18:
            self.work_status = "Не трудоустроен"
        return self.work_status
    
    def get_description (self):
        if self.age <= 12:
            age_status = "Ребенок"
        elif self.age > 12 and self.age <= 18:
            age_status = "Подросток" 
        elif self.age > 18 and self.age <= 30:
            if self.gender == "Женский пол":
                age_status = "Девушка"
            elif self.gender == "Мужской пол":
                age_status = "Юноша"
        elif self.age > 30:
            if self.gender == "Женский пол":
                age_status = "Женщина"
            elif self.gender == "Мужской пол":
                age_status = "Мужчина"
        
        description = """%s:
        Имя: %s;
        Возраст: %i л.;
        Дата рождения: %i-%02i-%02i;
        Место рождения: %s;
        Рост: %i;
        Вес: %i; 
        Семейное положение: %s;
        Наличие работы: %s.
        """ %(age_status,self.name,self.age,self.birth_year,self.birth_month,self.birth_date, self.birth_place, self.height, self.weight, self.family_status, self.work_status)
        return description
  
person1=Human("Цирилла", "Женский пол", "Цинтра", "")
person1.birth()
person1.growth()
person1.get_age()
person1.get_family_status()
person1.work()
print(person1.get_description())

person2=Human("Геральт", "Мужской пол", "Ривия", "Йенифер")
person2.birth()
person2.growth()
person2.get_age()
person2.get_family_status()
person2.work()
print(person2.get_description())

person3=Human("Йенифер", "Женский пол", "Венгерберг", "Геральт")
person3.birth()
person3.growth()
person3.get_age()
person3.get_family_status()
person3.work()
print(person3.get_description())

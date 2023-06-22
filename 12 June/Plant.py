class Plant:
    name = ""
    health = 0
    petal_count = None
    irrigation_norm = 0
    soil_moisture = 0
    soil_moisture_norm = 0

    def __init__(self,name,health,petal_count,irrigation_norm,soil_moisture_norm, soil_moisture = 0):
        self.name = name
        self.health = health
        self.petal_count = petal_count
        self.irrigation_norm = irrigation_norm
        self.soil_moisture = soil_moisture
        self.soil_moisture_norm = soil_moisture_norm

    def irrigation(self, water):
        if water < (self.irrigation_norm/2):
           self.soil_moisture += (water * 0.2) 
        elif water > (self.irrigation_norm/2) and water < self.irrigation_norm:
           self.soil_moisture += (water * 0.3) 
        elif water >= self.irrigation_norm:
           self.soil_moisture += (water * 0.5)
        return self.soil_moisture
    
    def fade(self):
        num_soil_moisture_norm = (self.irrigation_norm * 100) / 60
        if self.soil_moisture < num_soil_moisture_norm:
            self.health -= 30
            if self.health > 0:
                result = f"Уровень здоровья растения - {self.health} %"
            else:
                self.health = 0
                result = f"Уровень здоровья растения - {self.health}%. Растение умерло."
        elif self.soil_moisture > num_soil_moisture_norm:
            self.health -= 12
            if self.health > 0:
                result = f"Уровень здоровья растения - {self.health} %"
            else:
                self.health = 0
                result = f"Уровень здоровья растения - {self.health}%. Растение умерло."
        elif self.soil_moisture== num_soil_moisture_norm:
            self.health == 100
            result = f"Уровень здоровья растения - {self.health}%. Растение чувствует себя прекрасно."
        return result
    
    def is_he_love(self):
        if self.petal_count > 0:
            start = input("Начать счет с 'любит' или 'не любит'? ")
            loves = start == "любит"
            for i in range(self.petal_count):
                loves = not loves
                if loves:
                    result = "Любит"
                else:
                    result = "Не любит"       
        else:
            result = "Возьмите растение с цветком и лепестками"
        return result
    
    def photosynthesis(self, sunlight, water):
        if sunlight and water:
            result = f"{self.name} проводит фотосинтез"
        else:
            result = f"{self.name} не может провести фотосинтез без солнечного света и воды"   
        return result
        

 
# rose = Plant("Роза", 100, 11, 400, 600) 
# print(f"Почва увлажнена на {rose.irrigation(500)} мл")
# print(f"Сосотояние растения оценивается как {rose.fade()}%")
# print(rose.is_he_love())
# print(rose.photosynthesis("Солнце светит", 500))

# lopuh = Plant("Лопух", 80, 0, 200, 100) 
# print(f"Почва увлажнена на {lopuh.irrigation(150)} мл")
# print(f"Сосотояние растения оценивается как {lopuh.fade()}%")
# print(lopuh.is_he_love())
# print(lopuh.photosynthesis(None, 150))
    
ficus = Plant("Фикус", 20, 0, 400, 500) 
print(f"Почва увлажнена на {ficus.irrigation(150)} мл")
print(ficus.fade())
print(ficus.is_he_love())
print(ficus.photosynthesis(None, 150))


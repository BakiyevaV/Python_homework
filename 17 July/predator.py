class Animal():
    def __init__(self, name, size, weight):
        self.name = name
        self.size = size
        self.weight = weight


    def talk(self, word):
        word_len = len(word)
        animal_word = word_len * "m"
        animal_word = animal_word.capitalize()
        print(f"{animal_word}...")
    
    def eat(self, meal):
        l = len(meal)
        self.size += (l * 0.2)
        self.weight += (l * 0.3)
        print(f"Я покушал и вырос на {round(l * 0.2, 1)} cм. и сейчас моя величина - {self.size}.\nМой вес увеличился на {round(l * 0.3, 1)} кг. и составляет {self.weight} кг.")
        
class Herbivore(Animal):
    def __init__(self):
        super().__init__(name, size, weight)
        self.ratio = ["трава", "фрукты", "ягоды", "листва", "растения", "кустарник"]


class Predator(Animal):
    def __init__(self):
        super().__init__("Лев", 240, 190)
        self.eated_meal = []

    def eat(self, meal):
        if isinstance(meal, Animal) or isinstance(meal, Herbivore):
            if meal in self.eated_meal:
                print("Я уже съел это животное!")
            else:
                if meal.size > self.size and meal.weight > self.weight:
                    print("Я могу есть животных только меньше меня!")
                else: 
                    self.size += meal.size * 0.2
                    self.weight += meal.weight * 0.2
                    self.eated_meal.append(meal)
                    print(f"Я покушал и вырос на {round(meal.size * 0.2, 1)} cм. и сейчас моя величина - {self.size}.\nМой вес увеличился на {round(meal.weight * 0.2, 1)} кг. и составляет {self.weight} кг.")
        else:
            print("Я могу есть только других животных!")

antelope = Animal("Антилопа", 130, 120)
zebra = Animal("Зебра", 150, 180)
leo = Predator()
leo.eat(antelope)
leo.eat(antelope)
leo.eat(zebra)



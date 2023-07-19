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
        super().__init__("Корова", 120, 650 )
        self.ratio = ["трава", "фрукты", "ягоды", "листва", "растения", "кустарник"]

    def eat(self, meal):
        if meal in self.ratio:
            super().eat(meal)
            return True
        else:
            print(f"Я такое не ем. Мой рацион состоит из {self.ratio}")
            return False

            
cow = Herbivore()
cow.eat("листва")


 

        

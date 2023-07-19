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
    def __init__(self, name, size, weight):
        super().__init__(name, size, weight)
        self.ratio = ["трава", "фрукты", "ягоды", "листва", "растения", "кустарник"]

    def eat(self, meal):
        if meal in self.ratio:
            super().eat(meal)
            return True
        else:
            print(f"Я такое не ем. Мой рацион состоит из {self.ratio}")
            return False

class Goose(Herbivore):
    def __init__(self,name,size,weight):
        super().__init__(name,size,weight)
        self.eggs = 0
    
    def talk(self, word):
        word_len = len(word)
        animal_word = word_len * "га"
        animal_word = animal_word.capitalize()
        print(f"{animal_word}...")
    
    def give_egg(self,stat):
        if stat == True:
            self.eggs += 1
            print(f"Я снесла яйцо. Теперь их {self.eggs}")
        else:
            self.eggs = self.eggs
            print(f"Я не покушала. Яйца не снесла.")



goose1 = Goose("Гага", 70, 3)
goose1.talk("привет")
stat = goose1.eat("камни")
goose1.give_egg(stat)
stat = goose1.eat("трава")
goose1.give_egg(stat)

strng = 50 * "-"
print(f"{(strng).center(100)}")

goose2 = Goose("Гиги", 50, 2)
goose2.talk("и тебе привет")
stat = goose2.eat("ягоды")
goose2.give_egg(stat)

strng = 50 * "-"
print(f"{(strng).center(100)}")

goose3 = Goose("Гога", 60, 2.5)
goose3.talk("хочу есть")







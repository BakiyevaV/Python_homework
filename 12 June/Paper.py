class Paper:
    def __init__(self, color, width, height, condition, fullness = 0):
        self.color = color
        self.width = width
        self.height = height
        self.condition = condition
        self.fullness = fullness
       

    def write(self, sign_count):
        capacity = ((self.width * self.height) * 10) / 6
        self.fullness = (sign_count / capacity) * 100
        if sign_count > capacity:
            result = "На листе не поместилось такое кол-во знаков!"
        elif sign_count == capacity:
            result = "Лист заполнен на 100%"
        elif sign_count < capacity:
            result = f"Лист заполнен на {self.fullness:.2f}%. Написано {sign_count} знаков"
        return result

    def figure_cut(self, figure_square, figure_name):
        square = self.height * self.width
        figure_count = square // figure_square
        if figure_count < 1:
            result = f"Из данного листа нельзя вырезать заявленную вами фигуру типа {figure_name} "
        else:
            result = f"Из данного листа можно вырезать {figure_count} фигур типа {figure_name}"
        return result

    def wrinkle (self,wrinkle_count):
        for i in range (0,wrinkle_count):
            self.condition -= 10
            if self.condition <= 0:
                self.condition =0
                result = f"Лист смят {wrinkle_count} раз. Визуальное состояние листа оценивается как 'Неудовлетворительное'"
            elif self.condition > 0 and self.condition < 50:
                result = f"Лист смят {wrinkle_count} раз. Визуальное состояние листа оценивается как 'Средней паршивости'"
            elif self.condition >= 50 and self.condition <= 80:
                result = f"Лист смят {wrinkle_count} раз. Визуальное состояние листа оценивается как 'Удовлетворительное'"
            elif self.condition > 80:
                result = f"Лист смят {wrinkle_count} раз. Визуальное состояние листа оценивается как 'Хорошее'"
        return result
     
    def recolor(self,new_color):
        self.color = new_color
        result  = f"Обновленный цвет - {self.color}"
        return result
    
# paper1 = Paper("Белый" , 36, 25, 100)
# print (paper1.write(1000))
# print (paper1.figure_cut(12, "Прямоугольник"))
# print (paper1.wrinkle (22))
# print (paper1.recolor("Синий"))

# paper2 = Paper("Красный" , 12, 8, 80)
# print (paper2.write(200))
# print (paper2.figure_cut(5, "Круг"))
# print (paper2.wrinkle (5))
# print (paper2.recolor("Черный"))

paper3 = Paper("Желтый" ,44 , 38, 50)
print (paper3.write(1000))
print (paper3.figure_cut(2000, "Квадрат"))
print (paper3.wrinkle (2))
print (paper3.recolor("Белый"))


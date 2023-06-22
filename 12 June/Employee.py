class Employee:
    def __init__(self, name, position, start_day, start_month,start_year, work_days_sum=0, absence_days_sum=0, attendance=True,
                 day_salary=0, balance=0, vacation_days = 0,work_day = 0, work_month = 0 ,work_year = 0,com_days_num = 0):
        self.name = name
        self.position = position
        self.work_days_sum = work_days_sum
        self.absence_days_sum = absence_days_sum
        self.attendance = attendance
        self.day_salary = day_salary
        self.start_day = start_day
        self.start_month = start_month
        self.balance = balance
        self.vacation_days = vacation_days
        self.start_year = start_year
        self.work_day = start_day
        self.work_month = start_month
        self.work_year = start_year
        self.com_days_num = work_day

    

    def go_work(self):
        if self.attendance in ["yes", "да", "д"]:
            self.work_day += 1
            self.work_days_sum += 1
            self.com_days_num += 1
            self.earn()
            if self.work_day > 30:
                self.work_day = 1
                self.work_month += 1
                if self.work_month > 12:
                    self.work_month = 1
                    self.work_year += 1
        elif self.attendance in ["no", "нет", "н"]:
            self.absence_days_sum += 1
            self.work_day += 1
            self.com_days_num += 1
            if self.work_day > 30:
                self.work_day = 1
                self.work_month += 1
                if self.work_month > 12:
                    self.work_month = 1
                    self.work_year += 1


        return self.work_days_sum, self.absence_days_sum, self.work_day, self.work_month, self.work_year, self.com_days_num

    def earn(self):
        if self.position == "Специалист":
            salary = 42500
            self.day_salary = salary / 20
            self.balance += self.day_salary
        elif self.position == "Ведущий специалист":
            salary = 46000
            self.day_salary = salary / 20
            self.balance += self.day_salary
        elif self.position == "Главный специалист":
            salary = 50000
            self.day_salary = salary / 20
            self.balance += self.day_salary
        return self.balance
    
    def vacation(self):
        self.vacation_days = self.com_days_num // 30
        return self.vacation_days *2
    
    def quit(self):
        self.quit_date = input ("Какого числа он уволился?Введите значение через '-':")
        self.quit_day, self.quit_month, self.quit_year = map(int,self.quit_date.split('-'))
    

    def get_info(self):
        info = """Сотрудник: %s\ 
        Должность: %s;\ 
        Дата начала работы: %02i-%02i-%i г.;\ 
        Дата увольнения: %02i-%02i-%i г;
        Трудовой стаж %i дней;
        Кол-во дней присутствия на работе %i дней;\ 
        Сумма полученной заработной платы за весь период работы:%i\ 
        Накопленные дни отпуска за весь период работы:%i"""%(self.name,self.position,
        self.start_day,self.start_month,self.start_year,self.quit_day,self.quit_month,
        self.quit_year, self.work_days_sum, employee1.com_days_num, self.balance,
        self.vacation_days)
        return info




employee1 = Employee("Виктория", "Главный специалист", 1, 6, 2019)
employee2 = Employee("Морти", "Специалист", 13, 2, 2023)
employee3 = Employee("Рик", "Ведущий специалист", 1, 7, 2022)
# while True:
#     employee1.attendance = input("Сотрудник: %s был на работе %02i:%02i:%i?: " % (employee1.name,employee1.work_day, employee1.work_month, employee1.work_year))
#     employee1.go_work()
#     print("Выплачена дневная заработная плата в размере %i. Баланс: %i"%(employee1.day_salary, employee1.balance) )
#     print("Общее кол-во дней с момента трудоустройства:",employee1.com_days_num)
#     print("Количество дней фактической работы:",employee1.work_days_sum)
#     if employee1.absence_days_sum > 2:
#         answer = input("Сотрудник уволился??: ")
        
#         if answer in ["yes", "да", "д"]:
#             employee1.quit()
#             print(f"Печально. Вот сводная информация по сoтруднику{employee1.name}:{employee1.get_info()}")
#             break
#         elif answer in ["no", "нет", "н"]:
#             continue

# while True:
#     employee2.attendance = input("Сотрудник: %s был на работе %02i-%02i-%i?: " % (employee2.name,employee2.work_day, employee2.work_month, employee2.work_year))
#     employee2.go_work()
#     employee2.vacation()
#     print("Выплачена дневная заработная плата в размере %i. Баланс: %i"%(employee2.day_salary, employee2.balance) )
#     print("Общее кол-во дней с момента трудоустройства:",employee2.com_days_num)
#     print("Количество дней фактической работы:",employee2.work_days_sum)
#     if employee2.absence_days_sum > 2:
#         answer = input("Сотрудник уволился??: ")
#         if answer in ["yes", "да", "д"]:
#             employee2.quit()
#             print(f"Печально. Вот сводная информация по сoтруднику{employee2.name}:{employee2.get_info()}")
#             break
#         elif answer in ["no", "нет", "н"]:
#             continue
 

while True:
    employee3.attendance = input("Сотрудник: %s был на работе %02i-%02i-%i?: " % (employee3.name,employee3.work_day, employee3.work_month, employee3.work_year))
    employee3.go_work()
    employee3.vacation()
    print("Выплачена дневная заработная плата в размере %i. Баланс: %i"%(employee3.day_salary, employee3.balance) )
    print("Общее кол-во дней с момента трудоустройства:",employee3.com_days_num)
    print("Количество дней фактической работы:",employee3.work_days_sum)
    if employee3.absence_days_sum > 2:
        answer = input("Сотрудник уволился??: ")
        if answer in ["yes", "да", "д"]:
            employee3.quit()
            print(f"Печально. Вот сводная информация по сoтруднику {employee3.name}:{employee3.get_info()}")
            break
        elif answer in ["no", "нет", "н"]:
            continue


from logger import *

def get_average(log, student, *marks, **kwargs):
    marks = list(marks)
    summ = 0
    calc = 0
    log.log_t(f"Отрабатывается функция: {get_average.__name__}, рассчитывающая средний балл студента. Студент: {student}",**kwargs)
    if len(marks) == 0:
        log.log_t(f"Проверка наличия данных для расчета", **kwargs)
        log.log_e(f"Ошибка! Отсутствуют данные для расчета", **kwargs)
        return False
    else:
        log.log_t(f"Верификация типа данных", **kwargs)
        for mark in marks:
            log.log_d("Оценка: ", mark, **kwargs)
            t = type(mark)
            if t != int:
                log.log_e(f"Ошибка! Имеются Данные неподходящего типа!{mark}", **kwargs)
                return False
        else:
            if len(marks) < 4:
                log.log_t(f"Проверка колличества объектов для расчета!", **kwargs)
                log.log_d("Длина: ", len(marks),**kwargs)
                log.log_w(f"Ошибка! У студента должно быть не менее 4 оценок! Вместо отсутствующего числа, будет использоваться - 0", **kwargs)
                while len(marks) < 4:
                    marks.append(0) 
                log.log_t("Расчет средней оценки!",**kwargs)
                for i in range(len(marks)):
                    log.log_d("Оценка: ",marks[i], **kwargs)
                    summ += marks[i]
                    calc += 1
                aver = round((summ / len(marks)), 1)
                log.log_i(f"Вычисление закончено! Студент: {student}, Средняя оценка: {aver}, Число итераций: {calc}",**kwargs)   
                return True 


log1 = Logger(Logger.ERROR, file='logs.log')
log1.set_log_level(log1.TRACE) 
get_average(log1,"Виктория", 12,11,10, sep = " ~ ") 

log2 = Logger(Logger.ERROR, file='somefile.txt', stdout = False)
get_average(log2,"Кирилл", sep = " ~ ") 

# VN: обычно в приложении создаётся только один экземпляр логгера, и он является глобальным, т.е. все другие
# классы и функции могут его использовать и им для этого не нужно его передавать в качестве аргумента.
# Это значит, что функция будет иметь следующий вид: get_average(student, *marks) или get_average(student, mark_list).
# И, кстати, судя по названию, она должна возвращать средний балл студента в качестве результата.

        
        

        



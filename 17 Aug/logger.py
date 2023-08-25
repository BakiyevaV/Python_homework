import datetime

class Logger:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ["[E] ", "[W] ", "[I] ", "[D] ", "[T] "]
    
    def __init__(self, level, file=None, stdout=True):
        self.stdout = stdout
        self.file = file
        self.current_log_level = level

    def set_log_level(self, level):
        self.current_log_level = level
        # VN: здесь не хватает проверки level на допустимый диапазон


    def log_prnt_write(self,color,lvl, *args, **kwargs):
        for k in kwargs:
            val = kwargs[k] 
        # после этого цикла val указывает на значение последнего ключа, а ключ может быть любым 
        args_str = ' '.join(map(str, args))
        if lvl <= self.current_log_level:
            if self.stdout == True:
                print(color,Logger.names[lvl], datetime.datetime.now(),*args,**kwargs )
                # VN: ^^^^^ всё хорошо, но в конце строки нужно сбрасывать цвет в default - для этого есть специальная escape-последовательность
            if self.file != None: 
                with open(f"{self.file}", "a", encoding='utf-8') as file:
                # VN: этот open нужно оборачивать в try, т.к. если такого файла нет, будет исключение
                    file.write(f"{str(val)}{Logger.names[lvl]}{str(val)}{datetime.datetime.now()}{str(val)}{args_str}\n")

    def log_e(self,*args, **kwargs):
        self.log_prnt_write("\033[31m",Logger.ERROR, *args, **kwargs)
        # VN: эти константы ^^^^^^^^^^ лучше определить в начале класса в виде переменных или словаря,
        # например: colors = {'red': "\033[31m", ...}, и тогда вызовы станут понятнее: 
        # self.log_prnt_write(self.colors['red'], Logger.ERROR, ...

    def log_w(self,*args, **kwargs):
        self.log_prnt_write("\033[33m",Logger.WARNING, *args, **kwargs)

    def log_i(self,*args, **kwargs):
        self.log_prnt_write("\033[32m",Logger.INFO, *args, **kwargs)

    def log_d(self,*args, **kwargs):
        self.log_prnt_write("\033[37m",Logger.DEBUG, *args, **kwargs)

    def log_t(self,*args,**kwargs):
        self.log_prnt_write("\033[34m",Logger.TRACE, *args, **kwargs)


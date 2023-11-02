import datetime


class Logger:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ["[E] ", "[W] ", "[I] ", "[D] ", "[T] "]

    def __new__(cls, level, file=None, stdout=True):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            cls.instance.__init__(level, file, stdout)
        return cls.instance

    def __init__(self, level, file=None, stdout=True):
        self.stdout = stdout
        self.file = file
        self.current_log_level = level

    def set_log_level(self, level):
        self.current_log_level = level

    def log_prnt_write(self, color, lvl, *args, **kwargs):
        # for k in kwargs:
        #     val = kwargs[k]  
        args_str = ' '.join(map(str, args))
        if lvl <= self.current_log_level:
            if self.stdout == True:
                print(color, Logger.names[lvl], datetime.datetime.now(), *args, **kwargs)
            if self.file != None:
                with open(f"{self.file}", "a", encoding='utf-8') as file:
                    file.write(f"{Logger.names[lvl]}{datetime.datetime.now()}{args_str}\n")

    def e(self, *args, **kwargs):
        self.log_prnt_write("\033[31m", Logger.ERROR, *args, **kwargs)

    def w(self, *args, **kwargs):
        self.log_prnt_write("\033[33m", Logger.WARNING, *args, **kwargs)

    def i(self, *args, **kwargs):
        self.log_prnt_write("\033[32m", Logger.INFO, *args, **kwargs)

    def d(self, *args, **kwargs):
        self.log_prnt_write("\033[37m", Logger.DEBUG, *args, **kwargs)

    def t(self, *args, **kwargs):
        self.log_prnt_write("\033[34m", Logger.TRACE, *args, **kwargs)


log = Logger(Logger.TRACE)

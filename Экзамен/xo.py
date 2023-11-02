from app import XoApplication
import sys

if __name__ == "__main__":
    args = sys.argv
    print(args)
    size = 3
    if len(args) == 1:
        app = XoApplication(size)
    elif len(args) == 2:
        app = XoApplication(size, hostname = args[1])
    elif len(args) == 3:
        app = XoApplication(size, mode =  args[1], char = args[2])
    elif len(args) == 4:
        app = XoApplication(size, mode =  args[1], char = args[2], hostname = args[3])
    app.start()

    

num = 32
strings = 0

while num <= 126 and num >= 32:
    strings += 1 
    sym = chr (num)
    num +=1
    if strings % 6 == 0:
        print("")
        continue
    print(f"Номеру -{num - 1} соответствует -{sym}")
        
    
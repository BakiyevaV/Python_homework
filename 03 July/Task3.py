def divide_into_syllables(word):
    vowels = 'аеёиоуыэюя'
    sonorant_consonants = 'лмнр'
    syllables = []
    current_syllable = '' 
    vol_count = 0
    for letter in word:
        if letter in vowels:
            vol_count +=1
    
    if vol_count ==  1:
        current_syllable = word
        syllables.append(current_syllable)
    else:
        for i, letter in enumerate(word): 
            current_syllable += letter 
            
            # VN: например, в слове "творог", последняя буква "г" не проходит проверку in vovels, а поскольку
            # гласных больше нет, то эта буква выкидывается, и результат получается ['тво','ро'].
            # Тут нужно ещё условие: если длина syllables уже равна количеству гласных, то оставшиеся буквы 
            # просто приписываются к последнему слогу
            if letter.lower() in vowels: 
                if i < len(word) - 1 and letter.lower() in sonorant_consonants and not word[i + 1].lower() in vowels: 
                    continue 
                    
                syllables.append(current_syllable) 
                current_syllable = ''
    
    return syllables

word = input("Введите слово: ") 
syllables = divide_into_syllables(word) 
print('-'.join(syllables)) 
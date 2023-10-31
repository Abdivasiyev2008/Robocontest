def omadli_chipta(chipta):
    # chiptadagi raqamni stringga aylantiramiz
    chipta_str = str(chipta)
    
    # barcha raqamlarni alohida listga yozamiz
    raqamlar = [int(i) for i in chipta_str]

    
    # raqamlar orasida o'ngdan chapga o'tishni tekshiramiz
    for i in range(1, len(raqamlar)):
        if raqamlar[i] == 3 and raqamlar[i-1] == 1:
            return "omadsiz chipta"
        
    return "omadli chipta"


print(omadli_chipta(int(input())))

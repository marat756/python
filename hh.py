try:
    
    if  login == maratt and parol == 4444:
        print("tabriklaymiz : ")
    elif login != maratt and parol == 4444:
        a = 0
        print("siz xato molumot krittingiz: ")
        while a < 60:
            a += 1 
            time.sleep(1)
            print(a) 
    elif login == maratt and parol != 4444:
        a = 0
        print("siz xato molumot krittingiz: ")
        while a < 60:
            a += 1 
            time.sleep(1)
            print(a) 
except ValueError:
    print("siz nonogri qimat kritingiz: ")

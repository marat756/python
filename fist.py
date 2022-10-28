import time 

tanlov = input("kodni kritinng: ")


if tanlov == 4444:
    print("tabriklaymiz : ")
     
else:
    a = 0
    print("siz xato molumot krittingiz: ")
    while a < 60:
        a += 1 
        time.sleep(1)
        print(a)

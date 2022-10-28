a = input(" mersedes cevrolet bmb ustozjon sizga qaysi brend kerak?: ")

list2 ={
    "a": ["mersedes benz s class","h25000$","mersedes benz c class","22000$"]
} 
list3 ={
    "d": ["cevrolet nexia3 ","7000$","cevrolet laseti","7200"]
}
list4 = {
    "u": ["bmb m9 4x4","45000$"]
}

if  a.lower() == "mersedes":
    print(list2["a"],["g"])
elif a.lower() == "cevrolet":
    print(list3["d"], ["s"])
   
elif a.lower() == "bmw":
    print(list4["u"])


else:
    print("xato")
    


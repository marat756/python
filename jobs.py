isim = input("isimni kiriting: ")
famila = input("familani kriting: ")
yetkazish = input("yetkazish manzili")
tolov = input("tolov usili: ")
boglanish = input("telefon nomer: ")


if isim == 'marat':
    print ("tanlouvingiz uchun raxmat: ")
elif isim != 'marat' and famila == 'tagaev' and yetkazish == 'home' and tolov == 'naxt' and boglanish == '1212':
    print ("isim xato: ")
elif isim == 'marat' and famila != 'tagaev' and yetkazish == 'home' and tolov == 'naxt' and boglanish == '1212':
    print ("famila xato: ")
elif isim == 'marat' and famila == 'tagaev' and yetkazish != 'home' and tolov == 'naxt' and boglanish == '1212':
    print ("yetkazish xato: ")
elif isim == 'marat' and famila == 'tagaev' and yetkazish == 'home' and tolov != 'naxt' and boglanish == '1212':
    print ("tolov xato: ")
elif isim == 'marat' and famila =='tagatv' and yetkazish == 'home' and tolov == 'naxt' and boglanish != '1212':
    print ("boglanish xato:")
else:
    print ("xato")
 
"""
 22.10.2025
  Pytonda royhatlar (List)

 """
  # ism = 'Dilmurod'
  # ism = 'Sultonbek'

 # print(ism)


#isimlar = ['Sultonbek,Humoyun, Zafarbek,Dilmurod']
#              0        1        2        3
#             -4       -3       -2       -1
#  print(isimlar)


#mevalar = ['olma','banan', 'nok','uzum','anor','behi','orik','gilos','mandarin']
moshinalar = ['bmw','depal','lambargini','audi','tesla','kia','toyota']


#print(moshinalar)
#print(moshinalar[1])
# print(mevalar[6].capitalize())
# print(mevalar[3].upper())
# print(isimlar[-1].lower())

# hayvonlar = []
# print(hayvonlar)

# hayvonlar.append("ot")
# print(hayvonlar)

# hayvonlar.append("yolbars")
# print(hayvonlar)

# hayvonlar.append("sher")
# print(hayvonlar)

# hayvonlar.append("baliq")
# print(hayvonlar)

# hayvonlar.append("kuchuk")
# print(hayvonlar)

# hayvonlar.append(" ayiq")
# print(hayvonlar)

# hayvonlar.append("kuchuk")
# print(hayvonlar)

# hayvonlar.append("xoroz")
# print(hayvonlar)

# hayvonlar.append("buqa")
# print(hayvonlar)

# hayvonlar.append("ilon")
# print(hayvonlar)

# hayvonlar.append("ordak")
# print(hayvonlar)

# hayvonlar.append("mushuk") # bu append() metodi royhatga qiymat qoshadi
# print(hayvonlar)

# hayvonlar.insert(1 , "buqa") # bu insert() metodi royhatda indeks yordamida qiymat qo'shadi
# print(hayvonlar)

# hayvonlar.insert(2 , "ordak")
# print(hayvonlar)

# hayvonlar.insert(4 , "ilon")
# print(hayvonlar)

moshinalar = ['bmw','depal','lambargini','audi','tesla','kia','toyota']
moshinalar.remove("tesla")
print(moshinalar)

moshinalar.remove("kia") #  remove() metodi royhatdan qiymat olib tashlaydi
print(moshinalar)

del moshinalar[2]
print(moshinalar) #  del[] tegi ham indeks yordamida ochiradi

del moshinalar[0]
print(moshinalar)

isimlar = ['sultonbek','humoyun']
print(isimlar[0])   # bu indeksdan malum bir qiymatni ajratib  oladi

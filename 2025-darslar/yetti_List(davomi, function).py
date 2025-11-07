"""
27.10.2025
Royhatning davomi methods, functions
methods(append(), insert(), remove(), pop(), sort(),,list(),max(),min(),sum(),range(),reversed(),tuple())

"""

davlatlar = ["O'zbekiston","Qozog'ston","Turkmaniston","Tojikistom","Rossiya","Xitoy","Latviya","Malayziya"]
uylar = list(("uy1","uy2","uy3","uy4","uy5","uy6","uy7","uy8","uy9","uy10"))

print(davlatlar)
print(uylar)

davlatlar.sort() # bu metod sozlarni bosh harfiga qarab alifbo ketma ketligida joylashtiradi
print(davlatlar)

print(sorted(davlatlar))  # sorted() funksiya bolib tartiblash uchun ishlatiladi
print(davlatlar)

sonlar = list(range(1,20))  # bu teg sonlarni ketma ket chiqarib beradi
print(sonlar)
juft_son = list(range(2,21,2)) # bunda juft sonlar chiqadi, oxiridagi ikki raqami qadamni bildiradi
print(juft_son)

toq_son = list(range(1,30,2))
print(toq_son)
print(len(toq_son)) # len() metodi royhat ichida nechta qiymat borligini sanab aytadi

sonlar = [1,2,-3,4,5,-6,7,8,9,-10]
print(f"Asl royhat : {sonlar}")
print(f"Eng kichik son : {max(sonlar)}") # bu max() tegi maxsimumini chiqaradi
print(f"Eng kichik son : {min(sonlar)}") # bu min()tegi minimumini chiqaradi
print(f"sonlar yigindisi : {sum(sonlar)}") # bu sum() tegi sonlarni hisoblab beradi
sonlar = list(range(-400,1003, 13))
print(len(sonlar))

davlatlar = ["O'zbekiston","Qozog'ston","Turkmaniston","Tojikistom","Rossiya","Xitoy","Latviya","Malayziya"] # bu opddiy royhat 
# tuple() oddiy royhatni o'zgarmas ro'yhatga aylantiradi

moshinalar = ['bmw','depal','lambargini','audi','tesla','kia','toyota'] # bu [] oddiy royhat
print(moshinalar)

moshinalar.remove("tesla")
print(moshinalar)
moshinalar.insert(0,"chevralet")  # bunda 0 indeksga qiymat qoshadi
print(moshinalar)
ranglar = ("qizil","qora","sariq","kok","yashil", "oq","pushti") # bu () o'zgarmas royhat buni hech nima qilib bolmaydi
print (ranglar)


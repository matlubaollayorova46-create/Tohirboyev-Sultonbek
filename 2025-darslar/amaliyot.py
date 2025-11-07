"""
         3.11.2025
           for loop da masalalar yechish
"""
# oquvchilar = ['sultonbek','humoyun','xursandbek','zafarbek']
# yillar = [14,15,20,16]

# for ism in oquvchilar:
#     print(f" Salom oquvchilar {ism.title()}")

# Amaliyot  
# 3-masala
# print("SHart bajarilsin (a<b)")
# a = int( input("a soniga butun qiymat kiriting :"))
# b = int( input("b soniga butun qiymat kiriting :"))
# sonlar = list(range(a,b+1))
# sonlar.sort(reverse=True)
# print(sonlar)
# print(f"Royhatdagi elementlar soni : {len(sonlar)}")

# 4-masala
# narxi = int(input("narxni kiriting :"))
# sonlar = list(range(1,11))
# for narx in sonlar:
#     print(f"siz",narx,"kg kanfet uchun",narx*narxi,"ming so'm tolaysiz")

# 5-masala
# narxi = int(input("kanfet narxini kiriting :"))

# for som in range(1,11):
#     naqd = som / 10
# print("sizni",naqd, "kg uchun to'laydigan pulingiz", naqd*narxi, "som boldi")

"""
5.11.2025

amaliyot ni takrorlash masalalar yechish

"""
# 7-masala
# a = int(input(" A soniga butun qiymat kiriting"))
# b =int(input(" B soniga butun qiymat kiriting"))

# # print(f"A sonining malumot tipi = {type(a)}")
# # print(f"B sonining malumot tipi = {type(b)}")

# sonlar = list(range(a,b+1))

# for s in sonlar :
#     print(f"{s} - sikl : {s}")
# print(f"Royhatning yigindisi : {sum(sonlar)}")

# 8- masala
# print("a<b")
# a = int(input(" A soniga butun qiymat kiriting"))
# b =int(input(" B soniga butun qiymat kiriting"))
# sonlar = list(range(a,b+1))
# print(f"Royhat : {sonlar} ")
# kopaytma = 1
# for s in sonlar :
#     kopaytma *= s
# print(f"Royhatning kopaytmasi : {kopaytma}")

# 10-masala

n = int(input("n soniga butun qiymat kiriting : "))

sonlar = list(range(1,n+1))

korinish = []
for son in sonlar : 
    i += f"1/{son}"
    korinish.append(i)
    i = 0
    yigindi += 1/son
print(korinish)
print(f"Yigindi : {yigindi}")
# c# taki Console.Readline bicimi burada "input" la yapiliyor.

greeting= "Hello"
name=input("Pleasae enter your name")
print(greeting + '' + name )
********************************************************************
tabbedString = "1\t2\t3\t4\t5"
#1	2	3	4	5
*********************************************************************
splitString = "This string has been \nsplit over\nseveral\nlines"
#split over
#several
#lines
**********************************************************************
# \ kendinden sonraki kelimeyi önceki kelimeyle birlestiriyor.
# \ karakter olarak kullanmak icin \\ veya cümle baina r yazilir.
notherString = """This string has been \
split over \
several 
lines"""
#This string has been split over several
#lines
***********************************************************************
#Bölme islemi
a=12
b=5
print(a/b)
print(a//b)   #tam sayi olarak bölüyor
#2.4
#2

**************************************************************************
#Stringlerde karakter yazdirma
#                   1
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6]) # 6nci karakter dahil degil
print(parrot[:6]+ parrot[6:]) # bastan degere kadar ve degerden sona kadar gider
print(parrot[:]) # start stop degeri yoksa bütün degerleri yazar                                          #
************************************************************************

print((parrot[0:6:2]))   # Nre  ilk 5 karakteri alir sonra 0,2,4 üncü karakterleri secer
print((parrot[0:6:3]))   # Nw    ilk 5 karakteri alir sonra 0,2,4 üncü karakterleri secer
print((parrot[::-1]))    # Degeri Tersten yazar

***********************************************************************
age = 24
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

*************************************************************************

age = 24
print(name+f"is {age} years old") # f koyunca print icinde integer degeri string olarak aliyor. C# daki $ isareti gibi.

**************************************************************************
## For döngüsünde baslangic elemani koyulmasada olur
for i in range (20):
      print(" i is now  {}".format((i)))



for i in range (0,20):
      print(" i is now  {}".format((i)))

## 10 da geriye dogru sayma

for i in range (10,0,-2):
      print(" i is now  {}".format((i)))
**************************************************************************
# While loops
i=0
while i<10 :
      print("i is now  {} ".format(i))
            i+=1

**************************************************************************

# Casefold kullanildi.Buna da arada bak!!!!!!!!!****
available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
      chosen_exit = input("Please choose a direction: ")
      if chosen_exit.casefold() == "quit":
            print("Game over")
            break

print("aren't you glad you got out of there")


**************************************************************************

































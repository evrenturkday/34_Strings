print("write a day:")
day = input ()
print("write a temperature:")
temperature = int(input())
raining= False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

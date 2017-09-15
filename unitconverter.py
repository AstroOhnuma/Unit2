#Astro Ohnuma
#9/14/17
#unitconverter.py - multiple unit conversions

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')
num = int(input('Which unit conversion would you like to use?: '))
if num==1:
    distance = float(input('Enter distance in Kilometers: '))
    print(distance,'kilometers is',distance*0.621371,'miles')
elif num==2:
    weight = float(input('Enter weight in Kilograms: '))
    print(weight,'kilograms is',weight*2.20462,'pounds')
elif num==3:
    liquid = float(input('Enter a volume of liquid in Liters: '))
    print(liquid,'liters is',liquid*0.264172,'gallons')
elif num==4:
    temperature = float(input('Enter Degrees in Celsius: '))
    print(temperature,'degrees Celsius is',(temperature*1.8)+(32),'degrees in Fahrenheit')

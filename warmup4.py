#Astro Ohnuma
#9/18/17
#warmup4.py - ask user for a number, print either number or buzz

num = int(input('Enter a number: '))

if '7' in str(num) or num%7 == 0:
    print('Buzz!')
else:
    print(num)


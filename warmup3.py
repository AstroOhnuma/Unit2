#Astro Ohnuma
#9/15/17
#warmup3.py - divisble by 3, 2, neither, or both

num = int(input('Enter a number: '))
if num%3 == 0 and num%2 == 0:
    print(num,'is divisible by both')
elif num%3 == 0:
    print(num,'is divisble by 3')
elif num%2 == 0:
    print(num,'is divisble by 2')
else:
    print(num,'is divisble by neither')


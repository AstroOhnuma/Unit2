#Astro Ohnuma
#9/15/17
#fortuneteller.py - picking a color and then a number and getting a fortune

color = input('Pick a color(red or blue): ')
number = int(input('Pick a number(1-4): '))
if color=='red' and number==1:
    print('You will be spooked by a ghost in your house')
elif color=='red' and number==2:
    print('You will fall into a river while crossing a bridge')
elif color=='red' and number==3:
    print('You will eat a delicious meal but it will actually be dirt')
elif color=='red' and number==4:
    print('You will find and befriend a rat in the sewers')
elif color=='blue' and number==1:
    print('You will be eaten by a fishman the next time you go to the beach')
elif color=='blue' and number==2:
    print('You will find and eat at a 5-star restaurant in the middle of the forest')
elif color=='blue' and number==3:
    print('You will get lost in the desert')
elif color=='blue' and number==4:
    print('You will fall in a well and wake up on the other side of the world')
else:
    print('no')
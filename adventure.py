#Astro Ohnuma
#9/18/17
#adventure.py - writing an interactable adventure

print('You are in a cave')
left = input('You come to a fork in the cave, do you go left?: ')
if left=='yes':
    print('You go left')
    print('You go downhill deeper into this part of the cave until you fall into a hole and die')
    quit
elif left=='no':
    right = input('Do you go right?: ')
    if right=='yes':
        print('You go right')
        print('You keep going forward until the tunnel opens up into an open area')
        rope = input('There is rope on the ground, do you take it?: ')
        if rope=='yes':
            


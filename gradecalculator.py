#Astro Ohnuma
#9/13/17
#gradecalculator.py - calculating a letter grade from percentages

grade = int(input('Input your grade: '))
if grade>92:
    print('You earned an A')
elif grade>89:
    print('You earned an A-')
elif grade>82:
    print('You earned a B')
elif grade>79:
    print('You earned a B-')
elif grade>72:
    print('You earned a C')
elif grade>69:
    print('You earned a C-')
elif grade>62:
    print('You earned a D')
elif grade>59:
    print('You earned a D-')
else:
    print('You earned an F')
    

#Astro Ohnuma
#9/13/17
#movie.py - getting age and finding out the most "scandalous" type of movie they can watch

age = int(input('Enter your age: '))
if age>17:
    print('You can watch NC-17 movies')
elif age>16:
    print('You can watch R rated movies')
elif age>12:
    print('You can watch PG-13 movies(and R rated movies with a parent/guardian)')
elif age<13:
    print('You can watch PG movies')

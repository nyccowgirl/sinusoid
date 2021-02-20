from math import sin, radians
import itertools

print(*map(lambda a: (' ' * (10 + a)) + ('*' * (-a)) if (a < 0) else (' ' * 10) + ('*' * a), map(lambda a: round(sin(radians(a)) * 10), itertools.chain(range(-180, 180, 10), range(-180, 180, 10)))), sep='\n')

"""
Code is similar to: 

for angle in range(-180, 180, 10):
    y = round(sin(radians(angle)) * 10)
    if (angle < 0):
        print((' ' * (10 + y)) + ('.' * (-y)))
    else:
        print((' ' * 10) + ('.' * y))

For one iteration as in the above for loop:

print(*map(lambda a: (' ' * (10 + a)) + ('.' * (-a)) if (a < 0) else (' ' * 10) + ('.' * a), map(lambda a: round(sin(radians(a)) * 10), range(-180, 180, 10))), sep='\n')

However, to iterate it a couple of times, intertools.chain was used.

Result:

        **
       ***
     *****
    ******
  ********
 *********
 *********
**********
**********
**********
 *********
 *********
  ********
    ******
     *****
       ***
        **
          
          **
          ***
          *****
          ******
          ********
          *********
          *********
          **********
          **********
          **********
          *********
          *********
          ********
          ******
          *****
          ***
          **
          
        **
       ***
     *****
    ******
  ********
 *********
 *********
**********
**********
**********
 *********
 *********
  ********
    ******
     *****
       ***
        **
          
          **
          ***
          *****
          ******
          ********
          *********
          *********
          **********
          **********
          **********
          *********
          *********
          ********
          ******
          *****
          ***
          **

"""


# def greet():
#   print('hello world')

# greet()

def greet(name, time):
  print(f'Good {time} {name}, hope you are well!')

name = input('enter your name')
time = input('enter the time of day')

greet (name, time)


## below using default parameters
def greet(name = 'lily', time = 'morning'):
  print(f'Good {time} {name}, hope you are well!')

greet ('lily', 'afternoon')
## the console would output good afternoon LILY because the arguments above override the default parameters

## finding the radius of a circle
# def area(radius):
#   print(3.14 * radius * radius)

# radius = int(input('enter a radius'))
# area(radius)

def area(radius):
  return(3.14 * radius * radius)


def vol(area, length):
  print(area * length)

radius = int(input('enter a radius'))
length =int(input('enter a length'))

vol(area(radius), length)

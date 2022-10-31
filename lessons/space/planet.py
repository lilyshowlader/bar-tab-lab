class Planet: 

  shape = 'round'
  def __init__(self):
    self.name = 'Hoth'
    self.radius = 20000
    self.gravity = 5.5
    self.system = 'Hoth System'
    ## above are propertiers

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'
  ## above is an example of a method

  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape} because of gravity'

  @staticmethod
  def spin(speed = '2000 miles per hour'):
    return f'The planet spins and spins at {speed}'

hoth = Planet()
print(f'Name is {hoth.name}')
print(f'Radius is {hoth.radius}')
print(f'the gravity is {hoth.gravity}')
print(hoth.orbit())



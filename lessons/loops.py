#FOR LOOPS
# pets = ['maya', 'maeby', 'mia', 'bao']


# for pet in pets:
#   print(pet)

# for pet in pets[1:3]:
#   print(pet)

# for pet in pets:
#   if pet == 'mia':
#     print(f'{pet} - is adorable')
#     break
#   else:
#     print(pet)

#WHILE LOOPS

age = 27
num = 0

#while the condition is true, the codeblock will run
while num < age:
  if num == 0:
    num += 1
    continue
  if num % 2 == 0:
    print(num)
  if num > 10:
    break
  num += 1

import random

spi = ['хороший', "очень хороший"]

main_data = ['Маша', 'Ян', 'Вася']
def pohvala(name):
    return name + " " + random.choice(spi)

names_with_characters = map(pohvala, main_data)

print(names_with_characters)
print(main_data)
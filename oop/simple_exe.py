from Car import Car

bmw = Car("bmw", 90, condey=True)
jigul = Car("vaz 2110", 110)

bmw.update_odometr(200)
bmw.increment_odometr(200, 3)
print(bmw.odometr)

bmw.cooling()
jigul.cooling()
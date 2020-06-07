def intro(**data):
    print("\nData type of argument: ", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(firstname = 'Petr', lastname = "Ivanov")
intro(firstname = 'Ivan', lastname = "Ivanov")

slovar = {'name': "Pavel", 'lastname': "Ivanov"}
intro(**slovar)
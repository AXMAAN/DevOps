def hello():
    name = input("What's your name? ")
    print(name)

    def world():
    hello()
    print("Hello world,", name)

    world()


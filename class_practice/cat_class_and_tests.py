class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.hunger = 50
        self.thirst = 50

    def meow(self):
        self.hunger = min(100, self.hunger + 10)
        return f"{self.name} says: Meow!"

    def play(self):
        self.thirst = min(100, self.thirst + 15)
        self.hunger = min(100, self.hunger + 5)
        return f"{self.name} is playing with a ball of yarn."

    def eat(self):
        self.hunger = max(0, self.hunger - 15)
        return f"{self.name}'s is eating"

    def drink(self):
        self.thirst = max(0, self.thirst - 20)
        return f"{self.name} is drinking"


    def info(self):
        return f"This is the cat named {self.name}.\nBreed = {self.breed}\nHunger = {self.hunger}\nThirst = {self.thirst}"

def test_meow():
    """
    Validate that the cat successfully meows with its name and hunger value is 60
    """
    cat = Cat("Red", breed="Bengal Cat")
    meow = cat.meow()
    expected_meow = f"{cat.name} says: Meow!"
    assert meow == expected_meow
    assert cat.hunger == 60

def test_play():
    """
    Validate that the cat successfully plays with its name, hunger value is 55 and thirst value is 65.
    """
    cat = Cat("Red", breed="Bengal Cat")
    play = cat.play()
    expected_play = f"{cat.name} is playing with a ball of yarn."
    assert play == expected_play
    assert cat.hunger == 55
    assert cat.thirst == 65

def test_eat():
    """
      Validate that the cat successfully eats with its name and hunger value is 35.
    """
    cat = Cat("Red", breed="Bengal Cat")
    eat = cat.eat()
    expected_eat = f"{cat.name}'s is eating"
    assert eat == expected_eat
    assert cat.hunger == 35

def test_drink():
    """
    Validate that the cat successfully drinks with its name and thirst value is 30.
    """
    cat = Cat("Red", breed="Bengal Cat")
    drink = cat.drink()
    expected_drink = f"{cat.name} is drinking"
    assert drink == expected_drink
    assert cat.thirst == 30

def test_start_info():
    """
    Validate that the info message contains cat's name, breed, hunger value is 50 and thirst value is 50.
    """
    cat = Cat("Red", breed="Bengal Cat")
    start_info = cat.info()
    expected_info = f"This is the cat named {cat.name}.\nBreed = {cat.breed}\nHunger = 50\nThirst = 50"
    assert start_info == expected_info

def test_end_info():
    """
    Validate that the info message contains cat's name, breed, hunger is 50 and thirst is 50.
    """
    cat = Cat("Red", breed="Bengal Cat")
    cat.meow()
    cat.play()
    cat.eat()
    cat.drink()
    expected_info = f"This is the cat named {cat.name}.\nBreed = {cat.breed}\nHunger = 50\nThirst = 45"
    assert cat.info() == expected_info

def test_min_hunger():
    """
    Validate that the min hunger value is 0.
    """
    cat = Cat("Red", breed="Bengal Cat")
    for food in range(4):
        cat.eat()
    hunger = cat.hunger
    assert cat.hunger == 0

def test_min_thirst():
    """
    Validate that the min thirst value is 0.
    """
    cat = Cat("Red", breed="Bengal Cat")
    for water in range(3):
        cat.drink()
    thirst = cat.thirst
    assert cat.thirst == 0

def test_max_hunger():
    """
    Validate that the max hunger value is 100.
    """
    cat = Cat("Red", breed="Bengal Cat")
    for voice in range(6):
        cat.meow()
    hunger = cat.hunger
    assert cat.hunger == 100

def test_max_thirst():
    """
    Validate that the max thirst value is 100.
    """
    cat = Cat("Red", breed="Bengal Cat")
    for water in range(4):
        cat.play()
    thirst = cat.thirst
    assert cat.thirst == 100
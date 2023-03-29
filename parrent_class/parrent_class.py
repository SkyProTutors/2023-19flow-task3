class Pine:

    def __init__(self, name):
        self.name = name
        self.lifetime = 30
        self.grow_speed = 1

    def calculate_max_height(self):
        return self.grow_speed*self.lifetime

    def __str__(self):
        return f"I'am Pine по имени {self.name} и смогу вырасти до {self.calculate_max_height()} метров"

class Rose:

    def __init__(self, name):
        self.name = name
        self.lifetime = 3
        self.grow_speed = 0.5

    def calculate_max_height(self):
        return self.grow_speed*self.lifetime

    def __str__(self):
        return f"I'am Rose по имени {self.name} и смогу вырасти до {self.calculate_max_height()} метров"


if __name__ == '__main__':
    pine = Pine("Лесная")
    print(pine)
    rose = Rose("Садовая")
    print(rose)

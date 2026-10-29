class GameCharacter:

    def __init__(self, name, health, level):

        self.name = name
        self.health = health
        self.level = level

    def show_details(self):

        print("Name:", self.name)
        print("Health:", self.health)
        print("Level:", self.level)

    def take_damage(self, damage):

        self.health = self.health - damage

        if self.health < 0:
            self.health = 0

        print(self.name, "health is now", self.health)


class Warrior(GameCharacter):

    def __init__(self, name, health, level, sword_power):

        super().__init__(name, health, level)

        self.sword_power = sword_power

    def sword_attack(self, opponent):

        print(self.name, "attacks", opponent.name, "with a sword!")

        opponent.take_damage(self.sword_power)


class Archer(GameCharacter):

    def __init__(self, name, health, level, arrow_power):

        super().__init__(name, health, level)

        self.arrow_power = arrow_power

    def arrow_attack(self, opponent):

        print(self.name, "attacks", opponent.name, "with an arrow!")

        opponent.take_damage(self.arrow_power)



class Wizard(GameCharacter):

    def __init__(self, name, health, level, magic_power):

        super().__init__(name, health, level)

        self.magic_power = magic_power

    def magic_attack(self, opponent):

        print(self.name, "attacks", opponent.name, "with magic!")

        opponent.take_damage(self.magic_power)
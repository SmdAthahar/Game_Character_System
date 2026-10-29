from character import Warrior, Archer, Wizard

warrior = Warrior("Thor", 100, 5, 20)

archer = Archer("Robin", 80, 4, 15)

wizard = Wizard("Merlin", 70, 6, 25)



print("==============================")
print("      GAME CHARACTERS")
print("==============================")

print()
print("Warrior Details")
warrior.show_details()

print()
print("Archer Details")
archer.show_details()

print()
print("Wizard Details")
wizard.show_details()



print()
print("==============================")
print("      CHARACTER BATTLE")
print("==============================")

warrior.sword_attack(archer)

archer.arrow_attack(wizard)

wizard.magic_attack(warrior)



print()
print("==============================")
print("      FINAL HEALTH")
print("==============================")

print(warrior.name, "Health:", warrior.health)

print(archer.name, "Health:", archer.health)

print(wizard.name, "Health:", wizard.health)

# Author: Yongdong Xi (Sep 30 2021)

magic_charge = float(input("What is magic charge?"))
shield_charge = float(input("What is shield charge?"))

if not ((magic_charge >= 90) and (shield_charge >= 75)):
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")

if not (magic_charge >= 90) or not (shield_charge >= 75):
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")

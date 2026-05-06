class GameCharacter:
    def __init__(self):
        # Private attributes (Encapsulation)
        self.__health = 100
        self.__energy = 50

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            return True
        else:
            print("Not enough energy!")
            return False

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0

    def get_status(self):
        return f"Health: {self.__health}, Energy: {self.__energy}"

    # Helper methods to allow subclasses to modify private data safely
    def _get_health(self):
        return self.__health

    def _set_health(self, value):
        self.__health = max(0, min(100, value))

    def _get_energy(self):
        return self.__energy

    def _set_energy(self, value):
        self.__energy = value


class Warrior(GameCharacter):
    def attack(self):
        # Use super() to call parent logic
        if super().attack():
            print("Warrior performs a heavy attack!")


class Mage(GameCharacter):
    def attack(self):
        # Override logic: Mages use more energy (20)
        current_energy = self._get_energy()
        if current_energy >= 20:
            self._set_energy(current_energy - 20)
            print("Mage casts a spell!")
        else:
            print("Not enough energy for spell!")

    def heal(self, amount):
        current_health = self._get_health()
        self._set_health(current_health + amount)


# --- Test Code ---
w = Warrior()
m = Mage()

w.attack()  # Uses 10 energy + warrior print
m.attack()  # Uses 20 energy + mage print

w.take_damage(30)
m.heal(20)  # Mage starts at 100, so this won't exceed 100

print(w.get_status())
print(m.get_status())

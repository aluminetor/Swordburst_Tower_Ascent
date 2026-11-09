import random
from entities.base_entity import Entity
class Player(Entity):
    def __init__(self,name: str, max_hp, power_attack, defend) -> None:
        super().__init__(name, max_hp, power_attack, defend)
        self._level = 1
        self._xp = 0
        self.__stamina = 100
        self.__max_stamina = 100
        self._inventory = []
        self._equipped_weapon = None

    def gain_xp(self, amount: int) -> None:
        self._xp += amount

    def equip_weapon(self,new_weapon):
        if self._equipped_weapon == None:
            self._equipped_weapon = new_weapon

    def __gt__(self, other):
        return self._equipped_weapon > other._equipped_weapon

    def __eq__(self, other):
        return self._equipped_weapon == other._equipped_weapon

    def _calculate_total_attack(self):
        total_attack = self.power_attack

        if self._equipped_weapon is not None:
            total_attack += self._equipped_weapon.get_bonus_damage()

        return total_attack

    def attack(self, target):
        return target.take_damage(self._calculate_total_attack())

    def get_stamina(self):
        return self.__stamina

    def consume_stamina(self, amount):
        if self.__stamina >= amount:
            self.__stamina = max(0, self.__stamina - amount)
            return True
        return False

    def recover_stamina(self,amount):
        self.__stamina = min(self.__max_stamina, self.__stamina + amount)


class DualWielder(Player):
    def __init__(self, name: str, max_hp, power_attack, defend) -> None:
        super().__init__(name, max_hp, power_attack, defend)
        self._offhand_weapon = None

    def equip_offhand_weapon(self, new_weapon):
        if self._offhand_weapon == None:
            self._offhand_weapon = new_weapon

    def starburst_stream(self, target):
        if not self.consume_stamina(20):
            return 0

        total_damage = target.take_damage(self._calculate_total_attack())

        if self._offhand_weapon is not None and target.is_alive():
            offhand_damage = self.power_attack + self._offhand_weapon.get_bonus_damage()
            total_damage += target.take_damage(int(offhand_damage * 0.7))

        return total_damage


class Paladin(Player):
    def __init__(self, name: str, max_hp, power_attack, defend) -> None:
        super().__init__(name, max_hp, power_attack, defend)
        self._defend += 10

    def take_damage(self, raw_damage):
        if random.random() < 0.5:
            raw_damage *= 0.5

        return super().take_damage(int(raw_damage))

    def holy_light(self):
        if not self.consume_stamina(20):
            return False

        self.heal(30)
        return True


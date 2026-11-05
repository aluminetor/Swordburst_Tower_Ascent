from entities.base_entity import Entity
class Player(Entity):
    def __init__(self,name: str, max_hp, power_attack, defend) -> None:
        super().__init__(name, max_hp, power_attack, defend)
        self._level = 1
        self.__stamina = 100
        self.__max_stamina = 100
        self._inventory = []
        self._equipped_weapon = None


    def equip_weapon(self,new_weapon):
        if self._equipped_weapon == None:
            self._equipped_weapon = new_weapon

    def __gt__(self, other):
        return self._equipped_weapon > other._equipped_weapon

    def __eq__(self, other):
        return self._equipped_weapon == other._equipped_weapon

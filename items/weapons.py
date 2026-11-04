from items.base_item import Item

class Sword(Item):
    def __init__(self, name:str, rarity:str, bonus_damage: int):
        super().__init__(name,rarity)
        self._bonus_damage = bonus_damage


    def get_bonus_damage(self):
        return self._bonus_damage
    
    def __str__(self):
        return f"[{self._rarity}] {self._name} (+{self._bonus_damage} ATK)"
        # Creación de una instancia
        #p = Persona("Lucía", 28)
    
    def __gt__(self, other):
        return self._bonus_damage > other._bonus_damage

    def __eq__(self, other):
        return self._bonus_damage == other._bonus_damage

    
from items.base_item import Item

class Potion(Item):
    def __init__(self, name:str, rarity: str, heal_amount):
        super().__init__(name,rarity)
        self.heal_amount = heal_amount
    
    def use(self,target) -> None:
        target.heal(self.heal_amount)

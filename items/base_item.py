
class Item():
    def __init__(self, name: str, rarity: str) -> None:
        # "Common", "Rare", "Legendary"
        self._name = name
        self._rarity = rarity

    def __str__(self):
        return f"[{self._name}] {self._rarity}"
        # Creación de una instancia
        #p = Persona("Lucía", 28)
    
    
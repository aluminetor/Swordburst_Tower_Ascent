
class Item():
    def __init__(self, name: str, rarity: str) -> None:
        self._name = name
        self._rarity = rarity

    def __str__(self):
        return f"[{self._name}] {self._rarity}"

    
    
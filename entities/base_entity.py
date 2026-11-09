
class Entity():
    def __init__(self, name: str, max_hp, power_attack, defend) -> None:
        self._name = name
        self.__max_health = max_hp
        self.power_attack = power_attack
        self._defend = defend
        self.__health = max_hp
    
    def get_health(self):
        return self.__health

    def get_max_hp(self) -> int:
        return self.__max_health

    def get_name(self):
        return self._name

    def is_alive(self) -> bool:
        return self.__health > 0

    def take_damage(self, damage: int) -> int:
        real_damage = max(0, damage - self._defend)
        self.__health = max(0, self.__health - real_damage)
        """Evaluación: max(0, -30) → 0 (la vida queda en 0, no en -30)."""
        return real_damage

    def attack(self, target):
        power = self.power_attack
        return target.take_damage(power)

    def heal(self,amount):
        self.__health = min(self.__max_health, self.__health + amount)
        return self.__health


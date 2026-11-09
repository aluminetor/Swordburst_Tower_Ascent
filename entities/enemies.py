import random
from typing import Optional

from entities.base_entity import Entity
from items.base_item import Item


class Enemy(Entity):
    def __init__(
        self,
        name: str,
        max_hp: int,
        attack_power: int,
        defense: int,
        xp_reward: int,
        loot_table: Optional[list[Item]] = None,
    ) -> None:
        super().__init__(name, max_hp, attack_power, defense)
        self._xp_reward = xp_reward
        self._loot_table = [] if loot_table is None else loot_table

    def drop_loot(self) -> Optional[Item]:
        if not self._loot_table:
            return None

        if random.randint(1, 100) <= 50:
            return random.choice(self._loot_table)

        return None

    def get_xp_reward(self) -> int:
        return self._xp_reward


class FloorBoss(Enemy):
    def __init__(
        self,
        name: str,
        max_hp: int,
        attack_power: int,
        defense: int,
        xp_reward: int,
        title: str,
        special_move_name: str,
        loot_table: Optional[list[Item]] = None,
    ) -> None:
        super().__init__(name, max_hp, attack_power, defense, xp_reward, loot_table)
        self._title = title
        self._special_move_name = special_move_name
        self._is_enraged = False

    def get_name(self) -> str:
        return f"[BOSS] {super().get_name()} - {self._title}"

    def take_damage(self, raw_damage: int) -> int:
        real_damage = super().take_damage(raw_damage)
        if self.is_alive():
            self._check_enrage()
        return real_damage

    def attack(self, target: Entity) -> int:
        if self._is_enraged and random.randint(1, 100) <= 35:
            print(f"¡{self.get_name()} usa {self._special_move_name}!")
            return target.take_damage(self.power_attack * 2)

        return super().attack(target)

    def drop_loot(self) -> Optional[Item]:
        if not self._loot_table:
            return None

        return random.choice(self._loot_table)

    def _check_enrage(self) -> None:
        if not self._is_enraged and self.get_health() <= self.get_max_hp() * 0.4:
            self._is_enraged = True
            self.power_attack = int(self.power_attack * 1.5)
            print(f"¡{self.get_name()} ruge y entra en modo berserk!")

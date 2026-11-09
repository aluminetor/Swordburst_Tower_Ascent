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
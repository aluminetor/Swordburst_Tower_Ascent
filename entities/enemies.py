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


    
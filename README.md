# Swordburst: Tower Ascent

Small Python combat simulation inspired by Swordburst. The project demonstrates
entities, playable classes, weapons, consumables, and turn-based combat. It has
no third-party dependencies and runs entirely in the terminal.

## Features

- Entity health, damage, defense, and healing model.
- Two playable classes: `DualWielder` and `Paladin`.
- Equipable swords with attack bonuses and comparison operators.
- Consumable potions that restore health.
- Turn-based combat demo with health bars and stamina costs.

## Requirements

- Python 3.9 or newer.
- No third-party packages.

## Run the simulation

```bash
python main.py
```

The output includes damage comparisons, two combat turns, health bars, weapon
stats, and potion healing.

## Combat mechanics

### Damage and defense

Every attack deals `max(0, raw_damage - defense)`. Health never drops below
zero, so defeated entities stay at `0` HP instead of negative values.

### Stamina

Player characters start with 100 stamina. Special abilities cost 20 stamina and
fail harmlessly when there is not enough left.

### Healing

Potions and abilities restore health up to the entity's maximum HP; overhealing
is discarded.

### Turn flow

`main.py` runs a scripted demo: a weapon damage comparison, two combat turns,
equipment inspection, and a potion use. `random.seed(1)` keeps the demo
repeatable across runs.

## Playable classes

All player classes inherit from `Player`, which extends `Entity` with stamina,
inventory, and an equipped weapon.

### Player

- Base HP, attack, and defense come from `Entity`.
- `attack(target)` adds the equipped weapon's bonus damage.
- Tracks stamina through `consume_stamina` and `recover_stamina`.

### DualWielder

- Can equip a second weapon in the off-hand slot.
- `starburst_stream(target)` costs 20 stamina: it lands a main-hand hit at full
  attack power, then an off-hand hit at 70% power if the target survives.

### Paladin

- Starts with 10 extra defense.
- Has a 50% chance to halve incoming damage.
- `holy_light()` costs 20 stamina and heals 30 HP.

## Items and equipment

### Swords

`Sword` stores a name, rarity, and bonus damage. `get_bonus_damage()` feeds into
player attacks, while `>` and `==` compare swords by bonus damage so equipment
strength can be checked directly.

### Potions

`Potion` is a consumable with a `heal_amount`. `use(target)` heals the target
without exceeding its maximum HP.

### Inventory

`Player` reserves an inventory list for future item management. Equipping is
currently limited to the main-hand and off-hand weapon slots.

## Project structure

- `main.py` - Scripted demo: damage comparison, combat turns, equipment, and
  potions.
- `entities/base_entity.py` - `Entity` base class with health, damage, defense,
  and healing.
- `entities/player.py` - `Player`, `DualWielder`, and `Paladin` classes.
- `items/base_item.py` - Shared `Item` base class.
- `items/weapons.py` - `Sword` equipment with attack bonuses.
- `items/consumables.py` - `Potion` consumables.

## Sample output

The script prints a banner for each section, for example:

```text
============ Swordburst Tower Ascent ============
============ Turno 1 ============
============ Turno 2 ============
============ Equipo y consumibles ============
```

## Roadmap

- Add a proper combat log for every damage roll.
- Introduce more enemy types and encounter waves.
- Implement inventory management and weapon swapping.
- Add automated tests for combat math and ability costs.
- Build tower progression with floors and rewards.

## Notes

Console messages are in Spanish, while code identifiers and this README are in
English.

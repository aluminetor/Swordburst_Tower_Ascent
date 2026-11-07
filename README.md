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

## Project structure

- `main.py` - Runs the sample battle.
- `entities/` - Base entities and player classes.
- `items/` - Weapons, potions, and shared item behavior.

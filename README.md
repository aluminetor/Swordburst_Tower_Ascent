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

## Project structure

- `main.py` - Runs the sample battle.
- `entities/` - Base entities and player classes.
- `items/` - Weapons, potions, and shared item behavior.

import random

from entities.base_entity import Entity
from items.base_item import Item
from items.weapons import Sword
from items.consumables import Potion
from entities.player import Player, DualWielder, Paladin


def print_section(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def print_health(name, health, max_health):
    filled = max(0, min(20, round(20 * health / max_health)))
    bar = "#" * filled + "-" * (20 - filled)
    print(f"{name:<16} [{bar}] {health}/{max_health} HP")


def main(): 
    print_section("Swordburst Tower Ascent")
    # Instanciamos el primer objeto y segundo (por ejemplo, el bear)
    bear = Entity(name="Bear", max_hp=1500, power_attack=400, defend=300)
    wasp = Entity(name="Wasp",max_hp=1200,power_attack=150,defend=250)
    #Instancia de espadas 
    iron_sword = Sword(name="Iron Sword",rarity="Commun",bonus_damage=10)
    dark_repulsor = Sword(name="Dark Repulsor",rarity="Rare",bonus_damage=35)
    #potion
    potion = Potion(name="Health Potion",rarity="Common",heal_amount=100)
    #Instancia un DualWielder y un Paladin.
    dual_wielder = DualWielder(
        name="Dual Wielder",
        max_hp=1300,
        power_attack=350,
        defend=220
    )

    paladin = Paladin(
        name="Paladin",
        max_hp=1800,
        power_attack=250,
        defend=180
    )

    dual_wielder.equip_weapon(iron_sword)
    dual_wielder.equip_offhand_weapon(dark_repulsor)

    random.seed(1)
    unarmed_dual_wielder = DualWielder(
        name="Unarmed Dual Wielder",
        max_hp=1300,
        power_attack=350,
        defend=220
    )
    unarmed_target = Entity(
        name="Unarmed Target",
        max_hp=2000,
        power_attack=0,
        defend=0
    )
    armed_target = Entity(
        name="Armed Target",
        max_hp=2000,
        power_attack=0,
        defend=0
    )
    unarmed_damage = unarmed_dual_wielder.starburst_stream(unarmed_target)
    armed_damage = dual_wielder.starburst_stream(armed_target)
    print(f"Daño desarmado: {unarmed_damage} HP.")
    print(f"Daño con dos espadas: {armed_damage} HP.")

    print_section("Turno 1")
    dual_damage = dual_wielder.starburst_stream(paladin)
    print(f"DualWielder inflige {dual_damage} HP al Paladin.")
    paladin_damage = paladin.attack(dual_wielder)
    print(f"Paladin inflige {paladin_damage} HP al DualWielder.")
    print_health("Paladin", paladin.get_health(), 1800)
    print_health("DualWielder", dual_wielder.get_health(), 1300)

    print_section("Turno 2")
    dual_damage = dual_wielder.starburst_stream(paladin)
    print(f"DualWielder inflige {dual_damage} HP al Paladin.")
    paladin_damage = paladin.attack(dual_wielder)
    print(f"Paladin inflige {paladin_damage} HP al DualWielder.")
    health_before_heal = paladin.get_health()
    paladin.holy_light()
    print(
        f"Paladin se cura de {health_before_heal} a "
        f"{paladin.get_health()} HP consumiendo 20 de estamina."
    )
    print_health("Paladin", paladin.get_health(), 1800)

    print_section("Equipo y consumibles")
    attack = Entity.attack(bear, wasp)

    print(f"{bear.get_name()} atacó a {wasp.get_name()}.")
    print(f"Daño realizado: {attack} HP.")
    print_health("Wasp", wasp.get_health(), 1200)

    print("Armas equipadas:")
    print(iron_sword)
    print(dark_repulsor)

    print(f"¿Dark Repulsor es superior? {'Sí' if dark_repulsor > iron_sword else 'No'}")

    # entidad de prueba de la Fase 1 reciba daño, y luego usa una Potion sobre ella(wasp)
    potion.use(wasp)
    print(f"{potion} aplicada a {wasp.get_name()}.")
    print_health("Wasp", wasp.get_health(), 1200)

if __name__ == "__main__":
    main()
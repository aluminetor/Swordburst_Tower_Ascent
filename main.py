from entities.base_entity import Entity
from items.weapons import Sword 
from items.base_item import Item 

def main(): 
    # Instanciamos el primer objeto y segundo (por ejemplo, el bear)
    bear = Entity(name="Bear", max_hp=1500, power_attack=400, defend=300)
    wasp = Entity(name="Wasp",max_hp=1200,power_attack=150,defend=250)
    #Instancia de espadas 
    iron_sword = Sword(name="Iron Sword",rarity="Commun",bonus_damage=10)
    dark_repulsor = Sword(name="Dark Repulsor",rarity="Rare",bonus_damage=35)

    attack = Entity.attack(bear,wasp)
    
    print(f"{bear.get_name()} ataco a  {wasp.get_name()}.")                                                    
    print(f"Daño realizado: {attack} HP.")    
    print(f"{bear.get_name()} ataco a  {wasp.get_name()}, salud del Wasp {wasp.get_health()}")
    print(iron_sword)
    print(dark_repulsor)


if __name__ == "__main__":
    main()
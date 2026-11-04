from entities.base_entity import Entity

def main(): 
    # Instanciamos el primer objeto (por ejemplo, el bear)
    bear = Entity(name="Bear", max_hp=1500, power_attack=400, defend=300)
    # Instanciamos el segundo objeto
    wasp = Entity(name="Wasp",max_hp=1200,power_attack=150,defend=250)

    attack = Entity.attack(bear,wasp)
    
    print(f"{bear.get_name()} ataco a  {wasp.get_name()}.")                                                    
    print(f"Daño realizado: {attack} HP.")    
    print(f"{bear.get_name()} ataco a  {wasp.get_name()}, salud del Wasp {wasp.get_health()}")


if __name__ == "__main__":
    main()
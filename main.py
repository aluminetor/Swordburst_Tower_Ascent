from entities.base_entity import Entity

def main(): #name, max_hp, power_attack, defend)
    # Instanciamos el primer objeto (por ejemplo, el bear)
    bear = Entity(name="Bear",max_hp=1500,power_attack=150,defend=300)

    # Instanciamos el segundo objeto
    wasp = Entity(name="Wasp",max_hp=1200,power_attack=150,defend=250)

    print(f"{bear.get_name()} tiene {bear.get_health()} HP.")                                                    
    print(f"{wasp.get_name()} tiene {wasp.get_health()} HP.")    

if __name__ == "__main__":
    main()
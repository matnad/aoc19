def get_fuel_incl_fuel():
    total_fuel = 0
    with open('input.txt') as file:
        for idx, mass in enumerate(file):
            fuel = 0
            mass = int(mass)
            while True:
                mass = mass // 3 - 2
                if mass <= 0:
                    break
                fuel += mass
            total_fuel += fuel

    return total_fuel


print(get_fuel_incl_fuel())

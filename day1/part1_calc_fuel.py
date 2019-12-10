def get_fuel():
    total_mass = 0
    with open('input.txt') as file:
        for idx, mass in enumerate(file):
            total_mass += int(mass) // 3 - 2
    return total_mass


print(get_fuel())
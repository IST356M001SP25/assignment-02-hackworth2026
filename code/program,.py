'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

import json 

def parse_packaging(data: str) -> list[dict]:
    return [{unit: int(qty)} for part in data.split("/") for qty, unit in [part.split()[:2]]]
def calc_total_units(package: list[dict]) -> int:
    total = 1
    for item in package:
        total *= next(iter(item.values()))
    return total

def get_unit(package: list[dict]) -> str:
    return next(iter(package[0])) if package else ""

def main():
    input_file = "data/packaging.txt"
    output_file = "data/packaging.json"
    packages = []
    
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                package = parse_packaging(line)
                total_units = calc_total_units(package)
                unit = get_unit(package)
                print(f"{line} => total units: {total_units} {unit}")
                packages.append(package)
    
    with open(output_file, "w") as file:
        json.dump(packages, file, indent=4)

if __name__ == "__main__":
    main()

# Test cases
print(parse_packaging("12 eggs in 1 carton"))
print(parse_packaging("6 bars in 1 pack / 12 packs in 1 carton"))
print(parse_packaging("20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"))

print(calc_total_units([{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]))  # Output: 72
print(calc_total_units([{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]))  # Output: 800

print(get_unit([{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]))  # Output: bars
print(get_unit([{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]))  # Output: pieces

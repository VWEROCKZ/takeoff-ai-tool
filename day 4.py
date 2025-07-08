def get_input():
    name = input("Enter item name: ")
    category = input("Is it count, area, or volume based? ").lower()
    return name, category

def handle_count(name):
    count = int(input("Enter number of items: "))
    print(f"{count} units of {name}")

def handle_area(name):
    l = float(input("Length: "))
    w = float(input("Width: "))
    print(f"Area for {name}: {calculate_area(l, w)} sq.m")

def handle_volume(name):
    l = float(input("Length: "))
    w = float(input("Width: "))
    h = float(input("Height: "))
    print(f"Volume for {name}: {calculate_volume(l, w, h)} cu.m")
    for i in range(3):
    name, category = get_input()
    if category == "count":
        handle_count(name)
    elif category == "area":
        handle_area(name)
    elif category == "volume":
        handle_volume(name)
    else:
        print("Invalid type.")


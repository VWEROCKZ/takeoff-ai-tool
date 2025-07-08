print("📋 Welcome to Quantity Type Categorizer")
print("----------------------------------------")

# Ask how many items the user wants to estimate
num_items = int(input("How many items do you want to enter? 👉 "))

for i in range(num_items):
    print(f"\n🧾 Item {i+1}:")
    name = input("Enter item name (e.g., wall, door, tile): ")
    category = input("Is it count, area, or volume based? ").lower()

    if category == "count":
        count = int(input("Enter number of items: "))
        print(f"✅ You need {count} units of {name}.")
    elif category == "area":
        length = float(input("Enter length (m): "))
        width = float(input("Enter width (m): "))
        area = length * width
        print(f"✅ Total area for {name} is {area:.2f} sq.m")
    elif category == "volume":
        length = float(input("Enter length (m): "))
        width = float(input("Enter width (m): "))
        height = float(input("Enter height (m): "))
        volume = length * width * height
        print(f"✅ Total volume for {name} is {volume:.2f} cu.m")
    else:
        print("❌ Unknown category. Please enter count, area, or volume.")

print("\n🎉 All items processed! You're getting the hang of it.")
while True:
    name = input("Item name (or type 'exit' to stop): ")
    if name.lower() == 'exit':
        break
# Takeoff Calculator – Area Estimation

print("📐 Quantity Takeoff: Area Calculator")
print("-------------------------------------")

# Get user input
length = float(input("Enter the length (in meters): "))
width = float(input("Enter the width (in meters): "))
height = float(input("Enter the height (in meter): "))

# Calculate area
area = length * width

# Output the result
print("✅ Total area is:", area, "square meters")

volume = length * width * height

print("total volume is : ",volume," cubic meters" )

# Optional: Estimate material quantity (e.g., tile coverage)
tile_coverage = 0.25  # Each tile covers 0.25 sqm
tiles_needed = area / tile_coverage


print("🧱 Approx. tiles needed:", round(tiles_needed), "tiles")

paint_coverage = 10

paint_needed = volume/ paint_coverage

print(" Approx, paint needed: " ,round(paint_needed), "litres of paint")

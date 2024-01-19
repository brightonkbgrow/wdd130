import math
radius = float(input("What is the radius of the can? "))
height = float(input("What is the height of the can? "))
cpc = float(input("What is the cost per can? "))
sa = 2 * math.pi * radius* (radius + height)
vol = 2 * math.pi * (radius**2) * height
storage_efficiency = vol/sa

print(f"The surface area of the can is {sa:.2f} cm squared")
print(f"The volume of the can is {vol:.2f} cm cubed")
print(f"The storage efficiency of the can is {storage_efficiency:.2f}")

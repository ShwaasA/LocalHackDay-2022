print("\nSTAY HYDRATED\n")
print("Average Water intake:")
print("Men: 3.7 liters (130 fl oz)")
print("Women: 2.7 liters (95 fl oz)")

cap = int(input("What's the capacity of the container used to drink water (in ml): "))
count = int(input("How many times did you finish and refill the container? "))

if count * cap < 3200:
    left = 3200 - (count * cap)
    print(f"\nDrink {left}ml more water to complete the daily water consumption level.\n")

else:
    print("You drank more water than the average daily water consumption of a normal person.\n")

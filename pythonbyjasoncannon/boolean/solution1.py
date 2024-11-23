distance=int(input("How far to travel :"))

if distance<3:
    mode_of_transport="walk"
elif distance<300:
    mode_of_transport="drive"
else:
    mode_of_transport="fly"

print("I suggest you to {} to reach your destination".format(mode_of_transport))


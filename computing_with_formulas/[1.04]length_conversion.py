# Exercise 1.04

inch = 0.0254
foot = inch * 12
yard = foot * 3
mile = yard * 1760

metres = input('Enter distance in meters to be converted to imperial units\n')
metres = float(metres)
inches = metres / inch
feet = metres / foot
yards = metres / yard
miles = metres / mile

print(f"{metres:g} metres is equivalent to {inches:g} inches, {feet:g} feet, {yards:g} yards, {miles:g} miles.")


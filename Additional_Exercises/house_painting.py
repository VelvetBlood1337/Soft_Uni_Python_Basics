# paint - area painted with 1 liter
GREEN_M = 3.4
RED_M = 4.3

# house height
x = float(input())
# length of side wall
y = float(input())
# height of the roof
h = float(input())

# walls painted in green
fb_walls = 2 * (x * x) - 2 * 1.2
sd_walls = 2 * (x * y) - 2 * 1.5 * 1.5
gw = fb_walls + sd_walls
gwp = gw / 3.4

# roof painted red
rs = 2 * x * y + (x * h)
rsp = rs / 4.3

print(f"{gwp:.2f}")
print(f"{rsp:.2f}")

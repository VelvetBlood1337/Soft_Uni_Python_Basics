length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
# all input in cm

tank_volume = length * width * height
volume_in_liters = tank_volume / 1000

liters_needed = volume_in_liters * (1 - percent)

print(liters_needed)

# version 2

length, width, height = int(input()), int(input()), int(input())
percent_filled = float(input()) / 100

volume = (length * width * height) / 1000
volume -= volume * percent_filled

print(volume)

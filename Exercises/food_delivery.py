CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEG_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_veg_menus = int(input())

meal_price = (number_of_chicken_menus * CHICKEN_MENU_PRICE) + \
              (number_of_fish_menus * FISH_MENU_PRICE) + \
              (number_of_veg_menus * VEG_MENU_PRICE)

dessert_price = meal_price * 0.20

total_price = meal_price + dessert_price + DELIVERY_PRICE

print(f"{total_price:,.2f}")

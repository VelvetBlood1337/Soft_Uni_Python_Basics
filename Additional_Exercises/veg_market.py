veg_kilo_price = float(input())
fruit_kilo_price = float(input())
ttl_veg_kilos = float(input())
ttl_fruit_kilos = float(input())

ttl_income = ((veg_kilo_price * ttl_veg_kilos) + (fruit_kilo_price * ttl_fruit_kilos)) / 1.94

print(f"{ttl_income:.2f}")

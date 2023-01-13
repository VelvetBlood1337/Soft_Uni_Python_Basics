square_meters_total = float(input())
full_price = square_meters_total * 7.61
discount = full_price * 0.18
final_price = full_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

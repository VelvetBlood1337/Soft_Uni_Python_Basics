# better name constants with capital letters
pen_package = 5.80
marker_package = 7.20
cleaner_per_liter = 1.20

number_of_pen_packages = int(input())
number_of_marker_packages = int(input())
liters_of_cleaner = int(input())
percent_discount = int(input()) / 100

original_payment_amount = number_of_pen_packages * pen_package + \
                          number_of_marker_packages * marker_package + liters_of_cleaner * cleaner_per_liter
discount = original_payment_amount * percent_discount

final_amount = original_payment_amount - discount

print(final_amount)

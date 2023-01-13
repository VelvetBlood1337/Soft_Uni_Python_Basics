NYLON_COVER_PER_METER = 1.50
PAINT_PER_LITER = 14.50
PAINT_THINNER_PER_LITER = 5.00
BAGS_PRICE = 0.40

nylon_cover_meters_needed = int(input())
paint_needed_in_liters = int(input())
paint_thinner_in_liters = int(input())
hours_to_complete_the_job = int(input())

nylon_cover_total = (nylon_cover_meters_needed + 2) * NYLON_COVER_PER_METER
paint_total = (paint_needed_in_liters * 1.10) * PAINT_PER_LITER
paint_thinner_total = paint_thinner_in_liters * PAINT_THINNER_PER_LITER

total_sum = nylon_cover_total + paint_total + paint_thinner_total + BAGS_PRICE

pay_per_hour = total_sum * 0.30
renovation_work_cost = hours_to_complete_the_job * pay_per_hour

final_cost = total_sum + renovation_work_cost

print(final_cost)

# version 2

nylon = int(input())
paint_liters = int(input())
thinner_in_liters = int(input())
hours = int(input())

nylon += 2
paint_liters *= 1.1
thinner = thinner_in_liters * 5.00

total_sum = nylon * 1.50 + paint_liters * 14.5 + thinner + 0.40

pay_per_hour = total_sum * 0.30
renovation_work_cost = hours * pay_per_hour

final_cost = total_sum + renovation_work_cost

print(final_cost)

# version 3 (re-done)
nylon = int(input())
paint_liters = int(input())
thinner_in_liters = int(input())
hours = int(input())

nylon += 2
paint = paint_liters * 1.10
thinner = thinner_in_liters * 5.00

total_sum = nylon * 1.50 + paint * 14.5 + thinner + 0.40

pay_per_hour = total_sum * 0.30
renovation_work_cost = hours * pay_per_hour

final_cost = total_sum + renovation_work_cost

print(final_cost)

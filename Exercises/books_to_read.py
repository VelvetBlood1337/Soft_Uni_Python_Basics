number_of_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())
total_hours_to_read = number_of_pages / pages_per_hour

hours_per_day_to_read = int(total_hours_to_read / days_to_read)
# or whole number division AS hours_per_day_to_read = total_hours_to_read // days_to_read

print(hours_per_day_to_read)

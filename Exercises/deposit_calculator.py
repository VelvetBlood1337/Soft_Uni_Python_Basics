deposit_amount = float(input())
deposit_duration_in_moths = int(input())
yearly_percent = float(input()) / 100
# same as yearly_percent /=100
total_sum = deposit_amount + deposit_duration_in_moths * ((deposit_amount*yearly_percent)/12)

print(total_sum)

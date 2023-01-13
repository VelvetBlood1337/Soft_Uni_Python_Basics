annual_training_fee = int(input())

shoes = annual_training_fee * 0.60
outfit = shoes * 0.80
ball = outfit * 0.25
accessories = ball * 0.20

total_expense = annual_training_fee + shoes + outfit + ball + accessories

print(total_expense)

# version 2

yearly_fee = int(input())

shoes = yearly_fee - yearly_fee * 0.40
clothes = shoes - shoes * 0.20
ball = clothes / 4
others = ball / 5

total_sum = shoes + clothes + ball + others + yearly_fee

print(total_sum)

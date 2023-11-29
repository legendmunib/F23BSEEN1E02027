prev_number = 0
current_number = 0
current_sum = 0
for i in range(0, 11):
    current_number = i
    prev_number = current_number - 1
    current_sum = current_number + prev_number
    print(f"Current Number {current_number} Previous Number {prev_number} Sum: {current_sum}")

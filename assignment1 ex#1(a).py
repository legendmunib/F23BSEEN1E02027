
number1 = 20
number2 = 30
def num1_num2(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2
output= num1_num2(number1, number2)
print(output)
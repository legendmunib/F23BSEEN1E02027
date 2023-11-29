i = 125
rev = 0
x = i
while i > 0:
    rev = (rev * 10) + i % 10
    i = i // 10

if x == rev:
    print("Given number is a palindrome number")
else:
    print("Given number is not a palindrome number")
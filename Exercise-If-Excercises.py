number1 = 10
number2 = 10
number3 = 5

#2a
print("All numbers are equal:", number1 == number2 == number3)

#2b
print("Either number1 == number2 OR number2 == number3:", 
      number1 == number2 or number2 == number3)

#2c
print("number1 > number2 AND number1 > number3:", 
      number1 > number2 and number1 > number3)

#2d
if number1 > number2:
    print("number1 > number2")
elif number2 > number3:
    print("number2 > number3")
else:
    print("Neither condition is true")

#2e
if number1 == number2:
    print("number1 == number2")
elif number1 == number3:
    print("number1 == number3")
else:
    print("None of them are the same")
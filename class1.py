val1 = float(input("Enter first number:"))
val2 = float(input("Enter second number:"))
val3= float(input("Enter third number:"))
#Subtaction 
sub = (val1-val2) *val3
print("The result of the subtraction is: ", sub)


#Addition
add = val1+val2+val3
print("The result of the addition is: ", add)

#Multiplication
mul = val1 * val2*val3
print("The result of the multiplication is: ", mul)

#Power
pow = (val1**val2)+val3
print("The result of the power operation is: ", pow)

#Division
if float(val2) == 0:
    print("Invalid Input for division")
else:
    div = (val1 / val2)+val3
    print("The result of the division is: ", div)

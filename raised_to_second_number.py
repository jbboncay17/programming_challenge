bold='\033[1m'
end='\033[0m'
green='\033[32m'

num1=int(input(bold+"Enter the first number:"))
num2=int(input(bold+"Enter the second number:"))

raised=num1**num2
print(bold+green+"First number raised to the second number is equal to="+end,raised)
bold='\033[1m'
end='\033[0m'
green='\033[32m'

num1=int(input(bold+"Enter the first number:"+end))
num2=int(input(bold+"Enter the second number:"+end))
print("")
if num1>num2:
    print(bold+green+"The bigger number is:"+end, num1)
elif num2>num1:
    print(bold+green+"The bigger number is:"+end, num2)
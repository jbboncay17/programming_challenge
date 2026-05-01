bold="\033[1m"
end="\033[0m"
green="\033[32m"

sum=0

for i in range(10):
    number = float(input(bold+f"Enter a number {i+1}: "+end))
    sum += number
print("")
print(bold+green+"The sum of all 10 numbers is="+end,sum )
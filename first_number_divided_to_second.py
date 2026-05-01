bold="\033[1m"
red="\033[31m"
green="\033[32m"
end="\033[0m"

firstnumber=int(input(bold+"Enter the first number: "+end))
secondnumber=int(input(bold+"Enter the second number: "+end))

if secondnumber !=0:
    remainder=firstnumber%secondnumber
    print("")
    print(bold+green+"The remainder is:"+end, remainder)

else:
    print("")
    print(bold+red+"Syntax Error"+end)
bold='\033[1m'
end='\033[0m'

num=0

while num<=100:
    if num%2!=0:
        print(bold+"",num)
    num=num+1
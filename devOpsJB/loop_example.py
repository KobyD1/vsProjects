# 1 digit - start with 0 , end with the digit 
# 2 digits - start with first number , end with second number
# 3 - digits -  start with first number , end with second number , with sterp according the third number 
for count  in range (10):
    print (f"the value of i is {count}")
    if count ==2:
        continue 
    print (f"the new value of i is {count}")
    if (count ==3):
        break 

# while loop 

is_loop = True
num = 1  
counter = 25


while is_loop and counter !=0 :
    print (num)
    result  = num % 5
    if result ==6 :
        is_loop = False
    num +=1 # as num= num+1 
    counter -=1


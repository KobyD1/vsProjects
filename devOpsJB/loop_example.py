# 1 digit - start with 0 , end with the digit 
# 2 digits - start with first number , end with second number
# 3 - digits -  start with first number , end with second number , with sterp according the third number 
for count  in range (1,10,3):
    print (f"the value of i is {count}")
    count = count + count
    print (f"the new value of i is {count}")

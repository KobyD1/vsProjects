
a= 3 
is_pass = False
if (is_pass==True):
    res = a* a 


else:
    res = a+a  

print (f"the results is {res}")

last_name = "Messi"

if (last_name=="Messi"):    # condition by equals 
    print ("Messi found ")

#if ( last_name!="Messi"):    # condition by not equals 


if (not last_name=="Messi"):    # condition by not equals 
    print ("Messi not found ")

print ("### condition example ####")

num_1 = 10

#example of multiple if 

# if (num_1 % 2 ==0):
#     print ("dived by 2 number fond")
# if (num_1 % 3 ==0):
#     print ("divied by 3 number found ")
# if (num_1 % 5 ==0):
#     print ("divied by 5 number found ")

#example of multiple if 

if (num_1 % 2 ==0) and (num_1 ==11):
    print ("dived by 2 number found")
    num_1= num_1 *2 
elif (num_1 % 3 ==0):
    print ("divied by 3 number found ")
elif (num_1 % 6 ==0):
    print ("divied by 5 number found ")
else :
    print ("the number is not dived by any tested number ")


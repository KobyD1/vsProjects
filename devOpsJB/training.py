digits= '123'

digits_as_int = int(digits)  # example of casting to int 
res = digits_as_int /3

num = 123456

num_as_str = str(num)  # example of casting to string 
string_slicing = 'abcdef'
slice = string_slicing[2:4]
string_slicing[:4]  # start from 0
string_slicing[4:] # end with the length of the string 
string_slicing[-3:-1]  # example of position VS the end of the string 

full_name = 'Leo Messi'
last_name = full_name[3:]
index = full_name.index(" ")
# last_name = full_name[index+1:]
last_name= full_name[index:]
last_name= last_name.strip()


index = num_as_str.index(3)
print ("end")
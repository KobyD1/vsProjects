# define mail and verily if leagal by contains @ and dot 
input_mail = "abcdemo.com"
first_count = input_mail.count("@")
dot_count = input_mail.count(".")
if (first_count ==1) and (dot_count>0):
    print ("legal mail found")
else:
    print ("not legal mail found ")
first_index = 0 
if (first_count > 0 ):
    first_index= input_mail.index("@")
index_dot = input_mail.index(".")

if index_dot>first_index:
        print ("legal mail found by index analyze")



print ("code end")
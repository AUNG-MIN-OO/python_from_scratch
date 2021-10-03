# age = int(input('type your age : '));
# if age < 18 :
#     print("you cant drink alcohol");
# elif age == 20 and age <21 : 
#     print("you can have a girlfriend");
# else :
#     print('you can now drink alcohol')

# tired = input('Are you tired? "y/n" : ')
# if tired == 'y' :
#     print("go back and rest")
# elif tired == 'n' :
#     print("go back to work")
# else :
#     print("please enter y or n")

username = "aungminoo"
password = '302918';
loginName = input('username : ') ;
loginPass = input('password : ');
if loginName == username and loginPass == password : 
    print('you are now loggied in')
elif loginName != username and loginPass == password : 
    print("username is wrong")
elif loginName == username and loginPass != password : 
    print("password is wrong")
else :
    print("user name and password is wrong")

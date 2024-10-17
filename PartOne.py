#get a variable name from the user
camel = input("give me a variable name in camel case: ")
#create an empty string for the new variable name
snake = ""

#loop through each character
for x in camel:
    if x.isupper() == True:
        #replace every upper case letter with an underscore and the lowercase of the letter
        snake = snake + "_" + x.lower() 
    else:
        #add each lowercase letter as it is
        snake = snake + x

#print out the new copy of the varible name
print("this variable in snake case is: " + snake)

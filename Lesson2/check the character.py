choice = input("Please Enter Your Own Character : ")

if((choice >= 'a' and choice <= 'z') or (choice >= 'A' and choice <= 'Z')): 
  
    print("The Given Character ", choice, "is an Alphabet") 
elif(choice >= '0' and choice <= '9'): 
  
    print("The Given Character ", choice, "is a Digit")
else: 
  
    print("The Given Character ", choice, "is a Special Character")
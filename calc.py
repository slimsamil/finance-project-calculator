from classes import *

def main():
    
    print("Welcome to the finance project calculator")
    while True:
        project = int(input(
        "Choose one of the following projects\n1: Passbook\n2: Loan\n3: Return of Investment\n4: Building Saving\n5: Exit\n"))

        if project == 1:
            passbook()
            
        
        elif project == 2:
            loan()
            

        elif project == 3:
            roi()
            

        elif project == 4:
            print("  ")
            print("this function isn't implemented yet")
            #buildingsaving()

        elif project == 5:
            print("  ")
            print("Thank you for using the finance project calculator")
            break

        else:
            print("  ")
            print("Your input did not equal one of the choices, try it again")
            
            
    


if __name__ == '__main__':
    main()

###Programming Project
###Garrett Jones, Dante Smith, Jose Oliver
###CPSC 1301K

def welcome():
    print("""Thank you for using the Distaster Preparation and Action Planning Programming! \n""")

def prepare():
    supplyList = ["Food", "Water", "Batteries","Flashlight","Portable Power Supply"]
    prepare = True
    while prepare:
        prepType = input("What information would you like on how to prepare? Type 'Supply' for a list of supplies, or 'Back' to return to the previous menu: ").lower()
        print()
        if prepType == "supply":
            print("Ensure your distaster preparation kit contains the following items:")
            
            for i, supply in enumerate(supplyList):
                print(f"{i+1}.",supply)
            print()
        elif prepType == "back":
            prepare = False
        else:
            print("Please enter a valid input! \n")
        
def act():
    foodList = ["Feeding the Valley Food Bank"]
    housingList = ["The Housing Authority of Columbus, GA", "Emergency Housing Voucher Program","Habitat for Humanity"]
    clothingList = ["Goodwill","Plato's Closet"]
    jobList = ["Goodwill"]
    monetaryList = ["GEMA Grants"]
    generalList = ["Homeless Resource Network"]
    act = True
    while act:
        actType = input("What information would you like on what to do post-disaster? Type 'Food' for food assistance, 'Housing' for housing assistance, 'Clothing' for low-cost clothing options, 'Job' for job assistance, 'Monetary' for monetary assistance, 'General' for general assistance, or 'Back' to return to the previous menu: ").lower()
        print()
        if actType == "food":
            for i, food in enumerate(foodList):
                print(f"{i+1}.",food)
            print()
        elif actType == "housing":
            for i, housing in enumerate(housingList):
                print(f"{i+1}.",housing)
            print()
        elif actType == "clothing":
            for i, clothing in enumerate(clothingList):
                print(f"{i+1}.",clothing)
            print()
        elif actType == "job":
            for i, job in enumerate(jobList):
                print(f"{i+1}.",job)
            print()
        elif actType == "monetary":
            for i, monetary in enumerate(monetaryList):
                print(f"{i+1}.",monetary)
            print()
        elif actType == "general":
            for i, general in enumerate(generalList):
                print(f"{i+1}.",general)
            print()
        elif actType == "back":
            act = False
        else:
            print("Please enter a valid input! \n")
            
                

def main():
    welcome()
    running = True
    while running:
        type = input("Please enter 'Prepare' or 'Act' to receive assistance or type 'Quit' to exit the program: ").lower()
        print()
        if type == 'quit':
            running = False
        elif type == 'act':
            act()
        elif type == 'prepare':
            prepare()
        else:
            print("Please enter a valid input! \n")

    print("Thank you for using our distater Prepare and Act program!")

main()

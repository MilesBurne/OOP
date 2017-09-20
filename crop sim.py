#Crop simulator by Miles Burne 18/9/17
import random

class Crop:
    """ A simple food crop """

    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        #set initial attributes w/ values

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        #attributes with underscores are private, should not be accessed directly
        #OUTSIDE the class

    #method to report on current needs on crop    
    def needs(self):
        #ALL methods NEED 'self'
        #return a dictionary containing light & water needs
        return {'light need':self._light_need,'water need':self._water_need}

    #method to report the provide information about the current state or status of crop
    def report(self):
        #NEED 'self'
        #return dictionary containing type, status, growtt and days growing
        return{'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    #method to update the status of the crop
    def _update_status(self):
        if self._growth > 300:
            self._status = 'Dinosaur'
        elif self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seedling'
        elif self._growth == 0:
            self._status = 'Seed'


    #method to grow the crop according to the light, water and growth rate
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update status
        self._update_status()


#FUNCTION not method, uses the METHOD grow therefore not a method itself        
def auto_grow(crop, days):
    #grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light, water)

#function to allow the user to grow the crop manually 
def manual_grow(crop):
    #get the light and water values from user
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value between 1 and 10: "))
            if 1 <= light <=10:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 10: ")
        except ValueError:
            print("Value entered is not valid - please enter a value between 1 and 10: ")
    valid = False

    while not valid:
        try:
            water = int(input("Please enter a water value between 1 and 10: "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 10: ")
        except ValueError:
            print("Value entered is not valid - please enter a value between 1 and 10: ")
    crop.grow(light, water)
    
#function to display the menu
def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program\n")
    print("Please selct an option from the above menu")

#function to get the users input for the menu
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Select an option: "))
            if 0 <= choice <= 3:
                option_choice = True
            else:
                option_choice = False
                print("Please enter a value between 0 and 3: ")
        except ValueError:
            print("Please enter a value between 0 and 3: ")

        return(choice)

def manage_crop(crop):
    print("This is the crop management system\n")
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop, 30)
        elif option == 3:
            print(crop.report(),"\n")
        elif option == 0:
            noexit = False
            print()
            print("Thank you for using our system")
    


def main():
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

main()

        




        
        

    

#Tree growth by Miles Burne 18/9/17
import random

class Tree:
    """ A simple tree """

    #constructor
    def __init__(self, growth_rate, water_level, light_level, space_amount):
        #set initial attributes

        self._growth = 0
        self._days_grown = 0
        self._water_level = water_level
        self._growth_rate = growth_rate
        self._light_level = light_level
        self._space_amount = space_amount
        self._status = "Seed"
        self._type = "generic"


    def needs(self):
        return{"light need":self._light_level,"water need":self._water_level,"space need":self._space_amount}

    def report(self):
        return{"type":self._type,"status":self._status,"growth":self._growth,"days growing":self._days_grown,"space left":self._space_amount}

    def _update_status(self):
        if self._growth >= 36500:
            self._status = "Ancient"
        elif self._growth >= 18250:
            self._status = "Old"
        elif self._growth >= 9125:
            self._status = "Reletively old"
        elif self._growth >= 4562:
            self._status = "Young"
        elif self._growth >= 2281:
            self._status = "New"
        elif self._growth >= 1095:
            self._status = "Tiny"
        elif self._growth >= 0:
            self._status = "Sapling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self, light, water):
        if light >= self._light_level and water >= self._water_level:
            self._growth += self._growth_rate
        self._days_grown += self._growth_rate
        self._update_status()

def auto_grow(Tree):
    valid = False
    while not valid:
        try:
            days = int(input("Please enter the desired amount of months: "))
            valid = True
        except ValueError:
            print("Value entered incorrectly - Please enter a whole number: ")
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        Tree.grow(light, water)

def manual_grow(Tree):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter the desired light level between (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Please enter a whole number between (1-10): ")
        except ValueError:
            print("Value entered incorrectly - Please enter a whole number between (1-10): ")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter the desired water level between (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Please enter a whole number between (1-10): ")
        except ValueError:
            print("Value entered incorrectly - Please enter a whole number between (1-10): ")
    Tree.grow(light, water)

def display_menu():
    print("1. Grow manually over 30 days")
    print("2. Grow automatically")
    print("3. Report status")
    print("0. Exit test program\n")
    print("Please selct an option from the above menu")

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


def manage_tree(tree):
    print("This is the tree management system\n")
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(tree)
        elif option == 2:
            auto_grow(tree)
        elif option == 3:
            print(tree.report(),"\n")
        elif option == 0:
            noexit = False
            print()
            print("Thank you for using our system")    
        
def main():
    new_tree = Tree(30,4,3,100)
    manage_tree(new_tree)

main()
















    
    

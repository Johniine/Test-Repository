valid = True
pet_list = {}

class Pet():
    def __init__(self,name=None,weight=0):
        self.name = str(name)
        self.weight = int(weight)
    
    def feed(self,unit):
        ate = self.weight + unit
        return ate
    
    def excercise(self,unit):
        exc = self.weight - unit
        return exc

while valid == True:
    ask_name = input("Enter pet name (xyz to end): ").lower()
    if not ask_name.isalpha():
        print("Please enter a valid pet name")
    elif ask_name == "xyz":
        valid = False
    else:
        ask_weight = int(input("Enter weight: "))

        pet_list[ask_name] = ask_weight

def check_status():
    print("Pet Status")
    print("="*11)
    for key in pet_list:
        if pet_list[key] <= 0:
            print(f"{key} : Dead")
        elif pet_list[key] >= 200:
            print(f"{key} : Sad")
        elif pet_list[key] > 0 and pet_list[key] < 200:
            print(f"{key} now weights {pet_list[key]}")
    print("="*11)

def skyfall():
    promp = input("Enter n to stop playing, or any other key to keep playing: ").lower()
    if promp == "n":
        check_status()
    else:
        actions()

def actions():
    print("="*11)
    for key in pet_list:
        the_honoured_pet = Pet(key,pet_list[key])
        ask_action = input(f"Enter F to feed, E to excercise or Q to quit for {key}: ").lower()
        if ask_action == "f":
            if pet_list[key] == 0:
                ask_unit = int(input("Enter unit of food between 1 and 200: "))
                pet_list[key] = 0
            else:
                ask_unit = int(input("Enter unit of food between 1 and 200: "))
                weight = the_honoured_pet.feed(ask_unit)
                pet_list[key] = weight
        elif ask_action == "e":
            if pet_list[key] == 0:
                ask_unit = int(input("Enter minutes of excercise between 1 and 200: "))
                pet_list[key] = 0
            else:
                ask_unit = int(input("Enter minutes of excercise between 1 and 200: "))
                weight = the_honoured_pet.excercise(ask_unit)
                pet_list[key] = weight
        elif ask_action == "q":
            check_status()
    print("="*11)
    skyfall()

actions()
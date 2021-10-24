productSelection_01 = {
    "APPLE":20,
    "ORANGE":25,
    "BANANA":12,
    "GUAVA":32,
    "MANGO":35,
    "MELON":45
} #Added dictionary for product selection
#productCode = {
    #"0001":{"APPLE"},
    #0002":{"BANANA"},
    #"0003":{"GUAVA"},
    #"0014":{"MANGO"},
    #"0015":{"MELON"},
    #"0023":{"ORANGE"}
#}

def init_cmd(): #Asks for valid command -- option to either browse or exit.
    while True:
        usr_first_cmd = input("\n> ").lower()
        if usr_first_cmd == "add":
            return True
        elif usr_first_cmd == "exit":
            return "exit_signal"
        else:
            print("Please enter a valid command.")

def second_cmd(): #Ask users for product to check
    while True:
        usr_second_cmd = input("\nEnter product name: ").upper()
        if usr_second_cmd in productSelection_01:
            print("We do have that here. Would you like to purchase?")
            return "proceed"
        elif usr_second_cmd == "EXIT":
            print("Thank you for stopping by. Come again.")
            return None
        else:
            print("Sorry. We don't have that here.")
        

print("\nadd  - Browse shop items\nexit - Terminate transaction anytime")

initial = init_cmd()

if initial == True:
    print("\nItem list:")
    for i in productSelection_01:
        print(i.capitalize())
    print("\nWhat would you like to buy?")
    second_cmd()
else:
    print("Have a nice day.")

productSelection_01 = {
    "APPLE":20,
    "ORANGE":25,
    "BANANA":12,
    "GUAVA":32,
    "MANGO":35,
    "MELON":45
} #Added dictionary for product selection

productCode = {
    "0001":"APPLE",
    "0002":"BANANA",
    "0003":"GUAVA",
    "0014":"MANGO",
    "0015":"MELON",
    "0023":"ORANGE"
} #Added product codes users can input to access product.

def init_cmd(): #Asks for valid command -- option to either browse or exit.
    while True:
        usr_first_cmd = input("\n> ").lower()
        if usr_first_cmd == "add":
            return True
        elif usr_first_cmd == "exit":
            return "exit_signal"
        else:
            print("Please enter a valid command.")

def codeRead(arg1):
    if arg1 in productCode:
        retriv_product = productCode.get(arg1)
        retreived = productSelection_01.get(retriv_product)
        return retreived

def YNConfirmation(arg1):
    if arg1 == True:
        print("Would you like to purchase?")
        while True:
            usr_decision = input("       Yes or No \n> ").lower()
            if usr_decision == "yes":
                return True
            elif usr_decision == "no":
                return False
            else:
                print("Please enter a valid command.")
    else:
        return None

def second_cmd(): #Ask users for product to check
    while True:
        usr_second_cmd = input("\nEnter product name or code: ").upper()
        if usr_second_cmd in productSelection_01:
            print(f"We do have that here. It costs {productSelection_01[usr_second_cmd]} gold coins.")
            return True
        elif usr_second_cmd in productCode:
            converted = codeRead(usr_second_cmd)
            print(f"We do have that here. It costs {converted} gold coins.")
            return True
        elif usr_second_cmd == "EXIT":
            print("Thank you for stopping by. Come again.")
            return None
        else:
            print("Sorry. We don't have that here.")

def third_cmd(arg1):
    if arg1 == True:
        confirmation = YNConfirmation(arg1)
        if confirmation == True:
            usr_third_cmd = input("\nQuantity: ")
            return True
        else:
            print("\nDiscarded..")
            return second_cmd()
    else:
        return None


print("\nadd  - Browse shop items\nexit - Terminate transaction anytime")

initial = init_cmd()

if initial == True:
    print("\nItem list:")
    for (j, i) in zip(productCode,productSelection_01):
            print(j, i.capitalize())
    print("\nWhat would you like to buy?")
    third_cmd(second_cmd())
else:
    print("Have a nice day.")

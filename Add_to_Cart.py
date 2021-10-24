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

numerical = [1]
code_numerical = [1]

def init_cmd(): #Asks for valid command -- option to either browse or exit.
    while True:
        usr_first_cmd = input("\n> ").lower()
        if usr_first_cmd == "add":
            return True
        elif usr_first_cmd == "exit":
            return "exit_signal"
        else:
            print("\nPlease enter a valid command.")

def codeRead(arg1):
    if arg1 in productCode:
        retriv_product = productCode.get(arg1)
        retreived = productSelection_01.get(retriv_product)
        return retreived

def YNConfirmation(arg1):
    if arg1 == True:
        print("\nWould you like to purchase?")
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
            explicit_prod = productSelection_01[usr_second_cmd]
            numerical.insert(0, explicit_prod)
            print(f"We do have that here. It costs {explicit_prod} gold coins.")
            return "True01"
        elif usr_second_cmd in productCode:
            converted = codeRead(usr_second_cmd)
            code_numerical.insert(0, converted)
            print(f"We do have that here. It costs {converted} gold coins.")
            return "True02"
        elif usr_second_cmd == "EXIT":
            print("Thank you for stopping by. Come again.")
            return None
        else:
            print("Sorry. We don't have that here.")

def quantity_val():
    while True:
        usr_quantity = input("\nQuantity: ")
        if usr_quantity.isdigit() == True:
            return usr_quantity
        else:
            print("Please enter a numerical value.")

def YNConfirm_sepa(arg1):
    if arg1 == "True01":
        return True
    elif arg1 == "True02":
        return True
    else:
        return None

def third_cmd(arg1):
    buy_categ = YNConfirm_sepa(arg1)
    buy_decision = YNConfirmation(buy_categ)
    if buy_decision == True:
        if arg1 == "True01":
            quantity = int(quantity_val())
            ttl_price_of_item01 = quantity*numerical[0]
            numerical.pop(0)
            print(ttl_price_of_item01)
            return ttl_price_of_item01
        elif arg1 == "True02":
            quantity = int(quantity_val())
            ttl_price_of_item02 = quantity*code_numerical[0]
            numerical.pop(0)
            print(ttl_price_of_item02)
            return ttl_price_of_item02
    else:
        print("\nDiscarded..")
        return third_cmd(second_cmd())


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

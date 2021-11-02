import time
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

numerical = [""]
usr_prod_list = [""]
usr_total = [""]
quan = [""]

def init_cmd(arg1): #If there is user input, ask command -- option to either browse or exit.
    if arg1 != None:
        print("\nadd  - Browse shop items\nexit - Terminate transaction anytime")
        while True:
            usr_first_cmd = input("\n> ").lower()
            if usr_first_cmd == "add":
                return True
            elif usr_first_cmd == "exit":
                return "exit_signal"
            else:
                print("\nPlease enter a valid command.")
    else:
        return None

def codeRead(arg1):
    if arg1 in productCode:
        retriv_product = productCode.get(arg1)
        retreived = productSelection_01.get(retriv_product)
        return retreived

def YNConfirmation(arg1):
    if arg1 == True:
        print("\nWould you like to purchase?\n       Yes or No")
        while True:
            usr_decision = input("\n> ").lower()
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
            usr_prod_list.insert(0, usr_second_cmd)
            numerical.insert(0, explicit_prod)
            print(f"We do have that here. It costs {explicit_prod} gold coins.")
            return "True01"
        elif usr_second_cmd in productCode:
            usr_prod_list.insert(0, productCode[usr_second_cmd])
            converted = codeRead(usr_second_cmd)
            numerical.insert(0, converted)
            print(f"We do have that here. It costs {converted} gold coins.")
            return "True02"
        elif usr_second_cmd == "EXIT":
            time.sleep(1)
            print("\nThank you for stopping by. Come again.")
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
            ttl_price_of_item = quantity*numerical[0]
            quan.insert(0, quantity)
            usr_total.insert(0, ttl_price_of_item)
            print(f"The total amount of {usr_prod_list[0]} with the quantity of {quantity} is {ttl_price_of_item} gold coins.")
            return "proceed"
        elif arg1 == "True02":
            quantity = int(quantity_val())
            ttl_price_of_item = quantity*numerical[0]
            quan.insert(0, quantity)
            usr_total.insert(0, ttl_price_of_item)
            print(f"The total amount of {usr_prod_list[0]} with the quantity of {quantity} is {ttl_price_of_item} gold coins.")
            return "proceed"
    elif buy_decision == None:
        return None
    else:
        print("\nDiscarded..")
        numerical.pop(0)
        usr_prod_list.pop(0)
        return third_cmd(second_cmd())

def fourth_cmd(arg1):
    if arg1 != None:
        print("\nWould you like to add this to your cart?\n           Yes or No")
        while True:
            fnl_usr_decision = input("\n> ").lower()
            if fnl_usr_decision == "yes":
                print("Added!")
                return fourth_cmd(third_cmd(second_cmd()))
            elif fnl_usr_decision == "no":
                numerical.pop(0)
                usr_prod_list.pop(0)
                usr_total.pop(0)
                quan.pop(0)
                print("\nDiscarded..")
                return fourth_cmd(third_cmd(second_cmd()))
            else:
                print("Please enter a valid command.")
    else:
        return None

from User_Input import usr_inpt
initial = init_cmd(usr_inpt())

if initial == True:
    print("\nItem list:")
    for (j, i) in zip(productCode,productSelection_01):
            print(j, i.capitalize())
    print("\nWhat would you like to buy?")
    fnl_decision = third_cmd(second_cmd())
    if fnl_decision == "proceed":
        adding_to_crt = fourth_cmd(fnl_decision)
    else:
        None
    #Add here if function for view cart
else:
    print("Have a nice day.")

#Temporary Cart Sys
items_in_cart = len(usr_prod_list)
if items_in_cart > 2:
    print( """\n                     Your Cart
Product:      Price:         Quantity:          Total:\n""")
    for (i,j,x,y) in zip(usr_prod_list[:-1], numerical[:-1], quan[:-1], usr_total[:-1]):
        print(f"{i}       {j} gold coins     {x} pieces      {y} gold coins")
elif items_in_cart == 2:
    print( """\n                     Your Cart
Product:      Price:         Quantity:          Total:\n""")
    for (i,j,x,y) in zip(usr_prod_list[:1], numerical[:1], quan[:1], usr_total[:1]):
        print(f"{i}       {j} gold coins     {x} pieces      {y} gold coins")
else:
    print( """\n                     Your Cart
Product:      Price:         Quantity:          Total:\n""")
    for (i,j,x,y) in zip(usr_prod_list[:0], numerical[:0], quan[:0], usr_total[:0]):
        print(f"{i}       {j} gold coins     {x} pieces      {y} gold coins")
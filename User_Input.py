def usr_inpt():
    query = 0
    while True:
        usr_name = input("Enter your name: ")
        query += 1
        if usr_name != "":
            print(f"Welcome to the shop, {usr_name}!")
            break
        elif query == 5:
            print("Please try again later.")
            return None

usr_inpt()
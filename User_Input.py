import time
def usr_inpt():
    query = 0
    while True:
        usr_name = input("Enter your name: ")
        query += 1
        if usr_name != "":
            for i in "...":
                time.sleep(1)
                print(i)
            print(f"\n\nWelcome to the shop, {usr_name}!")
            return "proceed"
        elif query == 5:
            print("\nPlease try again later.")
            return None
        else:
            print("\nPlease enter a user name.")

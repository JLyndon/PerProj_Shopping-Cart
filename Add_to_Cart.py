def init_cmd(): #Asks for valid command -- option to either browse or exit.
    while True:
        usr_first_cmd = input("\n> ").lower()
        if usr_first_cmd == "add":
            for i in range(1,5+1):
                print(i)
            return "proceed"
        elif usr_first_cmd == "exit":
            return "exit_signal"
        else:
            print("Please enter a valid command.")


print("\nadd  - Browse shop items\nexit - Terminate")

init_cmd()
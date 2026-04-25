def shutdown(choice):
    if choice == "yes":
        return "Shutting down"
    elif choice == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

user_input = input("Do you want to shut down? (yes/no): ").lower()
print(shutdown(user_input))
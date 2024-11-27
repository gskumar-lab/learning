interests = {'gsk': 'fun', 'ravi': 'money', 'suresh': 'power'}

def add_person():
    """Function to add a new person to the dictionary."""
    person = input("Enter the name of the person to add: ").strip()
    if person:
        likes = input(f"Enter the activity for {person}: ").strip()
        if likes:
            interests[person] = likes
            print(f"{person} has been added to the dictionary.")
        else:
            print("Activity cannot be empty.")
    else:
        print("Name cannot be empty.")

def delete_person():
    """Function to delete a person from the dictionary."""
    person = input("Enter the name of the person to delete: ").strip()
    if person:
        if person in interests:
            del interests[person]
            print(f"{person} has been removed from the dictionary.")
        else:
            print(f"{person} not found in the dictionary.")
    else:
        print("Name cannot be empty.")

def display_dictionary():
    """Function to display the current dictionary."""
    if interests:
        print("\nThe Dictionary:")
        print("-" * 30)
        for key, value in interests.items():
            print(f"{key}: {value}")
        print("-" * 30)
    else:
        print("The dictionary is empty.")

def show_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nWelcome to the Dictionary Menu!")
        print("1. Add person")
        print("2. Remove person")
        print("3. Display current dictionary")
        print("Press 'Enter' to exit.")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_person()
        elif choice == '2':
            delete_person()
        elif choice == '3':
            display_dictionary()
        elif choice == '':
            print("Exiting the program.")
            break  # Exit the program if the user presses Enter
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the program
show_menu()

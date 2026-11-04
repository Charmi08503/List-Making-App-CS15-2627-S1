items = []
previous_list = []

while True:
    print("List Making App")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo the Previous Change")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        previous_list = items.copy()

        new_item = input("Enter the item you want to add: ")

        if new_item.strip() == "":
            print("You cannot add an empty item.")
            continue

        items.append(new_item)

        print("Item added successfully.")

    elif choice == "2":

        if len(items) == 0:
            print("Your list is empty.")
            continue

        print("Your List:")

        for i in range(len(items)):
            print(i, "-", items[i])

        try:
            index = int(input("Enter the index of the item you want to remove: "))

            if index < 0 or index >= len(items):
                print("Invalid index. Please try again.")
                continue

            previous_list = items.copy()
            removed_item = items.pop(index)

            print(removed_item, "was removed.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":

        if len(items) == 0:
            print("Your list is empty.")
        else:
            print("Your List:")

            for i in range(len(items)):
                print(i, "-", items[i])

    elif choice == "4":

        if items == previous_list:
            print("There is no previous change to undo.")
        else:
            items = previous_list.copy()
            previous_list = items.copy()
            print("Previous change undone.")

    elif choice == "5":

        print("Thanks for using the List Making App")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
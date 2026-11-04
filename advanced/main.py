todo_list = []
completed_list = []
previous_todo = []
previous_completed = []

while True:
    print("To-Do List App")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display a List")
    print("4. Undo the Previous Change")
    print("5. Replace an Item")
    print("6. Check an Item Off")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        previous_todo = todo_list.copy()
        previous_completed = completed_list.copy()

        new_item = input("Enter the item you want to add: ")

        if new_item.strip() == "":
            print("You cannot add an empty item.")
            continue

        todo_list.append(new_item)

        print("Item added successfully.")

    elif choice == "2":

        if len(todo_list) == 0:
            print("Your to-do list is empty.")
            continue

        print("To-Do List:")

        for i in range(len(todo_list)):
            print(i, "-", todo_list[i])

        try:
            index = int(input("Enter the index of the item you want to remove: "))

            if index < 0 or index >= len(todo_list):
                print("Invalid index. Please try again.")
                continue

            previous_todo = todo_list.copy()
            previous_completed = completed_list.copy()

            removed_item = todo_list.pop(index)

            print(removed_item, "was removed.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":

        print("1. View To-Do List")
        print("2. View Completed List")

        view_choice = input("Which list would you like to view? ")

        if view_choice == "1":

            if len(todo_list) == 0:
                print("Your to-do list is empty.")
            else:
                print("To-Do List:")

                for i in range(len(todo_list)):
                    print(i, "-", todo_list[i])

        elif view_choice == "2":

            if len(completed_list) == 0:
                print("Your completed list is empty.")
            else:
                print("Completed List:")

                for i in range(len(completed_list)):
                    print(i, "-", completed_list[i])

        else:
            print("Invalid choice.")

    elif choice == "4":

        previous_todo_copy = previous_todo.copy()
        previous_completed_copy = previous_completed.copy()

        todo_list = previous_todo_copy
        completed_list = previous_completed_copy

        print("Previous change undone.")

    elif choice == "5":

        if len(todo_list) == 0:
            print("Your to-do list is empty.")
            continue

        print("To-Do List:")

        for i in range(len(todo_list)):
            print(i, "-", todo_list[i])

        try:
            index = int(input("Enter the index of the item you want to replace: "))

            if index < 0 or index >= len(todo_list):
                print("Invalid index. Please try again.")
                continue

            new_item = input("Enter the replacement item: ")

            if new_item.strip() == "":
                print("You cannot enter an empty item.")
                continue

            previous_todo = todo_list.copy()
            previous_completed = completed_list.copy()

            todo_list[index] = new_item

            print("Item replaced successfully.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "6":

        if len(todo_list) == 0:
            print("Your to-do list is empty.")
            continue

        print("To-Do List:")

        for i in range(len(todo_list)):
            print(i, "-", todo_list[i])

        try:
            index = int(input("Enter the index of the item you completed: "))

            if index < 0 or index >= len(todo_list):
                print("Invalid index. Please try again.")
                continue

            previous_todo = todo_list.copy()
            previous_completed = completed_list.copy()

            completed_item = todo_list.pop(index)
            completed_list.append(completed_item)

            print(completed_item, "was moved to your completed list.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "7":

        print("Thanks for using the To-Do List App")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 7.")
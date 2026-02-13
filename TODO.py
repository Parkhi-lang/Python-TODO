# CLI Todo List

# ADD function
def ADD():
    date = input("DATE (DD/MM/YY): ")
    title = input("TITLE: ")
    des = input("DESCRIPTION: ")

    # Write task in structured format
    with open("todo.txt", "a") as file:
        file.write(f"DATE: {date}\n")
        file.write(f"TITLE: {title}\n")
        file.write(f"DESCRIPTION: {des}\n")
        file.write("-" * 30 + "\n")

    print("Task updated successfully.\n")


# VIEW function
def VIEW():
    try:
        with open("todo.txt", "r") as file:
            lines = file.readlines()

            if len(lines) == 0:
                print("YOUR TODO LIST IS EMPTY.\n")
            else:
                for line in lines:
                    print(line, end="")

    except FileNotFoundError:
        print("No todo file found. Your list is empty.\n")


# REMOVE function
def REMOVE(title):
    try:
        with open("todo.txt", "r") as file:
            lines = file.readlines()

        new_lines = []
        skip = False

        for line in lines:
            if line.startswith("TITLE:") and title in line:
                skip = True
                continue

            if skip and line.startswith("-" * 30):
                skip = False
                continue

            if not skip:
                new_lines.append(line)

        with open("todo.txt", "w") as file:
            file.writelines(new_lines)

        print("Task removed (if it existed).\n")

    except FileNotFoundError:
        print("No todo file found.\n")


# MAIN function
def main():
    print("Welcome Sunshine ☀️")

    while True:
        print('''What would you like to do?
1) ADD task
2) REMOVE task
3) VIEW task
Press Enter to Exit
''')

        answer = input("Enter choice: ")

        if not answer:
            break

        match answer:
            case "1" | "ADD" | "add":
                ADD()

            case "2" | "REMOVE" | "remove":
                title = input("TITLE of the task you want to remove: ")
                REMOVE(title)

            case "3" | "VIEW" | "view":
                VIEW()

            case _:
                print("Please enter a valid choice.\n")


if __name__ == "__main__":
    main()

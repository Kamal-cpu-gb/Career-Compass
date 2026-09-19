# Stores the available careers and the details shown to the user.
careers = {
        "Medicine": {
            "Salary": "£40K",
            "Study Years": "5-6 years",
            "Competition": "High"
        },
        "Pharmacy": {
            "Salary": "£35K",
            "Study Years": "4 years",
            "Competition": "Medium"
        },
        "Software Engineering": {
            "Salary": "£50K",
            "Study Years": "3-4 years",
            "Competition": "Medium"
        },
        "Law": {
            "Salary": "£45K",
            "Study Years": "3-4 years",
            "Competition": "High"
        },
        "Chemical Engineer": {
            "Salary": "£55K",
            "Study Years": "4 years",
            "Competition": "Medium"
        }
    }
# Keeps track of user notes and saved favourite careers.
notes_list = []
favourites_list = []

# Displays all career options and lets the user inspect one in detail.
def view_careers():
    print("=== Available careers ===")
    print()

    career_list = list(careers.keys())
    for index, career in enumerate(career_list, start=1):
        print(f"{index}. {career}")

    try:
        view = int(input("Enter a career to view: "))
        if 1 <= view <= len(career_list):
            matched_career = career_list[view - 1]
        else:
            matched_career = None

        if matched_career is not None:
            print(f"\n{matched_career}:")
            for key, value in careers[matched_career].items():
                print(f"{key}: {value}")
            print("1. Add to favourites")
            print("2. Return to main menu")
            try:
                fav_choice = int(input("Choice: "))
                if fav_choice == 1:
                    favourites_list.append(matched_career)
                    print(f"{matched_career} added to favourites.")
                elif fav_choice == 2:
                    return
                else:
                    print("Please enter a valid option")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("Career not found. Please enter a valid career name")
    except ValueError:
        print("Please enter a valid career name")
    


# Compares two careers side by side using the stored information.
def compare_careers():
    print()
    print("=== Compare Careers ===")
    print()

    for index, career in enumerate(careers.keys(), start=1):
        print(f"{index}. {career}")

    print()
    career_list = list(careers.keys())
    try:
        first = int(input("First career to compare: "))
        if 1 <= first <= len(careers):
            matched_first = career_list[first - 1]
        else:
            print("Please enter a valid career number")
            return
        second = int(input("Second career to compare: "))
        print()
        if 1 <= second <= len(careers):
            matched_second = career_list[second - 1]
        else:
            print("Please enter a valid career number")
            return
    except ValueError:
        print("Please enter a valid number")
        return

    print()
    print(f"{matched_first} vs {matched_second}")
    print()
    print("Salary:")
    print(f"{matched_first}: {careers[matched_first]['Salary']}")
    print(f"{matched_second}: {careers[matched_second]['Salary']}")
    print("Study Years:")
    print(f"{matched_first}: {careers[matched_first]['Study Years']}")
    print(f"{matched_second}: {careers[matched_second]['Study Years']}")
    print("Competition:")
    print(f"{matched_first}: {careers[matched_first]['Competition']}")
    print(f"{matched_second}: {careers[matched_second]['Competition']}")
    print()


# Shows the careers the user has marked as favourites.
def favourites():
    print("=== Favourites ===")
    if favourites_list:
        for fav, career in enumerate(favourites_list, start=1):
            print(f"{fav}. {career}")
    else:
        print("No favourites added yet.")


# Handles the note menu: viewing saved notes, adding new ones, or returning.
def notes():
    while True:
        print()
        print("=== Notes ===")
        print("1. View notes")
        print("2. Add note")
        print("3. Return to main menu")
        print()
        try:
            note_choice = int(input("Choice: "))
        except ValueError:
            print("Please enter a valid number")
            return
        if note_choice == 1:
            if notes_list:
                for index, note in enumerate(notes_list, start=1):
                    print(f"{index}. {note}")
            else:
                print("No notes added yet.")
        elif note_choice == 2:
            new_note = input("Enter your note: ")
            notes_list.append(new_note)
            print("Note added.")
            print()
            continue
        elif note_choice == 3:
            break
        else:
            print("Please enter a valid option")

while True:
    print()
    print("===Career Compass ===")
    print("1. View all careers")
    print("2. Compare careers")
    print("3. Favourites")
    print("4. Notes")
    print("5. Exit")
    print()

    try:
        choice = int(input("Choice: "))
        print()

        if choice == 1:
            view_careers()
        elif choice == 2:
            compare_careers()
        elif choice == 3:
            favourites()
        elif choice == 4:
            notes()
        elif choice == 5:
            break
        else:
            print("Please enter a valid option")
    except ValueError:
        print("Please enter a valid number")

    
# Available career options shown to the user in the menu.
careers = [
    "Software Engineering",
    "Data Analysis",
    "UI/UX Design",
    "Cybersecurity"
]

# Each career has a roadmap of skills that the user can explore.
roadmaps = {
    "Software Engineering": [
        "Python",
        "JavaScript",
        "Functions",
        "Object-Oriented Programming",
        "Git",
        "SQL",
        "REST APIs",
        "Web Development"
    ],
    "Data Analysis": [
        "Python",
        "SQL",
        "Statistics",
        "Pandas",
        "Excel",
        "Data Visualization",
        "Tableau",
        "R Programming"
    ],
    "UI/UX Design": [
        "Figma",
        "Adobe XD",
        "Wireframing",
        "Prototyping",
        "User Research",
        "Color Theory",
        "Typography",
        "Responsive Design"
    ],
    "Cybersecurity": [
        "Network Security",
        "Cryptography",
        "Firewalls",
        "Penetration Testing",
        "Linux",
        "Ethical Hacking",
        "Threat Analysis",
        "Security Protocols"
    ]
}

career_descriptions = {
    "Software Engineering": "Designs and builds software applications, websites, and systems using programming languages.",
    "Data Analysis": "Uses data to find patterns, create reports, and help businesses make better decisions.",
    "UI/UX Design": "Creates user-friendly designs and improves how people interact with digital products.",
    "Cybersecurity": "Protects computer systems, networks, and data from cyber threats."
}

skill_resources = {
    "Python": "https://www.youtube.com/",
    "JavaScript": "https://www.youtube.com/",
    "SQL": "https://www.youtube.com/",
    "Git": "https://www.youtube.com/"
}
# Stores the current career chosen by the user.
selected_career = None

# Main menu loop that keeps the program running until the user exits.
while True:
    # Show the list of available careers.
    for index, career in enumerate(careers):
        print(f"{index + 1}. {career}")
    print("5. Exit")
    print("6. View all careers again")

    try:
        choice = int(input("Choice:"))

        # Select a career from the list.
        if 1 <= choice <= 4:
            selected_career = careers[choice - 1]
            print(f"You selected {selected_career}")

        # Exit the program.
        if choice == 5:
            break

        # Re-display the career list.
        if choice == 6:
            print("Here are the careers: ")
            for index, career in enumerate(careers):
                print(f"{index + 1}. {career}")

        # If a career was selected, show its roadmap skills.
        if selected_career != None:
            description = career_descriptions[selected_career]
            skills = roadmaps[selected_career]

            print(f"\n=== {selected_career} ===")
            print(f"Description: {description}")

            print("\nSkills:")
            for index, skill in enumerate(skills):
                print(f"{index + 1}. {skill}")

            # Let the user choose a skill from the selected roadmap.
            try:
                skill_choice = int(input("Choose a skill: "))
                if 1 <= skill_choice <= len(skills):
                    selected_skill = skills[skill_choice - 1]
                    print(f"You selected: {selected_skill}")
                    resource = skill_resources[selected_skill]
                    print(f"Resource for {selected_skill}: {resource}")
                else:
                    print("Please enter a valid skill number")
            except ValueError:
                print("Please enter a number")
    except ValueError:
        print("Please enter a number")
    except IndexError:
        print("Please enter within correct range")
from tkinter import *

root = Tk()
root.title("Career Compass")
root.geometry("420x360")
root.configure(bg="#f3f6ff")

result_text = StringVar()
result_text.set("")


def medicine_button_clicked():
    result_text.set("Medicine Selected")


def software_button_clicked():
    result_text.set("Software Selected")


def law_button_clicked():
    result_text.set("Law Selected")


def search_button_clicked():
    search_query = search.get().strip()
    if search_query:
        result_text.set(f"Search Query: {search_query}")
    else:
        result_text.set("Please enter a search query")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

career_compass = Label(
    root,
    text="Career Compass",
    font=("Arial", 18, "bold"),
    bg="#f3f6ff",
    fg="#1f3c88",
)
career_compass.grid(row=0, column=0, columnspan=2, pady=(20, 10))

search_frame = Frame(root, bg="#f3f6ff")
search_frame.grid(row=1, column=0, columnspan=2, pady=(5, 15))

search = Entry(search_frame, width=24)
search.grid(row=0, column=0, padx=(0, 8))

search_button = Button(
    search_frame,
    text="Search",
    width=10,
    command=search_button_clicked,
    bg="#4c6ef5",
    fg="white",
)
search_button.grid(row=0, column=1)

button_frame = Frame(root, bg="#f3f6ff")
button_frame.grid(row=2, column=0, columnspan=2)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

Medicine = Button(
    button_frame,
    text="Medicine",
    width=18,
    height=2,
    command=medicine_button_clicked,
    bg="#ffffff",
    fg="#1f3c88",
)
Medicine.grid(row=0, column=0, padx=10, pady=8)

Software = Button(
    button_frame,
    text="Software Engineering",
    width=18,
    height=2,
    command=software_button_clicked,
    bg="#ffffff",
    fg="#1f3c88",
)
Software.grid(row=0, column=1, padx=10, pady=8)

Law = Button(
    button_frame,
    text="Law",
    width=18,
    height=2,
    command=law_button_clicked,
    bg="#ffffff",
    fg="#1f3c88",
)
Law.grid(row=1, column=0, columnspan=2, padx=10, pady=8)

result_label = Label(
    root,
    textvariable=result_text,
    font=("Arial", 12),
    bg="#f3f6ff",
    fg="#2f3e46",
)
result_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

root.mainloop()

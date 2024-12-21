from tkinter import Entry, StringVar, Tk, Button, Label

from yoruba_dic_module import yoruba_dictionary
from igbo_dic_module import igbo_dictionary

window = Tk()
window.geometry("600x400")
window.title("Multi-Language Dictionary")

languages = {"Yoruba": yoruba_dictionary,
             "Igbo": igbo_dictionary}

language_label = Label(window, text="Select a Language:", font=("Arial", 16))
language_label.pack(pady=20)

def show_search_interface(language):

    for widget in window.winfo_children():
        widget.destroy()

    Label(window, text=f"{language} Dictionary", font=("Arial", 18)).pack(pady=10)
    entry_text = Entry(window, font=("Arial", 14))
    entry_text.pack(pady=10)

    result = StringVar()
    result_label = Label(window, textvariable=result, font=("Arial", 16), fg="blue")
    result_label.pack(pady=10)

    def search():
        word = entry_text.get().lower()
        dictionary = languages[language]
        if word in dictionary:
            result.set(dictionary[word])
        else:
            result.set("Not Found")

    search_btn = Button(window, text="Search", command=search, font=("Arial", 14))
    search_btn.pack(pady=10)


    Button(window, text="Back", command=display_language_options, font=("Arial", 12)).pack(pady=10)


def display_language_options():

    for widget in window.winfo_children():
        widget.destroy()

    language_label = Label(window, text="Select a Language:", font=("Arial", 16))
    language_label.pack(pady=20)

    for language in languages.keys():
        Button(
            window,
            text=language,
            command=lambda lang=language: show_search_interface(lang),
            font=("Arial", 14),
            width=15,
        ).pack(pady=10)

display_language_options()

window.mainloop()
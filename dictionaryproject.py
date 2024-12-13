from tkinter import Entry, StringVar, Tk, Button, Label, OptionMenu, Radiobutton

from yoruba_dic_module import yoruba_dictionary

window = Tk()
window.geometry("600x300")
window.title("Language Translator")

languages = {"Yoruba": yoruba_dictionary}
selected_language = StringVar()
selected_language.set("Yoruba")

language_label = Label(window, text="SELECT A LANGUAGE:", font=("Arial", 12))
language_label.pack(pady=10)

for language in languages.keys():
    Radiobutton(
        window,
        text=language,
        variable=selected_language,
        value=language,
        font=("Arial", 12)
    ).pack(anchor="w")

entry_text = Entry(window, font=("Arial", 14))
entry_text.pack(pady=10)

result = StringVar()
result_label = Label(window, textvariable=result, font=("Arial", 16), fg="blue")
result_label.pack(pady=10)

def search():
    word = entry_text.get().lower()
    language = selected_language.get()
    dictionary = languages[language]

    if word in dictionary:
        result.set(dictionary[word])
    else:
        result.set("Not Found")

search_btn = Button(window, text="Search", command=search)
search_btn.pack(pady=10)

window.mainloop()
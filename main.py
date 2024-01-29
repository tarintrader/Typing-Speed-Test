from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st
from words import words_list
import random
import time

words = random.sample(words_list, 120)
index = 0
count = 60
clicks = 0
correct_words = 0
correct_clicks = 0

root = Tk()
root.geometry("707x550")
root.title("Typing Speed Test")
root.configure(bg="#393E46")
root.iconbitmap("icon.ico")

frm = ttk.Frame(root, padding=200)
frm.grid()

time_label = Label(root, text=f"Time: {count}", font="Courier 16", bg="#393E46", fg="#00E5CF")
time_label.grid(row=0, column=0, pady=15)

correct_cpm_label = Label(root, text="CPM:", font="Courier 16", bg="#393E46", fg="#00E5CF")
correct_cpm_label.grid(row=0, column=1)

wpm_label = Label(root, text="WPM:", font="Courier 16", bg="#393E46", fg="#00E5CF")
wpm_label.grid(row=0, column=2)


def restart():
    global words, index, count, clicks, correct_words, correct_clicks
    root.after_cancel(timer)
    words = random.sample(words_list, 120)
    index = 0
    count = 60
    clicks = 0
    correct_words = 0
    correct_clicks = 0
    time_label.config(text=f"Time: {str(count)}")
    correct_cpm_label.configure(text="CPM:")
    wpm_label.configure(text="WPM:")
    entry.grid(row=3, column=1, columnspan=2, pady=30)
    entry.focus_set()
    result_label.configure(text="")

    # Update the text_area with the new words
    text_area.configure(state='normal')  # Re-enable the text_area
    text_area.delete("1.0", "end")
    # Insert each word as a separate taggable entity
    for word in words:
        text_area.insert(INSERT, f"{word} ", f"{word}_tag")

    text_area.configure(state='disabled')  # Disable the text_area again



restart_button = Button(root, text="Restart", font=("Courier 16"), command=restart, bg="#393E46", fg="#00E5CF")
restart_button.grid(row=0, column=3)

# Creating scrolled text area
# widget with Read only by
# disabling the state
text_area = Text(root,
                 width=60,
                 height=12,
                 font=("Times New Roman", 16),
                 wrap=WORD,
                 bg="#222831",
                 fg="#EEEEEE"
                 )

text_area.grid(row=1, column=0, columnspan=4, padx=20, pady=10)

# Insert each word as a separate taggable entity
for word in words:
    text_area.insert(INSERT, f"{word} ", f"{word}_tag")

text_area.configure(state='disabled')  # Disable the text_area again

# Making the text read only
text_area.configure(state='disabled')

result_label = Label(root, text="", font=("Courier 14 bold"), bg="#393E46", fg="yellow")
result_label.grid(row=2, column=0, columnspan=4, pady=30)

entry = Entry(root, width=40, font=("Times New Roman", 14), bd=5)
entry.focus_set()
entry.grid(row=3, column=1, columnspan=2, pady=30)


def new_word(event=None):
    print(index)
    value = entry.get().rstrip()
    print(value)
    entry.delete(0, 'end')
    check_word(value)
    change_color()


def check_word(value, event=None):
    global index, correct_words, correct_clicks

    # Find the starting index of the current word in the text_area
    start_index = text_area.search(words[index], "1.0", END)

    if start_index:
        # Calculate the ending index of the current word
        end_index = f"{start_index}+{len(words[index])}c"

        # Check if the typed word matches the current word in the text_area
        if value == words[index]:
            correct_words += 1
            correct_clicks += len(value)
            # Tag the correct word in green
            text_area.tag_add("correct", start_index, end_index)
            text_area.tag_configure("correct", foreground="#41E600")
        else:
            # Tag the incorrect word in red
            text_area.tag_add("incorrect", start_index, end_index)
            text_area.tag_configure("incorrect", foreground="red")

        index += 1
        print(count)


def change_color(event=None):
    pass


def count_down(count):
    print("timer")
    time_label.configure(text=f"Time: {str(count)}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
        correct_cpm_label.configure(text=f"CPM: {int(correct_clicks * 60 / (60 - count))}")
        wpm_label.configure(text=f"WPM: {int(correct_words * 60 / (60 - count))}")
    else:
        entry.grid_forget()
        result_label.configure(text=f"Your score: {correct_clicks} CPM (that is {correct_words} WPM)")


def click_count(event=None):
    global clicks
    clicks += 1
    print(clicks)
    if clicks > 1:
        pass
    elif clicks > 0:
        count_down(count)


def start_timer():
    if clicks != 0:
        count_down(count)


root.bind_all('<Key>', click_count)
root.bind("<space>", new_word)
root.mainloop()

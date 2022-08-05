import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    Question=simpledialog.askstring('title', 'Can you ask a question?')
    # Make a variable and initialize it to a random number between 0 and 3
    random_num=random.randint(0,3)
    # If the random number is 0
    if random_num==0:
        messagebox.showinfo('title','Yes')
        # tell the user "Yes"

    # If the random number is 1
    elif random_num==1:
        messagebox.showinfo('title','No')
        # tell the user "No"

    # If the random number is 2
    elif random_num==2:
        messagebox.showinfo('title','Maybe you should ask Google?')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    else:
        messagebox.showinfo('title', 'Maybe you should go to the library to research on your question.')
        # write your own answer
    window.mainloop()
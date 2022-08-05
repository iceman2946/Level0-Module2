import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()




    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        random_number = random.randint(1, 5)
        print(random_number)
        if random_number==1:
            messagebox.showinfo('title', 'You are so kind!')
        elif random_number==2:
            messagebox.showinfo('title', 'You are so funny!')
        elif random_number==3:
            messagebox.showinfo('title','You are so friendly!')
        elif random_number==4:
            messagebox.showinfo('title','You are so amazing! ')
        else:
            messagebox.showinfo('title','You are so smart!')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)

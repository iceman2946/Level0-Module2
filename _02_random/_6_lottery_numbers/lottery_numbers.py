import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    number1= random.randint(0,9)
    number2= random.randint(0,9)
    number3= random.randint(0,9)
    number4= random.randint(0,9)
    number5= random.randint(0,9)
    number6= random.randint(0,9)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo('Lottery Ticket', str(number1)+ str(number2)+ str(number3)+ str(number4) + str(number5)+ str(number6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket

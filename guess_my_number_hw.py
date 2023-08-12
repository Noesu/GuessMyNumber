# Задание. Перепишите игру «Отгадай число» из главы 3,
# создайте для нее графический интерфейс.
#
# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
#
# import random
#
# print("\tWelcome to 'Guess My Number'!")
# print("\nI'm thinking of a number between 1 and 100.")
# print("Try to guess it in as few attempts as possible.\n")
#
# # set the initial values
# the_number = random.randint(1, 100)
# guess = int(input("Take a guess: "))
# tries = 1
#
# # guessing loop
# while guess != the_number:
#     if guess > the_number:
#         print("Lower...")
#     else:
#         print("Higher...")
#
#     guess = int(input("Take a guess: "))
#     tries += 1
#
# print("You guessed it!  The number was", the_number)
# print("And it only took you", tries, "tries!\n")
#
# input("\n\nPress the enter key to exit.")

import random
from tkinter import *


class Application(Frame):
    """ GUI application """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.guess = None
        self.output_field = None
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Строка 1. Вступление.
        Label(self,
              text="Welcome to 'Guess My Number'!\n"
                   "I'm thinking of a number between 1 and 100.\n"
                   "Try to guess it in as few attempts as possible.\n"
              ).grid(row=0, column=0, columnspan=3, sticky=W)

        # Строка 2. Ввод значения.
        Label(self,
              text="Take a guess:"
              ).grid(row=1, column=0, sticky=W)

        self.guess = Entry(self)
        self.guess.grid(row=1, column=1, sticky=W)

        Button(self,
               text="Enter",
               command=self.input_number
               ).grid(row=1, column=2, sticky=W)

        # Строка 3. Вывод результатов.
        Label(self, text="\n").grid(row=2, column=0, columnspan=3, sticky=W)
        self.output_field = Text(self, width=40, height=3, wrap=WORD)
        self.output_field.grid(row=3, column=0, columnspan=3)

    def input_number(self):
        global tries
        rezultat = None
        guess = int(self.guess.get())
        if 1 < guess < 100:
            tries += 1
            rezultat = self.check_number(guess)
        self.output_field.delete(0.0, END)
        self.output_field.insert(0.0, rezultat)

    def check_number(self, guess):
        if guess > the_number:
            rezultat = "Lower..."
        elif guess < the_number:
            rezultat = "Higher..."
        else:
            rezultat = self.victory()
        return rezultat

    @staticmethod
    def victory():
        rezultat = "You guessed it!  The number was "
        rezultat += str(the_number)
        rezultat += ", and it only took you "
        rezultat += str(tries)
        rezultat += " tries!"
        return rezultat


# main
the_number = random.randint(1, 100)
tries = 1
root = Tk()
root.title("Guess My Number!")
app = Application(root)
root.mainloop()

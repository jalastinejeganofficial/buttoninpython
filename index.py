from tkinter import *
root=Tk()
root.title("Simple Calculator JJ")
button = Button(root, text="Click me!", width=200)
#To Display a Button using two Ways
button.pack() #pack use to Display the button in center.
button.grid(row=0, column=0) #grid use to set row and column to where is Display

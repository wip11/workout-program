from tkinter import *
import random

root = Tk()
root.title('Workout   10 reps   2 sets')
root.geometry("500x500")

# Listbox!
my_listbox = Listbox(root, height=20, width=50)
my_listbox.pack()

ent = Entry(root, width=50)
ent.pack()

# Lists
warmup = ['jack knife', 'jump rope']
warmup2 = ['jumping jacks', 'break dance']
push = ['push ups', 'db floor presses']
push2 = ['push ups', 'db floor presses']
pull = ['standing db row', 'sled pull']
legs = ['squat', 'reverse nordic', 'nordic ham curl']
legs2 = ['split squat', 'hip thrusters']
press = ['shoulder press', 'arnold press']
ballistic = ['overhead throw', 'weighted jumps', 'weighted box jumps', 'shot put', 'lateral bounds']
full_body = ['turkish getup', 'man makers', 'romanian dead lift']
auxiliary = ['shoulder exo rotation', 'airplanes', 'heel lifts']
auxiliary2 = ['bent over rear deltoid',  'knee lifts', 'tibialis']
speed = ['ali shuffle', 'speed ladder snake']
speed2 = ['icky shuffle', 'hop-scotch']
ab = ['slam ball', 'crunch press']
ab2 = ['paloff press', 'hundred']
erectors = ['prone cobra']
erectors2 = ['back extensions']





# Random selections
my_listbox.insert(0, (random.choice(warmup)))
my_listbox.insert(END, (random.choice(warmup2)))
my_listbox.insert(END, (random.choice(push)))
my_listbox.insert(END, (random.choice(pull)))
my_listbox.insert(END, (random.choice(legs)))
my_listbox.insert(END, (random.choice(press)))
my_listbox.insert(END, (random.choice(full_body)))
my_listbox.insert(END, (random.choice(auxiliary)))
my_listbox.insert(END, (random.choice(ballistic)))
my_listbox.insert(END, (random.choice(push2)))
my_listbox.insert(END, (random.choice(legs2)))
my_listbox.insert(END, (random.choice(auxiliary2)))
my_listbox.insert(END, (random.choice(speed)))
my_listbox.insert(END, (random.choice(speed2)))
my_listbox.insert(END, (random.choice(ab)))
my_listbox.insert(END, (random.choice(erectors)))
my_listbox.insert(END, (random.choice(ab2)))
my_listbox.insert(END, (random.choice(erectors2)))





# Buttons

def adder():
    my_listbox.insert(END, ent.get())
    ent.delete(0, END)

my_button3 = Button(root, text='Add', command=adder)
my_button3.pack()


def delete():
    my_listbox.delete(ANCHOR)

my_button = Button(root, text='Delete', command=delete)
my_button.pack()





root.mainloop()

import random
import tkinter
import tkinter.messagebox

top = tkinter.Tk()
Modlabel = tkinter.Label(top, text="Initial Attack Modifier")
Modlabel.pack()
Modenter = tkinter.Entry(top)
Modenter.pack()
Numlabel = tkinter.Label(top, text="Number of Attacks")
Numlabel.pack()
Numenter= tkinter.Entry(top)
Numenter.pack()
typelabel = tkinter.Label(top, text="Attack Type")
attackSelect = tkinter.StringVar(top)
attackSelect.set("Good")
attacks = tkinter.OptionMenu(top, attackSelect, "Good", "Average", "Bad")
attacks.pack()

def multiroller(initmod, attacknum, type):
		i = 0
		final = ''
		while i < attacknum:
			dice = random.randrange(20) + 1
			result = dice + initmod
			final = final + '\n (' + str(dice) + ') ' + str(result)
			print('(' + str(dice) + ')', result)
			i = i + 1
			if type == 'Bad':
				initmod = initmod - 6
			elif type == 'Average':
				initmod = initmod - 4
			elif type == 'Good':
							initmod = initmod - 2
		return final
# multiroller(10,3,"heavy")

def attacker():
	if str.isdigit(Modenter.get()) != True:
		tkinter.messagebox.showinfo("Error", "Please input a number for the modifier")
	elif str.isdigit(Numenter.get()) != True or int(Numenter.get()) < 1:
		tkinter.messagebox.showinfo("Error", "Please input a positive number for the number of attacks")
	else:
		tkinter.messagebox.showinfo("Result", multiroller(int(Modenter.get()), int(Numenter.get()), attackSelect.get()))
		print(attackSelect.get())
		multiroller(int(Modenter.get()), int(Numenter.get()), attackSelect.get())


b = tkinter.Button(top, text = "Attack!", command = attacker)
b.pack()
top.mainloop()
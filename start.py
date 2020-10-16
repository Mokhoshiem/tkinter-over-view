import tkinter as tk
initial_text = '''
first import tkinter as tk alliace
then create the root window of the whole program using Tk()
method and remember T is upper case
at the end of the program never forget to mainloop
root.mailoop()
'''
root = tk.Tk()

label_text = ''' label widget:
first assign the label
after that show it using pack(), grid() or display()
'''
main_label = tk.Label(root, text=initial_text + '\n' + label_text)
main_label.pack()



root.mainloop()

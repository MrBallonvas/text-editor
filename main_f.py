import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import tkinter.messagebox

root = tk.Tk()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w = screen_w-15
h = screen_h-85

resolution = str(w)+'x'+str(h)

root.geometry(resolution)

menu = Menu(root)


def Open():
	filename1 = filedialog.askopenfilename()
	file1 = open(filename1, 'r', encoding='utf8')

	message_text.delete("1.0", tk.END)
	
	for l in file1:
		message_text.insert(tk.END, l)

	file1.close()
	fileopen = Label(text=str(filename1), bg='yellow').grid(column=1, row=1)
	btn_cls = tk.Button(text="Х", command=lambda: btn_cls_func()).grid(column=3, row=1)

	def btn_cls_func():
		fileopen(text='').grid(column=1, row=1)
		message_text.delete('1.0', tk.END)

def Save():
	file = asksaveasfile(
		mode='w',
		defaultextension=".txt",
		filetypes=(("text", "*.txt"), ("Python", ".py"), ("All files", "*"))	
		)

	text_for_save = message_text.get("1.0", tk.END)
	file.write(text_for_save)

	file.close()


new_item = Menu(menu)
new_item.add_command(label='Открыть', command=lambda: Open())
new_item.add_command(label='Сохранить', command=lambda: Save())
new_item.add_command(label='Выйти', command=lambda: root.destroy())
menu.add_cascade(label='Файл', menu=new_item)
root.config(menu=menu)

message_text = Text(bg='light cyan', fg='black')
message_text.place(relx=.5, rely=.5, anchor="c", height=h-100, width=w-30)

root.mainloop()

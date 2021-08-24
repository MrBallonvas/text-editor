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
	fileopen = Label(text=str(filename1), bg='yellow')
	fileopen.grid(column=1, row=1)
	btn_cls = tk.Button(text="Х", command=lambda: btn_cls_func())
	btn_cls.grid(column=3, row=1)

	def btn_cls_func():
		win_ext = Tk()

		label_ext = tk.Label(win_ext, text='Вы действительно хотите выйти?')
		label_ext.pack()
		frame = Frame(win_ext)
		#yes_ext = tk.Button(frame,text='Да', command=lambda:ext).pack(side='right')
		#no_ext = tk.Button(frame,text='Нет', command=lambda:win_ext.destroy()).pack(side='left')
		yes_ext = tk.Button(frame,text='Да', command=lambda:ext()).grid(padx=10, column=1, row=0 , pady=2 , sticky="nsew")
		no_ext = tk.Button(frame,text='Нет', command=lambda:win_ext.destroy()).grid( row=0, padx=10 , pady=2 , sticky="nsew")
		frame.pack()

		def ext():
			btn_cls.destroy()
			
			try:
				Save()
			except AttributeError as error_data:
				pass

			fileopen.destroy()
			win_ext.destroy()
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

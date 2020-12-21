run=6

if (1==run):
	import tkinter
	from tkinter import Label, Button, Entry
	from tkinter import *
	from tkinter.ttk import *
	print("Test một vài chức năng của winform, không có gì đặc biệt")
	window=tkinter.Tk()
	window.title("GUI")
	window.geometry('640x480')

	label=tkinter.Label(window,text="Hello world!")
	l1=Label(window,text="Tuấn Anh!", font=("Arial Bold", 20)) 
	l1.grid(column=100,row=20)

	txt=Entry(window,width=10)
	txt.grid(column=1,row=0)
	def clicked():
		res="Welcome to "+ txt.get()
		l1.configure(text=res)
	bt=Button(window,text="enter", command=clicked)
	bt.grid(column=30,row=30)


	combo=Combobox(window)
	combo['values']=(1,2,3,4,5,'text')
	combo.current(3)
	combo.grid(column=0,row=40)

	img=PhotoImage(file="imgs/anh5.gif")
	label=Label(window,image=img)
	label.grid(column=0,row=0)
	window.mainloop()
if (2==run):
	# import Tkinter as tk # Python 2
	import tkinter as tk # Python 3
	from tkinter import *
	print("Hướng dẫn: tạo 1 folder có ảnh: ./imgs/anh5.gif rồi chạy, click chuột phải vào ảnh form sẽ thoát")
	root = tk.Tk()
	# The image must be stored to Tk or it will be garbage collected.
	# def btnClick():
	# 	exit(0)
	# bt=tk.Button(root,text="Exit", command=btnClick).pack()
	def close_window(x=None): 
		root.destroy()
	def change_position(root_variable,x,y):
		root_variable.geometry('+{}+{}'.format(x,y))

	root.image = tk.PhotoImage(file='imgs/anh5.gif')
	label = tk.Label(root, image=root.image, bg='white') #, command=close_window)
	label.bind("<Button-3>",close_window)
	
	root.overrideredirect(True)
	root.geometry("+250+250")
	# change_position()
	root.lift()
	root.wm_attributes("-topmost", True)
	# root.wm_attributes("-disabled", True)
	root.wm_attributes("-transparentcolor", "white")
	label.pack()
	
	
	label.mainloop()
if (3==run):
	import tkinter as tk
	# root = tk.Tk()
	print(" Chạy cái này sẽ lên 2 form, ở góc trên trái, bấm vào kéo dê cái đó đi được")
	class App(tk.Tk):
		def __init__(self):
			root=tk.Tk.__init__(self)
			self.floater = FloatingWindow(self,root)

	class FloatingWindow(tk.Toplevel):
		def __init__(self, root, *args, **kwargs):
			tk.Toplevel.__init__(self, *args, **kwargs)
			self.overrideredirect(True)
			self.lift()
			self.label = tk.Label(self, text="Click on the grip to move")
			self.grip = tk.Label(self, bitmap="gray25")
			self.grip.pack(side="left", fill="y")
			self.label.pack(side="right", fill="both", expand=True)

			self.grip.bind("<ButtonPress-1>", self.start_move)
			self.grip.bind("<ButtonRelease-1>", self.stop_move)
			self.grip.bind("<B1-Motion>", self.do_move)
			root.overrideredirect(False)
			self.wm_attributes("-topmost", True)
			self.wm_attributes("-transparentcolor", "white")
	
	

		def start_move(self, event):
			self.x = event.x
			self.y = event.y

		def stop_move(self, event):
			self.x = None
			self.y = None

		def do_move(self, event):
			deltax = event.x - self.x
			deltay = event.y - self.y
			x = self.winfo_x() + deltax
			y = self.winfo_y() + deltay
			self.geometry(f"+{x}+{y}")

	app=App()
	app.mainloop()
if (4==run):
	import tkinter as tk # Python 3
	from tkinter import *
	# root = tk.Tk()
	print("Chạy cái này sẽ hiện ảnh lên, Lclick sẽ (un)transparent form, Rclick sẽ close_window")
	def change_position(root_variable,x,y):
		root_variable.geometry('+{}+{}'.format(x,y))

	class App(tk.Tk):
		def __init__(self):
			self.root=tk.Tk.__init__(self)
			self.floater = FloatingWindow(self,self.root)

	class FloatingWindow(tk.Toplevel):
		def __init__(self, root, *args, **kwargs):
			root.image = tk.PhotoImage(file='imgs/anh5.gif')

			label = tk.Label(root, image=root.image, bg='white') #, command=close_window)
			label.bind("<Button-3>",self.close_window)
			label.bind("<Button-1>",self.trans)

			# label.bind("<ButtonPress-1>", self.start_move)
			# label.bind("<ButtonRelease-1>", self.stop_move)
			# label.bind("<B1-Motion>", self.do_move)

			# root.overrideredirect(True)
			root.geometry("+250+250")
			root.lift()
			root.wm_attributes("-topmost", True)
			# root.wm_attributes("-disabled", True)
			# root.wm_attributes("-transparentcolor", "white")
			label.pack()
			self.root=root
			self.trans_flag=False
		def close_window(self,event):
			self.root.destroy()

		def trans(self,event):
			if self.trans_flag:
				self.trans_flag=False
				self.root.overrideredirect(0)
				self.root.wm_attributes("-transparentcolor", None)
			else:
				self.trans_flag=True
				self.root.overrideredirect(1)
				self.root.wm_attributes("-transparentcolor", "white")
			
		def start_move(self, event):
			self.x = event.x
			self.y = event.y

		def stop_move(self, event):
			self.x = None
			self.y = None

		def do_move(self, event):
			deltax = event.x - self.x
			deltay = event.y - self.y
			x = self.winfo_x() + deltax
			y = self.winfo_y() + deltay
			self.geometry(f"+{x}+{y}")
	app=App()
	app.mainloop()
if (5==run):
	import tkinter as tk
	from tkinter import ttk
	print("chạy cái này sẽ resize được form")
	class Example(tk.Tk):
		def __init__(self):
			r=tk.Tk.__init__(self)


			self.floater = FloatingWindow(self)

	class FloatingWindow(tk.Toplevel):
		def __init__(self, *args, **kwargs):
			tk.Toplevel.__init__(self, *args, **kwargs)
			self.overrideredirect(True)
			self.wm_geometry("400x400")

			self.label = tk.Label(self, text="Grab the lower-right corner to resize")
			self.label.pack(side="top", fill="both", expand=True)

			self.grip = ttk.Sizegrip(self)
			self.grip.place(relx=1.0, rely=1.0, anchor="se")
			self.grip.lift(self.label)
			self.grip.bind("<B1-Motion>", self.OnMotion)


		def OnMotion(self, event):
			x1 = self.winfo_pointerx()
			y1 = self.winfo_pointery()
			x0 = self.winfo_rootx()
			y0 = self.winfo_rooty()
			self.geometry("%sx%s" % ((x1-x0),(y1-y0)))
			return

	app=Example()
	app.mainloop()	
if (6==run):
	import tkinter as tk # Python 3
	from tkinter import *
	print("Chạy cái này sẽ transparent form, Lclick & drag để dê form ra chỗ khác, Rclick sẽ close_window")
	def change_position(root_variable,x,y):
		root_variable.geometry('+{}+{}'.format(x,y))

	class App(tk.Tk):
		def __init__(self):
			self.root=tk.Tk.__init__(self)
			self.floater = FloatingWindow(self,self.root)

	class FloatingWindow(tk.Toplevel):
		def __init__(self, root, *args, **kwargs):
			root.image = tk.PhotoImage(file='imgs/anh5.gif')			
			label = tk.Label(root, image=root.image, bg='white') #, command=close_window)
			label.bind("<Button-3>",self.close_window)
			# label.bind("<Button-1>",self.trans)
			root.overrideredirect(1)
			root.wm_attributes("-transparentcolor", "white")
				
			label.bind("<ButtonPress-1>", self.start_move)
			label.bind("<ButtonRelease-1>", self.stop_move)
			label.bind("<B1-Motion>", self.do_move)

			root.geometry("+250+250")
			root.lift()
			root.wm_attributes("-topmost", True)
			label.pack()
			self.root=root
			self.trans_flag=False
			self.x0=250
			self.y0=250
		def close_window(self,event):
			self.root.destroy()

		def trans(self,event):
			if self.trans_flag:
				self.trans_flag=False
				self.root.overrideredirect(0)
				self.root.wm_attributes("-transparentcolor", None)
			else:
				self.trans_flag=True
				self.root.overrideredirect(1)
				self.root.wm_attributes("-transparentcolor", "white")
				# root.wm_attributes("-disabled", True)
			
		def start_move(self, event):
			self.x = event.x
			self.y = event.y

		def stop_move(self, event):
			self.x = None
			self.y = None

		def do_move(self, event):
			deltax = event.x - self.x
			deltay = event.y - self.y
			self.x0+=deltax
			self.y0+=deltay
			change_position(self.root,self.x0,self.y0)
	app=App()
	app.mainloop()


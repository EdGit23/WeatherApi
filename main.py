import tkinter as tk
import tkinter.ttk as ttk

class MyApp(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title('Weather API Interface')
		self.resizable(False,False)
		self.geometry(('500x250'))
		self.myVar = tk.IntVar()

		#Create Frames for the widgets
		self.frame1 = tk.Frame(self)
		self.frame2 = tk.Frame(self)
		self.frame3 = tk.Frame(self)

		#Put the frames on to the display
		self.frame1.grid(row=0, column=0, padx=20, pady=20)
		self.frame2.grid(row=0, column=1, sticky='n', pady=(15,0))
		self.frame3.grid(row=1, column=0, columnspan=2, sticky='w', padx=(20,0))

		#Widgets placed on frame1
		self.myLabel = ttk.Label(self.frame1, text='Enter Name of Location:')
		self.myLabel.grid(row=0,column=0, sticky='w')
		self.entry_widget = ttk.Entry(self.frame1, width=30)
		self.entry_widget.grid(row=1, column=0, pady=(10,0))
		self.fetch_button = ttk.Button(self.frame1, text='Fetch')
		self.fetch_button.grid(row=2, column=0, sticky='w', pady=(10,0))
		self.parse_button = ttk.Button(self.frame1, text='Parse')
		self.parse_button.grid(row=2, column=0, padx=(100,0), pady=(10,0))
		ttk.Label(self.frame1, text='UNITS').grid(row=3,column=0, sticky='w', pady=(20,0))
		ttk.Radiobutton(self.frame1, text='Imperial', variable=self.myVar, value=1).grid(row=4, column=0, sticky='w', pady=(10,0))
		ttk.Radiobutton(self.frame1, text='Metric', variable=self.myVar, value=2).grid(row=4, column=0, padx=(30,0),pady=(10,0))

		#Widgets placed on frame2
		self.output_window = tk.Text(self.frame2, font=('Verdana',7), height=12, width=35)
		self.output_window.grid(row=0, column=0, pady=(10,0))

		#Widgets placed on frame3
		self.output_button = ttk.Button(self.frame3, text='Output Data',padding=10,width=25, command=self.get_weather_data).grid(row=0,column=0, sticky='w')
		self.reset_button = ttk.Button(self.frame3, text='RESET', width=37,padding=10, command=self.reset_interface).grid(row=0, column=1, padx=(30,0))

	#Methods
	#Clear the screen
	def reset_interface(self):
		self.entry_widget.delete(0,tk.END)
		self.output_window.delete('1.0','end')


	def get_weather_data(self):
		self.entry_widget_data = self.entry_widget.get() + "\n"
		self.output_window.insert(tk.INSERT,self.entry_widget_data)
		self.entry_widget.delete(0,tk.END)


if __name__ == '__main__':
	app = MyApp()
	app.mainloop()


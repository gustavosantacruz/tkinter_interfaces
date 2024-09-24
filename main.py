import tkinter as tk

ventana = tk.Tk() # la segunda  t va en mayuscula

ventana.title("mi primer ventana")
ventana.geometry("600x400+0+0")
ventana.minsize(400, 200)
ventana.maxsize(800, 600)
ventana.iconbitmap("perrito.ico")
ventana.configure(bg= "aquamarine2")
ventana.resizable(False,True)
ventana.attributes("-alpha", 0.9)

ventana.mainloop()
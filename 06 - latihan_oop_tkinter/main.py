# 06 - Latihan OOP Tkinker
import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text="label1")
label2 = tkinter.Label(main_window, text="label2")
button1 = tkinter.Button(main_window, text="Tombo1")
button2 = tkinter.Button(main_window, text="Tombo2")

# methods positioning
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# methods utk menampilkan GUI
main_window.mainloop()

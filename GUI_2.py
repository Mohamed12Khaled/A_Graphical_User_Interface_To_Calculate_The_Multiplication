from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("600x600")
root.title("multiply")

label1 = Label(root, text="enter the first number", relief="groove", borderwidth="3")
label1.pack(padx=10, pady=30)

label2 = Label(root, text="enter the first number", relief="groove", borderwidth="3")
label2.pack(padx=10, pady=30)

label3 = Label(root, text="the result")
label3.pack(padx=10, pady=30)


ent1 = Entry(root)
ent1.place(x=400, y=30)
ent2 = Entry(root)
ent2.place(x=400, y=115)
def calc():
    num1 = float(ent1.get())
    num2 = float(ent2.get())
    result = num1 * num2
    showinfo(title="the result of multiplication", message=f"result = {result}")

button1 = Button(root, text="calculate", command=calc)
button1.place(x=400, y=200)
exit_btn = Button(root, text="Exit", command=lambda: root.destroy(), relief="sunken")
exit_btn.place(x=350, y=270)


root.mainloop()
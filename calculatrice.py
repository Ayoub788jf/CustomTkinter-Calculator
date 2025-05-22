from customtkinter import *

root = CTk()
root.geometry('355x410')
root._set_appearance_mode('dark')
root.resizable(False, False)

def calcul(value):
    current_text = entry.get("1.0", "end-1c")  
    entry.delete("1.0", "end")  
    entry.insert("end", current_text + value) 
def solution():
    try:
        expression = entry.get("1.0", "end-1c")  
        result = eval(expression)  
        entry.delete("1.0", "end")  
        entry.insert("end", result) 
    except Exception:
        entry.delete("1.0", "end")

def clear():
    entry.delete("1.0", "end")

#button keysboard 

def handle_key_press(event):
    key = event.char  # Get the character of the key pressed
    if key.isdigit() or key in "+-*/":
        calcul(key)  # Handle digit or operator
    elif key == '\r':  # Enter key
        solution()  # Evaluate the expression
    elif key == 'c' or key == 'C':  # Clear command
        entry.delete("1.0", "end")

root.bind('<Key>', handle_key_press)

# Entry
entry = CTkTextbox(root,
                  wrap="word",
                  width=250,
                  height=50,
                  border_color="white",
                  border_width=2, 
                  font=("Roboto", 20, "bold"),
                  text_color="white",
                  bg_color="#242424",
                  fg_color="#242424")
entry.place(x=10, y=10)

entry.insert("1.0", " ")

clear = CTkButton(root, 
                     text='C',
                     font=("Roboto", 30, "bold"), 
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=50,
                     bg_color="#242424",
                     fg_color="orange",
                     corner_radius=10,
                     command=clear)
clear.place(x=265, y=10)

# Buttonss
button1 = CTkButton(root, 
                     text='1',
                     font=("Roboto", 30, "bold"), 
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("1"))
button1.place(x=10, y=70)



button2 = CTkButton(root, 
                     text='2', 
                     width=80,
                     font=("Roboto", 30, "bold"), 
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("2"))
button2.place(x=95, y=70)

button3 = CTkButton(root, 
                     text='3',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("3"))
button3.place(x=180, y=70)

button4 = CTkButton(root, 
                     text='4',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     height=80,
                     border_color="white",
                     border_width=2, 
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("4"))
button4.place(x=10, y=155)

button5 = CTkButton(root, 
                     text='5',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("5"))
button5.place(x=95, y=155)

button6 = CTkButton(root, 
                     text='6',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("6"))
button6.place(x=180, y=155)

button7 = CTkButton(root, 
                     text='7',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     height=80,
                     border_color="white",
                     border_width=2, 
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("9"))
button7.place(x=10, y=240)

button8 = CTkButton(root, 
                     text='8',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("8"))
button8.place(x=95, y=240)

button9 = CTkButton(root, 
                     text='9',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     height=80,
                     border_color="white",
                     border_width=2, 
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("7"))
button9.place(x=180, y=240)


button = CTkButton(root, 
                     text='.',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     height=80,
                     border_color="white",
                     border_width=2, 
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("."))
button.place(x=10, y=325)

button0 = CTkButton(root, 
                     text='0',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("0"))
button0.place(x=95, y=325)

buttonequal = CTkButton(root, 
                     text='=',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="orange",
                     corner_radius=10,
                     command=solution)
buttonequal.place(x=180, y=325)

buttonplus = CTkButton(root, 
                     text='+',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("+"))
buttonplus.place(x=265, y=70)

buttonmines = CTkButton(root, 
                     text='-',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("-"))
buttonmines.place(x=265, y=155)

buttontimes = CTkButton(root, 
                     text='x',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("*"))
buttontimes.place(x=265, y=240)

buttondiv = CTkButton(root, 
                     text='/',
                     font=("Roboto", 30, "bold"),  
                     width=80,
                     border_color="white",
                     border_width=2, 
                     height=80,
                     bg_color="#242424",
                     fg_color="#343434",
                     corner_radius=10,
                     command=lambda: calcul("/"))
buttondiv.place(x=265, y=325)


root.mainloop()
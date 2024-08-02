import tkinter as tk



def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(values):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, values)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=220, y=70)
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=240, y=70)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=260, y=70)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=280, y=70)
number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=30, y=75)
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=30, y=130)
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=30, y=185)
number1 = tk.Label(window, text="Ввведите первое число:")
number1.place(x=30, y=50)
number2 = tk.Label(window, text="Ввведите второе число:")
number2.place(x=30, y=100)
answer = tk.Label(window, text="Ответ:")
answer.place(x=30, y=155)
actions = tk.Label(window, text="Действия:")
actions.place(x=240, y=40)
window.mainloop()

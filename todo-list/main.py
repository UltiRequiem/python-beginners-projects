from tkinter import *

from tkinter import messagebox

tasks_list = []

counter = 1


def inputError():
    if enter_task_field.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1


def clear_taskNumberField():
    task_number_field.delete(0.0, END)


def clear_taskField():
    enter_task_field.delete(0, END)


def insertTask():

    global counter

    value = inputError()

    if value == 0:
        return

    content = enter_task_field.get() + "\n"

    tasks_list.append(content)

    text_area.insert("end -1 chars", "[ " + str(counter) + " ] " + content)

    counter += 1

    clear_taskField()

def sortTasks():
    global tasks_list
    tasks_list = sorted(tasks_list)
    text_area.delete(1.0, END)
    for i in range(len(tasks_list)):
        text_area.insert("end -1 chars", "[ " + str(i + 1) + " ] " + tasks_list[i])


def delete():

    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return

    number = task_number_field.get(1.0, END)

    if number == "\n":
        messagebox.showerror("input error")
        return

    else:
        task_no = int(number)

    clear_taskNumberField()

    tasks_list.pop(task_no - 1)

    counter -= 1

    text_area.delete(1.0, END)

    for i in range(len(tasks_list)):
        text_area.insert("end -1 chars", "[ " + str(i + 1) + " ] " + tasks_list[i])


if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="light green")

    gui.title("ToDo App")

    gui.geometry("250x300")

    enter_task = Label(gui, text="Enter Your Task", bg="light green")

    enter_task_field = Entry(gui)

    submit = Button(gui, text="Submit", fg="Black", bg="Red", command=insertTask)

    text_area = Text(gui, height=5, width=25, font="lucida 13")

    task_number = Label(gui, text="Delete Task Number", bg="blue")

    task_number_field = Text(gui, height=1, width=2, font="lucida 13")

    delete = Button(gui, text="Delete", fg="Black", bg="Red", command=delete)

    exite = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    sort_button = Button(gui, text="Sort Tasks", fg="Black", bg="Green", command=sortTasks)
    sort_button.grid(row=8, column=2, pady=5)

    enter_task.grid(row=0, column=2)

    enter_task_field.grid(row=1, column=2, ipadx=50)

    submit.grid(row=2, column=2)

    text_area.grid(row=3, column=2, padx=10, sticky=W)

    task_number.grid(row=4, column=2, pady=5)

    task_number_field.grid(row=5, column=2)

    delete.grid(row=6, column=2, pady=5)

    exite.grid(row=7, column=2)

    gui.mainloop()

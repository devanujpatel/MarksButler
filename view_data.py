import tkinter as tk
from database_interface import *

db = Database()
drop_values = []


def show_data_in_table():
    data = db.get_marks_data(drop_values[1].get(), drop_values[0].get())
    print(data)

    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = tk.Entry(root, width=20, fg='blue',
                                      font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(tk.END, lst[i][j])

    # take the data
    lst = data

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    grid_container = tk.Frame(container_)
    grid_container.pack()
    t = Table(grid_container)


def control_view_data(container):
    global container_
    container_ = container
    drop_values.append(tk.StringVar())
    drop_values[0].set("Class")

    # Create Dropdown menu
    class_drop = tk.OptionMenu(container, drop_values[0], *db.existing_values("class_name", "classes"))
    class_drop.config(height=2, width=60, font=("Courier", 15))
    class_drop.pack()

    drop_values.append(tk.StringVar())
    drop_values[1].set("Exam")
    # Create Dropdown menu
    exam_drop = tk.OptionMenu(container, drop_values[1], *db.existing_values("exam_name", "exams"))
    exam_drop.config(height=2, width=60, font=("Courier", 15))
    exam_drop.pack()

    tk.Button(container, text="Submit", command=lambda: show_data_in_table()).pack()

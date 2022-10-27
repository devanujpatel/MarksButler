import tkinter as tk
from database_interface import *

fields_to_show = {
    'classes': ['Class Name'],
    'students': ["First Name", "Last Name", "Class"],
    'exams': ['Exam Name'],
    'subjects': ["Subject Name"],
    'marks': ["Student", "Exam", "Subject", "Marks"]
}

drop_required = {"Class": ["class_name", "classes"], "Student": ["first_name", "students"],
                 "Exam": ["exam_name", "exams"], "Subject": ["subject_name", "subjects"]}

db = Database()


def get_data_from_drop_and_insert(fields_dict, value):
    values = []
    for val in fields_dict:
        if val not in drop_required:
            values.append(fields_dict[val].get())
        else:

    if value == "classes":
        db.add_data_classes(values)

    elif value == "students":
        db.add_data_students(values)

    elif value == "exams":
        db.add_data_exams(values)

    elif value == "marks":
        db.add_data_marks(values)

    elif value == "subjects":
        db.add_data_subjects(values)

    db.db.close()


def dropdown_selected(value):
    drop.forget()
    fields_dict = {}

    # TODO: Add label

    for field in fields_to_show[value]:
        if field not in drop_required:
            text = tk.StringVar()
            text.set(field)
            fields_dict[field] = tk.Entry(add_container, textvariable=text)
            fields_dict[field].pack()
        else:
            print(fields_dict)
            print(drop_required)
            print(field)
            text = tk.StringVar()
            text.set(field)
            val_drop = tk.OptionMenu(add_container, text,
                                     *db.existing_values(drop_required[field][0], drop_required[field][1]),
                                     command=dropdown_selected)
            val_drop.config(height=1, width=5)
            val_drop.pack()

    tk.Button(add_container, text="Enter", font=("Courier", 16),
              command=lambda: get_data_from_drop_and_insert(fields_dict, value)).pack()


def control_add_data_container(container):
    clicked = tk.StringVar()
    global add_container
    add_container = container
    # initial menu text
    clicked.set("What do you want to insert?")
    global drop
    # Create Dropdown menu
    drop = tk.OptionMenu(container, clicked, *fields_to_show.keys(), command=dropdown_selected)
    drop.config(height=2, width=60, font=("Courier", 15))
    drop.pack()

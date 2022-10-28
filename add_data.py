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

drop_values = {}


def get_data_from_drop_and_insert(fields_dict, value):
    values = []
    print(fields_dict)
    for val in fields_dict:
        if val not in drop_required:
            print(val, "not in")
            values.append(fields_dict[val].get())
        else:
            print(val, "in")
            selected = fields_dict[val].get()
            print(selected)
            if val == "Class":
                values.append(db.get_fk_mapping_class(str(selected)))
            elif val == "Student":
                values.append(db.get_fk_mapping_student(str(selected)))
            elif val == "Exam":
                values.append(db.get_fk_mapping_exam(str(selected)))
            elif val == "Subject":
                values.append(db.get_fk_mapping_subject(str(selected)))
    print(values)
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

    db.db.commit()
    add_container.forget()
    _start_frame.pack()


def dropdown_selected(value):
    drop.forget()
    fields_dict = {}

    # TODO: Add label
    for field in fields_to_show[value]:
        if field not in drop_required:
            edit_text = tk.StringVar()
            edit_text.set(field)
            fields_dict[field] = tk.Entry(add_container, textvariable=edit_text)
            fields_dict[field].pack()
        else:
            fields_dict[field] = tk.StringVar()
            fields_dict[field].set(field)
            menu = tk.OptionMenu(add_container, fields_dict[field], "",
                                 *db.existing_values(drop_required[field][0],
                                                     drop_required[field][1])
                                 )

            menu.config(height=1, width=5)
            menu.pack()

    tk.Button(add_container, text="Enter", font=("Courier", 16),
              command=lambda: get_data_from_drop_and_insert(fields_dict, value)).pack()


def control_add_data_container(container, start_frame):
    clicked = tk.StringVar()
    global add_container, _start_frame
    add_container = container
    _start_frame = start_frame
    # initial menu text
    clicked.set("What do you want to insert?")
    global drop
    # Create Dropdown menu
    drop = tk.OptionMenu(container, clicked, *fields_to_show.keys(), command=dropdown_selected)
    drop.config(height=2, width=60, font=("Courier", 15))
    drop.pack()

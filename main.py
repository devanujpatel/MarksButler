import tkinter as tk
import add_data

container = tk.Tk()

width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen
container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

start_frame = tk.Frame(container, width=width, height=height)
start_frame.pack()

tk.Label(start_frame, text="Welcome to Marks Butler", font=("Courier", 19)).place(relx=.5, rely=.3, anchor=tk.CENTER)


def add_button_clicked():
    start_frame.pack_forget()
    add_data_container = tk.Frame(container, height=height, width=width)
    add_data_container.pack()
    add_data.control_add_data_container(add_data_container)



def view_button_clicked():
    start_frame.pack_forget()
    view_data_container = tk.Frame(container, height=height, width=width)
    view_data_container.pack()


tk.Button(start_frame, text="Add data", command=lambda: add_button_clicked(), font=("Courier", 16)).place(relx=.4,
                                                                                                          rely=.45,
                                                                                                          anchor=tk.CENTER)

tk.Button(start_frame, text="View data", command=lambda: view_button_clicked(), font=("Courier", 16)).place(relx=.6,
                                                                                                            rely=.45,
                                                                                                            anchor=tk.CENTER)

container.mainloop()

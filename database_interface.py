import mysql.connector

fields_to_insert = {
    'classes': ['class_name'],
    'students': ["first_name", "last_name", "class_fk"],
    'exams': ['exam_name'],
    'subjects': ["subject_name"],
    'marks': ["student_fk", "exam_fk", "subject_fk"]
}


class Database():
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dev@mysql"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("USE marks_butler")

    def add_data_classes(self, values):
        self.cursor.execute("INSERT INTO classes (class_name) VALUES (%s)", values)
        self.db.commit()

    def add_data_students(self, values):
        self.cursor.execute("INSERT INTO students (first_name, last_name, class_fk) VALUES (%s, %s, %s)", values)
        self.db.commit()

    def add_data_subjects(self, values):
        self.cursor.execute("INSERT INTO subjects (subject_name) VALUES (%s)", values)
        self.db.commit()

    def add_data_exams(self, values):
        self.cursor.execute("INSERT INTO exams (exam_name) VALUES (%s)", values)
        self.db.commit()

    def add_data_marks(self, values):
        self.cursor.execute("INSERT INTO marks (student_fk, exam_fk, subject_fk, marks) VALUES (%s, %s, %s, %s)", values)
        self.db.commit()

    def existing_values(self, field, table):
        self.cursor.execute(f"SELECT {field} FROM {table};")
        return_list = []
        for val_tup in self.cursor.fetchall():
            return_list.append(val_tup[0])
        return return_list


    def get_fk_mapping_class(self, where_condition_value):
        print(type(where_condition_value), where_condition_value)
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT class_pk FROM classes WHERE class_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT class_pk FROM classes WHERE class_name = %s", (where_condition_value,))
        return self.cursor.fetchall()[0][0]

    def get_fk_mapping_subject(self, where_condition_value):
        print(type(where_condition_value), where_condition_value)
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT subject_pk FROM subjects WHERE subject_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT subject_pk FROM subjects WHERE subject_name = %s", (where_condition_value,))
        return self.cursor.fetchall()[0][0]

    def get_fk_mapping_exam(self, where_condition_value):
        print(type(where_condition_value), where_condition_value)
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT exam_pk FROM exams WHERE exam_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT exam_pk FROM exams WHERE exam_name = %s", (where_condition_value,))
        return self.cursor.fetchall()[0][0]

    def get_fk_mapping_student(self, where_condition_value):
        print(type(where_condition_value), where_condition_value)
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT student_pk FROM students WHERE first_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT student_pk FROM students WHERE first_name = %s", (where_condition_value,))
        return self.cursor.fetchall()[0][0]



"""query = 'INSERT INTO %s('
        for i in fields_to_insert[table]:
            query += "%s,"
        query += "\b) VALUES ("

        for i in values:
            query += "'%s',"
        query += "\b);"

        placeholders = [table] + fields_to_insert[table] + values
        print(placeholders)

        print(query)"""

"""
        query = 'INSERT INTO ' + table + ' ('
        for val in fields_to_insert[table]:
            query += str(val) + ','
        query += '\b)'

        query += ' VALUES ('
        for val in values:
            query += '\'' + str(val) + '\','
        query += '\b)'
        print(query)
        self.cursor.execute(query)
        print(query)
        self.db.commit()
        """

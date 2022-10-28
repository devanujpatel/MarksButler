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
        self.cursor.execute("INSERT INTO marks (student_fk, exam_fk, subject_fk, marks) VALUES (%s, %s, %s, %s)",
                            values)
        self.db.commit()

    def existing_values(self, field, table):
        self.cursor.execute(f"SELECT {field} FROM {table};")
        return_list = []
        for val_tup in self.cursor.fetchall():
            return_list.append(val_tup[0])
        return return_list

    def get_fk_mapping_class(self, where_condition_value):
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT class_pk FROM classes WHERE class_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT class_pk FROM classes WHERE class_name = '" + where_condition_value + "'")
        return self.cursor.fetchall()[0][0]

    def get_fk_mapping_subject(self, where_condition_value):
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT subject_pk FROM subjects WHERE subject_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT subject_pk FROM subjects WHERE subject_name = %s", (where_condition_value,))
        return self.cursor.fetchall()[0][0]

    def get_fk_mapping_exam(self, where_condition_value):
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT exam_pk FROM exams WHERE exam_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT exam_pk FROM exams WHERE exam_name = '" + where_condition_value + "'")
        return self.cursor.fetchall()[0][0]

    def get_fk_mapping_student(self, where_condition_value):
        if where_condition_value[0] == "(":
            self.cursor.execute("SELECT student_pk FROM students WHERE first_name = %s", eval(where_condition_value))
        else:
            self.cursor.execute("SELECT student_pk FROM students WHERE first_name = %s", (where_condition_value,))
        return self.cursor.fetchall()[0][0]

    def get_marks_data(self, s_exam, s_class):
        self.cursor.execute("""select s.first_name, s.last_name, marks, su.subject_name from marks	
	                            join students as s on s.student_pk = marks.student_fk
                                join exams as e on marks.exam_fk = e.exam_pk
                                join subjects as su on marks.subject_fk = su.subject_pk
                                join classes as c on c.class_pk = s.class_fk
                                where c.class_pk = CAST(%s as UNSIGNED) and e.exam_pk = CAST(%s as UNSIGNED);""",
                            (self.get_fk_mapping_class(s_class), self.get_fk_mapping_exam(s_exam)))
        return self.cursor.fetchall()

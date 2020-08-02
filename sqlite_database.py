import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


# c.execute('''CREATE TABLE students (
#             name text,
#             year text,
#             branch text,
#             rollno text,
#             mobile int)''')


def add_student(student):
    with conn:
        c.execute('INSERT INTO students VALUES (:name, :year, :branch, :rollno, :mobile)',
                  {'name': student.name, 'year': student.year, 'branch': student.branch, 'rollno': student.rollno,
                   'mobile': student.mobile})


def delete_student(rollno):
    with conn:
        c.execute("DELETE from students WHERE rollno = :rollno",
                  {'rollno': rollno})


def get_student(rollno):
    c.execute("SELECT * FROM students WHERE rollno=:rollno", {'rollno': rollno})
    return c.fetchone()


conn.commit()

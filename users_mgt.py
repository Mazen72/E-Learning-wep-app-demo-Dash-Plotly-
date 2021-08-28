from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine
import pandas as pd

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class courses(db.Model):
    Course_Name = db.Column(db.String(50), primary_key=True)
    Course_Rating = db.Column(db.Float, unique=True)
    Course_Hours =db.Column(db.Float, unique=True)
    Students =db.Column(db.Integer, unique=True)

class Python_data_analysis(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    Enrolled=db.Column(db.String(8), unique=True)
    Course_progress = db.Column(db.String(6), unique=True)
    Course_Rating = db.Column(db.Float, unique=True)
    quiz1_state =db.Column(db.String(10), unique=True)
    quiz2_state = db.Column(db.String(10), unique=True)
    quiz3_state = db.Column(db.String(10), unique=True)
    quiz4_state = db.Column(db.String(10), unique=True)
    quiz5_state = db.Column(db.String(10), unique=True)
    quiz6_state = db.Column(db.String(10), unique=True)
    final_exam_degree=db.Column(db.Float, unique=True)


User_tbl = Table('user', User.metadata)
courses_tbl=Table('courses',courses.metadata)
Python_data_tbl=Table('python_data_analysis',Python_data_analysis.metadata)

def create_user_table():
    User.metadata.create_all(engine)

def create_courses_table():
    courses.metadata.create_all(engine)

def create_course1_table():
    Python_data_analysis.metadata.create_all(engine)





def add_user(id,username, password):
    hashed_password = generate_password_hash(password, method='sha256')
    df = pd.read_sql_table('user', con='sqlite:///users.db')
    new_row = pd.Series(data={'id':'{}'.format(id), 'username':'{}'.format(username), 'password':'{}'.format(hashed_password),
                              },name='{}'.format(username))
    df = df.append(new_row, ignore_index=False)
    df.to_sql("user", con='sqlite:///users.db', if_exists='replace', index=False)



def del_user(user_num):
    df = pd.read_sql_table('user', con='sqlite:///users.db')
    df = df.drop(user_num-1)
    df.to_sql("user", con='sqlite:///users.db', if_exists='replace', index=False)



def show_users():
    select_st = select([User_tbl.c.username, User_tbl.c.email])

    conn = engine.connect()
    rs = conn.execute(select_st)

    for row in rs:
        print(row)

    conn.close()


def add_course(name, rating, hours,students):
    df = pd.read_sql_table('courses', con='sqlite:///users.db')
    new_row = pd.Series(data={'Course_Name':'{}'.format(name), 'Course_Rating':'{}'.format(rating), 'Course_Hours':'{}'.format(hours),
                              'Students':'{}'.format(students)},name='{}'.format(name))
    df = df.append(new_row, ignore_index=False)
    df.to_sql("courses", con='sqlite:///users.db', if_exists='replace', index=False)

def del_course(index):
    df = pd.read_sql_table('courses', con='sqlite:///users.db')
    df = df.drop(index)
    df.to_sql("courses", con='sqlite:///users.db', if_exists='replace', index=False)

def add_data_student(student_id,Enrolled,Course_progress,Course_Rating,quiz1_state,quiz2_state,
                     quiz3_state,quiz4_state,quiz5_state,quiz6_state,final_exam_degree):

    df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
    new_row = pd.Series(data={'student_id':'{}'.format(student_id), 'Enrolled':'{}'.format(Enrolled), 'Course_progress':'{}'.format(Course_progress),
                              'Course_Rating':'{}'.format(Course_Rating),'quiz1_state':'{}'.format(quiz1_state), 'quiz2_state':'{}'.format(quiz2_state),
                              'quiz3_state':'{}'.format(quiz3_state),'quiz4_state':'{}'.format(quiz4_state),'quiz5_state':'{}'.format(quiz5_state),
                              'quiz6_state':'{}'.format(quiz6_state),'final_exam_degree':'{}'.format(final_exam_degree)
                              },name='{}'.format(student_id))
    df = df.append(new_row, ignore_index=False)
    df.to_sql("python_data_analysis", con='sqlite:///users.db', if_exists='replace', index=False)

def del_data_student(index):
    df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
    df = df.drop(index)
    df.to_sql("python_data_analysis", con='sqlite:///users.db', if_exists='replace', index=False)


def edit_sql_cell(table_name,col_name,index,value):
    df = pd.read_sql_table(table_name, con='sqlite:///users.db')

    df.at[index, col_name] = value
    df.to_sql(table_name, con='sqlite:///users.db', if_exists='replace', index=False)

def read_sql_cell(table_name,col_name,index):
    df = pd.read_sql_table(table_name, con='sqlite:///users.db')
    df1=df.at[index, col_name]
    return df1


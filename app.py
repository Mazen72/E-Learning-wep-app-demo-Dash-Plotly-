# index page
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output,State
import users_mgt as um
from server import app, server
from flask_login import logout_user, current_user
from views import success, login, login_fd, logout
import data_material
import admin
import pandas as pd
import sqlalchemy
from config import engine
import base64
import dash_table
import data_material
import datetime


#new_row = pd.Series(data={'Course_Name':'Python Data Analysis', 'Course_Rating':'', 'Course_Hours':'20','Students':'0'},
#name='{}'.format(len(df.index+1)))
#df = df.append(new_row, ignore_index=False)
#df=df.drop(columns="python_data_analysis")

#df=pd.read_sql_table('user',con='sqlite:///users.db')
#df=df.drop(3)
#df.insert(loc=4,column='Students',value='',allow_duplicates=False)
#df.to_sql("user", con='sqlite:///users.db', if_exists='replace', index=False)
#um.add_course('Python Data Analysis','',20,0)
#um.add_course('Machine Learning','',27,0)
#um.edit_sql_cell('python_data_analysis','student_id',1,1)


#df.insert(loc=0,column='student_id',value='1',allow_duplicates=False)
#df.set_index('student_id',inplace=True)
#df.to_sql("python_data_analysis", con='sqlite:///users.db', if_exists='replace', index=True,index_label='student_id')



#df.to_sql("courses", con='sqlite:///users.db', if_exists='replace', index=False)


#index=df.index[df['id'] == '2'].tolist()
#print( um.read_sql_cell('user','username', index[0]  ))


#print(len(df.index))
#print(df)
#https://kanoki.org/2019/04/12/pandas-how-to-get-a-cell-value-and-update-it/
#https://www.youtube.com/watch?v=skGwKh1dAdk
encoded = base64.b64encode(open('logo.png', 'rb').read())

logo_img=dbc.Row([dbc.Col([
    html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='logo_img', height=80)
    ] ,
        xs=dict(size=12,offset=0), sm=dict(size=12,offset=0),
        md=dict(size=12,offset=0), lg=dict(size=12,offset=0), xl=dict(size=12,offset=0))
    ])

encoded2 = base64.b64encode(open('bg4.jpg', 'rb').read())

bg_img=html.Img(src='data:image/png;base64,{}'.format(encoded2.decode()), id='bg_img', height='800rem',width='100%')

header_text=html.Div('Learning Made Easy',style=dict(color='black',
                     fontWeight='bold',fontSize='1.4rem',marginTop='1rem',marginLeft='3rem'))

please_login_text=html.Div('Please login to continue..',style=dict(color='black',
                     fontWeight='bold',fontSize='1.4rem',marginTop='1rem',marginLeft='3rem'))

logout_msg=html.Div(id='logout')

search_input=dbc.Input(id="input", placeholder="Search here..", type="text",bs_size="lg",
                       style=dict(marginTop='1rem',fontSize='1.1rem'))
search_button= dbc.Button("Search", color="primary", size='lg', n_clicks=0,
                          style=dict(marginTop='1rem',fontSize='1.1rem'))

logout_button= dbc.Button("Logout", color="primary", size='md', n_clicks=0,id='logout_btn',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem',marginLeft='2.5rem'))




db_logo_img=dbc.Col([ logo_img] ,
        xs=dict(size=2,offset=0), sm=dict(size=2,offset=0),
        md=dict(size=2,offset=0), lg=dict(size=2,offset=0), xl=dict(size=1,offset=0))

db_header_text=  dbc.Col([ header_text] ,
        xs=dict(size=8,offset=0), sm=dict(size=8,offset=0),
        md=dict(size=2,offset=0), lg=dict(size=3,offset=0), xl=dict(size=3,offset=0))



db_search_input=dbc.Col([search_input],
        xs=dict(size=5, offset=2), sm=dict(size=5, offset=2),
        md=dict(size=2, offset=2), lg=dict(size=2, offset=2), xl=dict(size=2, offset=1))

db_search_button=dbc.Col([search_button],
        xs=dict(size=2, offset=0), sm=dict(size=2, offset=0),
        md=dict(size=2, offset=0), lg=dict(size=2, offset=0), xl=dict(size=2, offset=0))

db_please_login_text= dbc.Col([ please_login_text] ,
        xs=dict(size=8,offset=0), sm=dict(size=8,offset=0),
        md=dict(size=2,offset=0), lg=dict(size=3,offset=0), xl=dict(size=3,offset=0))

data_progress=dbc.Progress(children=[], max=100, striped=True, color="primary",id='progress',
                           style=dict(height='20px',backgroundColor='white',fontWeight='bold'),
                         bar_style=dict(color='black'))

data_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1567221927/image_3_ayi4rs.png", top=True),
                                 dbc.CardBody(
                                     [
                                         html.H5("Python Data Analysis", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "using pandas python package to analyze data and make reports",
                                             style=dict(color='black')
                                         ),
                    dbc.Nav([ dbc.NavItem(dbc.NavLink("Details", active=True, href="/data", id='data_details')) ],pills=True)

                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

data_course_card_progress=dbc.Col([html.Br(),dbc.CardImg(src="https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1567221927/image_3_ayi4rs.png", top=True,
                                                         style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Python Data Analysis", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "using pandas python package to analyze data and make reports",
                                             style=dict(color='black')
                                         ),
                    dbc.Nav([ dbc.NavItem(dbc.NavLink("Details", active=True, href="/data", id='data_details')) ],pills=True),html.Br(),data_progress

                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

ml_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://iraqcoders.com/wp-content/uploads/2019/02/emerging-tech_ai_machine-learning-100748222-large.jpg", top=True,
                                              style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Machine Learning", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will understand how to implement basic machine learning ",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

sql_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://media.onlinecoursebay.com/2019/08/27030502/2488822_25d1-750x405.jpg", top=True,
                                               style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("SQL basics", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will understand how to deal with different types of databases",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

image_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://images-na.ssl-images-amazon.com/images/I/61gBVmFtNpL.jpg", top=True,
                                               style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Image Processing", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will understand how to use opencv for image processing",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )



iot_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://cdn.mindmajix.com/courses/iot-training.png", top=True,
                                               style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Internet Of Things", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will understand how IoT devices and systems works",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )


embedded_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://prod-discovery.edx-cdn.org/media/course/image/785cf551-7f66-4350-b736-64a93427b4db-3dcdedbdf99d.small.jpg", top=True,
                                               style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Embedded Systems", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will learn embedded software techniques using tivac board",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

arch_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://moodle.aaup.edu/pluginfile.php/288902/course/overviewfiles/Computer-Architecture.jpg", top=True,
                                               style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Computer Architecture", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will learn how memory and cpu works in details",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

web_course_card=dbc.Col([html.Br(),dbc.CardImg(src="https://www.onlinecoursereport.com/wp-content/uploads/2020/07/shutterstock_394793860-1024x784.jpg", top=True,
                                               style=dict(height='20vh')),
                                 dbc.CardBody(
                                     [
                                         html.H5("Web development", className="card-title",style=dict(color='black')),
                                         html.P(
                                             "you will learn to develop website using html,css and javascript",
                                             style=dict(color='black')
                                         ),
                                         dbc.Button("Details", color="primary"),
                                     ] ,style=dict(backgroundColor='#f0ad4e')
                                 )

]  ,xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )

courses_layout=dbc.Row([ data_course_card, ml_course_card,sql_course_card,image_course_card,
                         iot_course_card,embedded_course_card ,arch_course_card,web_course_card



] , no_gutters=False)

rate_button= dbc.Button("Rate Course", color="primary", size='lg', n_clicks=0,id='rate_button',
                        style=dict(marginTop='1rem',fontSize='1.1rem'))

rate_input= html.Div([dbc.Input(id="rate_input", placeholder="0-5 Stars", type="number",bs_size="lg",
                                min=1, max=5,
                                style=dict(fontSize='1.1rem'))   ]  )

submit_rating_button= dbc.Button("Submit", color="primary", size='lg', n_clicks=0, id='submit_rating_button',
                        style=dict(marginTop='1rem',fontSize='1.1rem'))

rating_input=dbc.Collapse([ rate_input, submit_rating_button
                          ],id="collapse",is_open=False,
                            style=dict(border='0.5vh solid black')
                         )

rate_div=html.Div([rate_button,html.Br(),html.Br(),rating_input


] )

sidebar = html.Div(
    [
        html.H2("Course Content", className="display-4", style=dict(color='black',fontWeight='bold')),
        html.Hr(style=dict(color='black')),
        html.P(
            "Welcome to the course , you can start your lessons bellow ..",className="lead", style=dict(color='black')
        ),
        dbc.Nav(
            [
                dbc.NavLink("Session1", href="/data/video1", active="exact",style=dict(fontWeight='bold')),
                dbc.NavLink("Session2", href="/data/video2", active="exact",style=dict(fontWeight='bold')),
                dbc.NavLink("Session3", href="/data/video3", active="exact",style=dict(fontWeight='bold')),
                dbc.NavLink("Session4", href="/data/video4", active="exact",style=dict(fontWeight='bold')),
                dbc.NavLink("Session5", href="/data/video5", active="exact",style=dict(fontWeight='bold')),
                dbc.NavLink("Session6", href="/data/video6", active="exact",style=dict(fontWeight='bold'))
            ],
            vertical=True,
            pills=True,
        ),rate_div
    ],
style=dict(backgroundColor='#f0ad4e',height='100%')
)

star_img = 'star.jpg'
encoded = base64.b64encode(open(star_img, 'rb').read())
star_image = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='img1', height=40, width=40)
star_image_div=html.Div(star_image, style=dict(display='inline-block'))

data_course_header=html.Div([html.Br(),html.H1('Python Data analysis and visualization course',style=dict(fontSize=36)),
                            html.Div(' Rating : 4.5/5',style=dict(fontSize=22,display='inline-block'),id='stars'),
                            star_image_div,html.Div ('Students : 23',style=dict(fontSize=22),id='students'),
                            html.Div('Total Hours : 20 hour',style=dict(fontSize=22)),html.Br(),
                            dbc.Nav([dbc.NavItem(dbc.NavLink("Enroll Course", active=True, href="/data/video1", id='enroll_data'))],
                            pills=True),html.Br()

] , style=dict(color='white',border='4px #f0ad4e solid'))



data_course_Req= html.Div([html.H1('Requirements',style=dict(fontSize=32)),
                           html.Div(style=dict(border='3px #f0ad4e solid',width='100%',height='5px')),html.Br(),
                           html.Div(' 1-Basic math skills',style=dict(fontSize=22)),
                           html.Div ('2-Basic to Intermediate Python Skills.',style=dict(fontSize=22)),
                           html.Div  ('3-Have a computer (either Mac, Windows, or Linux.',style=dict(fontSize=22))

] , style=dict(color='white'))

data_course_desc=html.Div([html.H1('Description',style=dict(fontSize=32)),
                           html.Div(style=dict(border='3px #f0ad4e solid',width='100%',height='5px')),
                           html.Div('Our goal is to provide you with complete preparation. And this course will turn you into a job-ready data analyst.'
                                    ' To take you there, we will cover the following fundamental topics extensively.',
                                    style=dict(fontSize=22,color='white')),
                           html.Div('1- Theory about the field of data analytics',style=dict(fontSize=22,color='white')),
                           html.Div('2- Basic and Advanced python',style=dict(fontSize=22,color='white')),
                           html.Div('3- Pandas and Numpy libraries'),
                           html.Div('4- Data collection ,Cleaning and Visualization',style=dict(fontSize=22,color='white'))
                           ] )


data_video1_youtube=html.Div(children=[
            html.Iframe(width="100%%", height="474", src="https://www.youtube.com/embed/nLw1RNvfElg"
                       , title="YouTube video player"

                        ),
                  ])
data_quiz1_header=html.Div('A graph used in statistics to demonstrate how many of a certain type of variable occurs within a specific range',
                           style=dict(fontSize=22,color='black',fontWeight='black') )

data_quiz1_choices=dcc.RadioItems(
    options=[
        {'label': 'Bar plot', 'value': 'bar'},
        {'label': 'Histogram ', 'value': 'hist'},
        {'label': 'Scatter plot', 'value': 'scat'},
        {'label': 'Box plot', 'value': 'box'}
    ],
    value='',labelStyle=dict(display='block',color='black',marginLeft='1rem',fontSize=22),
    inputStyle=dict(width='1.2rem',height='1.2rem',marginRight='0.5rem') ,id='data_quiz1_choices',
    style=dict(marginLeft='4rem') , persistence=True
)

data_quiz1_submit=dbc.Button("Submit", color="primary", size='lg', n_clicks=0,id='data_quiz1_submit',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem'))

data_quiz1_answer=html.Div('',style=dict(fontSize=22,color='white',fontWeight='bold'),id='data_quiz1_answer')

data_quiz1=html.Div([ html.H1('Quiz1',style=dict(fontSize=32,color='black')),data_quiz1_header,html.Br(),
                      html.Hr(style=dict(color='black')) ,data_quiz1_choices


] ,style=dict(backgroundColor='#f0ad4e') )

data_video1_layout=dbc.Row([dbc.Col([html.Br(),sidebar

]  ,xl=dict(size=2,offset=0),lg=dict(size=2,offset=0),
    md=dict(size=5,offset=0),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_video1_youtube,html.Br(),html.Br(),
          data_quiz1,data_quiz1_submit,html.Br(),data_quiz1_answer

]  ,xl=dict(size=5,offset=2),lg=dict(size=5,offset=2),
    md=dict(size=3,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1) )




] , no_gutters=False  )


data_details_layout=dbc.Row([dbc.Col([html.Br(),data_course_header

]  ,xl=dict(size=6,offset=1),lg=dict(size=6,offset=1),
    md=dict(size=8,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_course_Req,html.Br(),data_course_desc

]  ,xl=dict(size=5,offset=1),lg=dict(size=5,offset=1),
    md=dict(size=3,offset=1),sm=dict(size=8,offset=1),xs=dict(size=8,offset=1) )


] , no_gutters=False  )




app.layout = html.Div(
    [
dbc.Row([ db_logo_img ,db_header_text

] ,no_gutters=False,style=dict(backgroundColor='#f0ad4e'),id='header' )
        ,

        html.Div(id='page-content')
            , html.Div( []   , id='page-content2'),
        dcc.Location(id='url', refresh=True) , html.Div([''],id='hidden_div1',style=dict(display='none')),
        html.Div([''],id='hidden_div2',style=dict(display='none')) ,
        dcc.Interval(id='my_interval', interval=1500)
    ]
)


#   <iframe width="843" height="474" src="https://www.youtube.com/embed/nLw1RNvfElg"
        #   title="YouTube video player" frameborder="0"
        #   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
print( df['Course_Rating'][2] )
a=3.5666667
print("%.2f" % round(a,2))


@app.callback([Output('stars','children'),Output('students','children')],
              Input('url', 'pathname'))
def update_data_details(path):
    df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
    rating_sum=0
    rating_students=0
    for rating in range(0,len(df.index) ):
        if um.read_sql_cell('python_data_analysis','Course_Rating',rating) != '':
            rating_students+=1
            rating_sum= int(rating_sum) + int(df['Course_Rating'][rating])
    stars_avg=int(rating_sum)/rating_students
    students_num=len(df.index)
    return (' Rating : {}/5'.format("%.2f" % round(stars_avg,1)),'Students : {}'.format(students_num))

@app.callback([Output('page-content', 'children'),Output('header','children'),Output('page-content2','children')],
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return (login.layout, [db_logo_img , db_header_text,db_please_login_text],[])
    elif pathname == '/login':
        return (login.layout,[ db_logo_img , db_header_text,db_please_login_text ],[] )


    elif pathname == '/success':

        if current_user.is_authenticated:

            if current_user.username=='admin':
                return ([admin.layout,html.Br(),logout_button,dcc.Location(id='url_login_success', refresh=True)],[],[])

            else:
                username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                                fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                                marginLeft='1rem'))
                db_username_text = dbc.Col([username_text,logout_button],
                                       xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                       md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
                return (success.layout, [ db_logo_img , db_header_text ,
                    db_search_input,db_search_button,db_username_text] ,[bg_img])

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )

    elif pathname == '/data_course_table':

        if current_user.is_authenticated:
            return (admin.layout2, [], [])

        else:
            return (login_fd.layout, [db_logo_img, db_header_text, db_please_login_text], [])

    elif pathname == '/Add_Course':

        if current_user.is_authenticated:
            return (admin.layout3, [], [])

        else:
            return (login_fd.layout, [db_logo_img, db_header_text, db_please_login_text], [])

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return (logout.layout, [ db_logo_img , db_header_text ,db_please_login_text],[])
        else:
            return (logout.layout,[ db_logo_img , db_header_text ] ,db_please_login_text,[] )

#"https://www.youtube.com/embed/ln8dyS2y4Nc"
    elif pathname == "/Courses":

        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                 style=dict(color='black',
                                            fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                            marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [ db_logo_img , db_header_text ,
               db_search_input,db_search_button,db_username_text]
               ,    [courses_layout]    )

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )

    elif pathname == '/data':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                 style=dict(color='black',
                                            fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                            marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_details_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )

    elif pathname == '/data/video1':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                     fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                     marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_video1_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )


    elif pathname == '/data/video2':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                     fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                     marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_material.data_video2_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )

    elif pathname == '/data/video3':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                     fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                     marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_material.data_video3_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )


    elif pathname == '/data/video4':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                     fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                     marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_material.data_video4_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )


    elif pathname == '/data/video5':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                     fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                     marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_material.data_video5_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )

    elif pathname == '/data/video6':
        if current_user.is_authenticated:
            username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                     style=dict(color='black',
                                     fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                     marginLeft='1rem'))
            db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
            return (success.layout, [db_logo_img, db_header_text,
                                     db_search_input, db_search_button,db_username_text]
                ,data_material.data_video6_layout)

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )



    elif pathname == "/My-Courses":
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            try:
                um.read_sql_cell('python_data_analysis', 'Enrolled', index[0])
                username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                 style=dict(color='black',
                                            fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                            marginLeft='1rem'))
                db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
                return (success.layout, [ db_logo_img , db_header_text ,
               db_search_input,db_search_button,db_username_text]
               ,[data_course_card_progress] )

            except:

                username_text = html.Div(['Current user: ' + current_user.username], id='user-name',
                                 style=dict(color='black',
                                            fontWeight='bold', fontSize='1.1rem', marginTop='1rem',
                                            marginLeft='1rem'))
                db_username_text = dbc.Col([username_text, logout_button],
                                   xs=dict(size=8, offset=0), sm=dict(size=8, offset=0),
                                   md=dict(size=2, offset=0), lg=dict(size=3, offset=0), xl=dict(size=3, offset=0))
                return (success.layout, [ db_logo_img , db_header_text ,
               db_search_input,db_search_button,db_username_text]
               ,[html.H1('you dont have courses yet',
                         style={'textAlign':'center'})
                ] )

        else:
            return (login_fd.layout, [ db_logo_img , db_header_text,db_please_login_text ],[] )

    # If the user tries to reach a different page, return a 404 message
    return ( html.H1("404: Not found", className="text-danger"), [],[]  )









@app.callback(
    Output('user-name', 'children'),
    [Input('page-content', 'children')])
def cur_user(input1):

    if current_user.is_authenticated:
        return html.Div('Current user: ' + current_user.username)
        # 'User authenticated' return username in get_id()
    else:
        return ''


@app.callback(
    Output('logout', 'children'),
    [Input('page-content', 'children')])
def user_logout(input1):
    if current_user.is_authenticated:
        return html.A('Logout', href='/logout')
    else:
        return ''

# first input is the button clicks , second input is quiz answer picked up by student
# first output is the msg apear after user enter answer second output is the style of this msg ( color )
@app.callback([Output('data_quiz1_answer', 'children') , Output('data_quiz1_answer', 'style')  ],
              Input('data_quiz1_submit', 'n_clicks'),State('data_quiz1_choices', 'value') )
def data_quiz1_answer(clicks,answer):

    if answer=='hist': # check if answer is the correct answer
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db') #reading course table in database
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist() # reading the id of the current user
            ans=um.read_sql_cell('python_data_analysis','quiz1_state',index[0])  # reading the quiz1 answer that is recorded in database
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0]) # reading the course progress for the current user
            new_progress = '{}{}'.format(int(progress.split('%')[0]) + 10, '%') # increase the course progress
            if ans=='': # check if user already answered the quiz or its the first time
                um.edit_sql_cell('python_data_analysis','quiz1_state',index[0],'passed') # update the quiz1 state to passed
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress) # update the course progress in database
                return ('Correct Answer , Nice work..',dict(fontSize=22,color='green',fontWeight='bold')) # change the output string
            elif ans=='passed':
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold')) # user already answered so no update in database only return string
            elif ans == 'failed':
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                um.edit_sql_cell('python_data_analysis', 'quiz1_state', index[0], 'passed')
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))

    elif answer=='':
        return ('',dict(fontSize=22,color='green',fontWeight='bold'))

    else:
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz1_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) -10, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis', 'quiz1_state', index[0], 'failed')
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans=='passed':
                um.edit_sql_cell('python_data_analysis','quiz1_state',index[0],'failed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans == 'failed':
                return ('Wrong Answer , Try Again..', dict(fontSize=22, color='red', fontWeight='bold'))


@app.callback([Output('data_quiz2_answer', 'children') , Output('data_quiz2_answer', 'style')  ],
              Input('data_quiz2_submit', 'n_clicks'),State('data_quiz2_choices', 'value') )
def data_quiz2_answer(clicks,answer):

    if answer=='pd.Dataframe':
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz2_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) + 18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis','quiz2_state',index[0],'passed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Correct Answer , Nice work..',dict(fontSize=22,color='green',fontWeight='bold'))
            elif ans=='passed':
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))
            elif ans == 'failed':
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                um.edit_sql_cell('python_data_analysis', 'quiz2_state', index[0], 'passed')
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))

    elif answer=='':
        return ('',dict(fontSize=22,color='green',fontWeight='bold'))

    else:
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz2_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) -18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis', 'quiz2_state', index[0], 'failed')
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans=='passed':
                um.edit_sql_cell('python_data_analysis','quiz2_state',index[0],'failed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans == 'failed':
                return ('Wrong Answer , Try Again..', dict(fontSize=22, color='red', fontWeight='bold'))

@app.callback([Output('data_quiz3_answer', 'children') , Output('data_quiz3_answer', 'style')  ],
              Input('data_quiz3_submit', 'n_clicks'),State('data_quiz3_choices', 'value') )
def data_quiz3_answer(clicks,answer):

    if answer=='plotly':
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz3_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) + 18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis','quiz3_state',index[0],'passed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Correct Answer , Nice work..',dict(fontSize=22,color='green',fontWeight='bold'))
            elif ans=='passed':
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))
            elif ans == 'failed':
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                um.edit_sql_cell('python_data_analysis', 'quiz3_state', index[0], 'passed')
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))

    elif answer=='':
        return ('',dict(fontSize=22,color='green',fontWeight='bold'))

    else:
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz3_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) -18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis', 'quiz3_state', index[0], 'failed')
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans=='passed':
                um.edit_sql_cell('python_data_analysis','quiz3_state',index[0],'failed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans == 'failed':
                return ('Wrong Answer , Try Again..', dict(fontSize=22, color='red', fontWeight='bold'))



@app.callback([Output('data_quiz4_answer', 'children') , Output('data_quiz4_answer', 'style')  ],
              Input('data_quiz4_submit', 'n_clicks'),State('data_quiz4_choices', 'value') )
def data_quiz4_answer(clicks,answer):

    if answer=='line chart':
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz4_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) + 18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis','quiz4_state',index[0],'passed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Correct Answer , Nice work..',dict(fontSize=22,color='green',fontWeight='bold'))
            elif ans=='passed':
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))
            elif ans == 'failed':
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                um.edit_sql_cell('python_data_analysis', 'quiz4_state', index[0], 'passed')
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))

    elif answer=='':
        return ('',dict(fontSize=22,color='green',fontWeight='bold'))

    else:
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz4_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) -18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis', 'quiz4_state', index[0], 'failed')
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans=='passed':
                um.edit_sql_cell('python_data_analysis','quiz4_state',index[0],'failed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans == 'failed':
                return ('Wrong Answer , Try Again..', dict(fontSize=22, color='red', fontWeight='bold'))

@app.callback([Output('data_quiz5_answer', 'children') , Output('data_quiz5_answer', 'style')  ],
              Input('data_quiz5_submit', 'n_clicks'),State('data_quiz5_choices', 'value') )
def data_quiz5_answer(clicks,answer):

    if answer=='bootstrap':
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz5_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) + 18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis','quiz5_state',index[0],'passed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Correct Answer , Nice work..',dict(fontSize=22,color='green',fontWeight='bold'))
            elif ans=='passed':
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))
            elif ans == 'failed':
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                um.edit_sql_cell('python_data_analysis', 'quiz5_state', index[0], 'passed')
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))

    elif answer=='':
        return ('',dict(fontSize=22,color='green',fontWeight='bold'))

    else:
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz5_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) -18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis', 'quiz5_state', index[0], 'failed')
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans=='passed':
                um.edit_sql_cell('python_data_analysis','quiz5_state',index[0],'failed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans == 'failed':
                return ('Wrong Answer , Try Again..', dict(fontSize=22, color='red', fontWeight='bold'))


@app.callback([Output('data_quiz6_answer', 'children') , Output('data_quiz6_answer', 'style')  ],
              Input('data_quiz6_submit', 'n_clicks'),State('data_quiz6_choices', 'value') )
def data_quiz6_answer(clicks,answer):

    if answer=='callbacks':
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz6_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) + 18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis','quiz6_state',index[0],'passed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Correct Answer , Nice work..',dict(fontSize=22,color='green',fontWeight='bold'))
            elif ans=='passed':
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))
            elif ans == 'failed':
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                um.edit_sql_cell('python_data_analysis', 'quiz6_state', index[0], 'passed')
                return ('Correct Answer , Nice work..', dict(fontSize=22, color='green', fontWeight='bold'))

    elif answer=='':
        return ('',dict(fontSize=22,color='green',fontWeight='bold'))

    else:
        if current_user.is_authenticated:
            df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
            index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
            ans=um.read_sql_cell('python_data_analysis','quiz6_state',index[0])
            progress=um.read_sql_cell('python_data_analysis','Course_progress',index[0])
            new_progress = '{}{}'.format(int(progress.split('%')[0]) -18, '%')
            if ans=='':
                um.edit_sql_cell('python_data_analysis', 'quiz6_state', index[0], 'failed')
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans=='passed':
                um.edit_sql_cell('python_data_analysis','quiz6_state',index[0],'failed')
                um.edit_sql_cell('python_data_analysis', 'Course_progress', index[0], new_progress)
                return ('Wrong Answer , Try Again..',dict(fontSize=22,color='red',fontWeight='bold'))
            elif ans == 'failed':
                return ('Wrong Answer , Try Again..', dict(fontSize=22, color='red', fontWeight='bold'))




@app.callback(
    Output("collapse", "is_open"),
    [Input("rate_button", "n_clicks"),Input('submit_rating_button',"n_clicks")],
    [State("collapse", "is_open"),State("rate_input", "value")],
)
def toggle_collapse(n1,n2, is_open,input_value):
    if is_open==False:
        if n1:
            return True
        else:
            return False
    elif is_open==True:

        if n2 and (input_value>=1 and input_value<=5 ):
            if current_user.is_authenticated:
                df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
                index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
                um.edit_sql_cell('python_data_analysis', 'Course_Rating', index[0], input_value)

            return False
        return True

@app.callback(Output('hidden_div1','children'),
    Input('my_interval' , 'n_intervals')
)
def data_enrolled(time):

    if current_user.is_authenticated:
        df=pd.read_sql_table('python_data_analysis',con='sqlite:///users.db')
        index=df.index[df['student_id']=='{}'.format(current_user.id)].tolist()
        try:

            um.read_sql_cell('python_data_analysis', 'Enrolled', index[0])
            return 'enrolled'
        except:
            return 'not_enrolled'

@app.callback(Output('enroll_data','children'),
    Input('hidden_div1','children'))
def data_enrolled2(enroll_state):
    if enroll_state== 'enrolled' :
        return 'Continue Course'
    elif enroll_state== 'not_enrolled':
        return 'Enroll Course'
    return 'Enroll'

@app.callback(Output('enroll_data','active'),
              [Input('enroll_data','n_clicks'), Input('hidden_div1','children')  ]
              )
def data_enrolled3(enroll_data_btn,enroll_state) :
    if enroll_data_btn and enroll_state== 'enrolled':
        return True
    elif enroll_data_btn and enroll_state== 'not_enrolled':
        if current_user.is_authenticated:
            um.add_data_student(current_user.id,'yes','0%','','','','','','','','')
        return True
    return True


@app.callback(
    Output('our-table', 'data'),
    [Input('Add_Student', 'n_clicks')],
    [State('our-table', 'data'),
     State('our-table', 'columns')],
    prevent_initial_call=True)
def add_student(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

@app.callback(
    Output('our-table2', 'data'),
    [Input('Add_Student_To_Course', 'n_clicks')],
    [State('our-table2', 'data'),
     State('our-table2', 'columns')],
    prevent_initial_call=True)
def add_student_to_course(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

@app.callback(
    [Output('confirm_msg', 'children')],
    [Input('Save_To_Database', 'n_clicks')],
    [State('our-table', 'data'),State('our-table', 'columns')],
    prevent_initial_call=True)
def save_to_database1(clicks,data,columns):
    if clicks>0:
        df = pd.DataFrame(data,columns=['id','username','email','password'])
        df.to_sql("user", con='sqlite:///users.db', if_exists='replace', index=False)
        return ['Data saved successfully to Database']
    else:
        return ['']

@app.callback(
    [Output('confirm_msg2', 'children')],
    [Input('Save_To_Database2', 'n_clicks')],
    [State('our-table2', 'data'),State('our-table2', 'columns')],
    prevent_initial_call=True)
def save_to_database2(clicks,data,columns):
    if clicks>0:
        df = pd.DataFrame(data=data,columns=['student_id','Enrolled','Course_progress','Course_Rating'
                                             ,'quiz1_state','quiz2_state','quiz3_state','quiz4_state','quiz5_state','quiz6_state','final_exam_degree'])
        print(df)
        df.to_sql("python_data_analysis", con='sqlite:///users.db', if_exists='replace', index=False)
        return ['Data saved successfully to Database']
    else:
        return ['']



@app.callback([Output('postgres_datatable', 'children')],
              [Input('Refresh1', 'n_clicks')])
def refresh_table1(clicks):
    if clicks>=0:
        df = pd.read_sql_table('user', con='sqlite:///users.db')
        return [dash_table.DataTable(
            columns = [
                {
                    'name': str(x),
                    'id': str(x),
                    'deletable': False,
                } for x in df.columns
          ],id='our-table',
          data=df.to_dict('records'),    page_size=50
    ,style_cell=dict(textAlign= 'center', border= '2px solid black'
    ,backgroundColor= '#f0ad4e',color='black',fontSize='2vh',fontWeight='bold'),
    style_header=dict(backgroundColor= '#0275d8',
        fontWeight= 'bold', border= '1px solid black',fontSize='1.5vh'),
            editable=True,
            row_deletable=True,
            filter_action="native",
            sort_action="native",  # give user capability to sort columns
            sort_mode="single",  # sort across 'multi' or 'single' columns
            page_action='none',  # render all of the data at once. No paging.
            style_table={'height': '100%', 'overflowY': 'auto'}

)
            ]
    else:
        pass


@app.callback([Output('postgres_datatable2', 'children')],
              [Input('Refresh2', 'n_clicks')])
def refresh_table2(clicks):
    if clicks>=0:
        df2 = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        return [dash_table.DataTable(
            columns = [
                {
                    'name': str(x),
                    'id': str(x),
                    'deletable': False,
                } for x in df2.columns
             ],id='our-table2',
          data=df2.to_dict('records'),    page_size=50
    ,style_cell=dict(textAlign= 'center', border= '2px solid black'
    ,backgroundColor= '#f0ad4e',color='black',fontSize='2vh',fontWeight='bold'),
    style_header=dict(backgroundColor= '#0275d8',
        fontWeight= 'bold', border= '1px solid black',fontSize='1.5vh'),
            editable=True,
            row_deletable=True,
            filter_action="native",
            sort_action="native",  # give user capability to sort columns
            sort_mode="single",  # sort across 'multi' or 'single' columns
            page_action='none',  # render all of the data at once. No paging.
            style_table={'height': '100%', 'overflowY': 'auto'}

)
            ]

    else:
        pass


@app.callback([Output('progress', 'children'),Output('progress', 'value')],
              [Input('url', 'pathname')])
def update_data_progress(path):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        try :
            um.read_sql_cell('python_data_analysis', 'Enrolled', index[0])
            progress = um.read_sql_cell('python_data_analysis', 'Course_progress', index[0])
            if progress=='0%':
                return ('0%',5)
            else:
                return ('{}'.format(progress),int(progress.split('%')[0]) )
        except:
            return('0%',6)


@app.callback(Output('data_quiz1_choices','value'),
              Input('url','pathname'),State('data_quiz1_choices','value') )
def update_quiz1_state(path,value):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        state = um.read_sql_cell('python_data_analysis', 'quiz1_state', index[0])
        if state=='passed':
            return 'hist'
        else:
            return value

@app.callback(Output('data_quiz2_choices','value'),
              Input('url','pathname'),State('data_quiz2_choices','value' ) )
def update_quiz2_state(path,value):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        state = um.read_sql_cell('python_data_analysis', 'quiz2_state', index[0])
        if state=='passed':
            return 'pd.Dataframe'
        else:
            return value

@app.callback(Output('data_quiz3_choices','value'),
              Input('url','pathname') ,State('data_quiz3_choices','value') )
def update_quiz3_state(path,value):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        state = um.read_sql_cell('python_data_analysis', 'quiz3_state', index[0])
        if state=='passed':
            return 'plotly'
        else:
            return value


@app.callback(Output('data_quiz4_choices','value'),
              Input('url','pathname'),State('data_quiz4_choices','value' ) )
def update_quiz4_state(path,value):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        state = um.read_sql_cell('python_data_analysis', 'quiz4_state', index[0])
        if state=='passed':
            return 'line chart'
        else:
            return value

@app.callback(Output('data_quiz5_choices','value'),
              Input('url','pathname'),State('data_quiz5_choices','value' ) )
def update_quiz4_state(path,value):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        state = um.read_sql_cell('python_data_analysis', 'quiz5_state', index[0])
        if state=='passed':
            return 'bootstrap'
        else:
            return value

@app.callback(Output('data_quiz6_choices','value'),
              Input('url','pathname'),State('data_quiz6_choices','value' ) )
def update_quiz4_state(path,value):
    if current_user.is_authenticated:
        df = pd.read_sql_table('python_data_analysis', con='sqlite:///users.db')
        index = df.index[df['student_id'] == '{}'.format(current_user.id)].tolist()
        state = um.read_sql_cell('python_data_analysis', 'quiz6_state', index[0])
        if state=='passed':
            return 'callbacks'
        else:
            return value


def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents,style=dict(width='100%')),
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run_server(port=8400,host='0.0.0.0',debug=False)

import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
df=pd.read_sql_table('user',con='sqlite:///users.db')
df2=pd.read_sql_table('python_data_analysis',con='sqlite:///users.db')

add_student=dbc.Button("Add Student", color="primary", size='lg', n_clicks=0,id="Add_Student",
                          style=dict(marginTop='1rem',fontSize='1.1rem'))

save_btn1=dbc.Button("Save To Database", color="primary", size='lg', n_clicks=0,id='Save_To_Database',
                          style=dict(marginTop='1rem',fontSize='1.1rem'))

tables_navigation_header=dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Students Table", active='exact', href="/success",id='students_table')),
        dbc.NavItem(dbc.NavLink("Python Data Analysis Course", href="/data_course_table",active='exact',id='data_table')),
        dbc.NavItem(dbc.NavLink("Add Course", href="/Add_Course", active='exact', id='add_course'))
    ],
    pills=True,
)

students_table=html.Div([dash_table.DataTable(
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
    ,id='postgres_datatable')


db_tables_navigation_header=dbc.Col([tables_navigation_header],width='auto')


add_student_to_Course=dbc.Button("Add Student To Course", color="primary", size='lg', n_clicks=0,id="Add_Student_To_Course",
                          style=dict(marginTop='1rem',fontSize='1.1rem'))

save_btn2=dbc.Button("Save To Database", color="primary", size='lg', n_clicks=0,id='Save_To_Database2',
                          style=dict(marginTop='1rem',fontSize='1.1rem'))

data_course_table=html.Div([dash_table.DataTable(
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
    ,id='postgres_datatable2')

refresh_btn1=dbc.Button("Refresh Table", color="primary", size='lg', n_clicks=0,id='Refresh1',
                          style=dict(marginTop='1rem',fontSize='1.1rem'))

refresh_btn2=dbc.Button("Refresh Table", color="primary", size='lg', n_clicks=0,id='Refresh2',
                          style=dict(marginTop='1rem',fontSize='1.1rem'))






layout=html.Div([ dbc.Row([  db_tables_navigation_header  ]),html.Br(), students_table,
                  html.Div([add_student],style=dict(display='inline-block')),
                  html.Div([save_btn1],style=dict(display='inline-block',marginLeft='1vh')),
                  html.Div([''],id='confirm_msg',style=dict(fontSize=22,color='green',fontWeight='bold') ),
                  html.Br(),refresh_btn1,
                  dcc.Interval(id='interval', interval=2000)

]   )

layout2=html.Div([ dbc.Row([  db_tables_navigation_header  ]),html.Br(), data_course_table,
                  html.Div([add_student_to_Course],style=dict(display='inline-block')),
                  html.Div([save_btn2],style=dict(display='inline-block',marginLeft='1vh')),
                  html.Div([''],id='confirm_msg2',style=dict(fontSize=22,color='green',fontWeight='bold') ),
                  html.Br(),refresh_btn2,
                  dcc.Interval(id='interval', interval=2000)

]   )

course_card_design=html.H1('Course Card Design',
                           style=dict(fontSize=36,fontWeight='bold',color='#f0ad4e',textAlign='center'))

header_input=dbc.Input(
    placeholder='Enter Course Card Header',
    n_submit=0,
    type='text',
    id='box', bs_size="lg"
)

upload_image_div=html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            html.Div('Drag and Drop or ',style=dict(color='white',display='inline-block')),
            dbc.Button("Upload Card Image", color="primary", size='lg', n_clicks=0,
                       style=dict(fontSize='1.1rem',display='inline-block',marginLeft='5%'))
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload',style=dict(width='100%'))

])





layout3= html.Div([ dbc.Row([  db_tables_navigation_header]),
    dbc.Row([dbc.Col([ course_card_design,header_input, html.Br(),html.Br(),upload_image_div

]  ,

    xl=dict(size=4,offset=4),lg=dict(size=4,offset=4),
    md=dict(size=4,offset=4),sm=dict(size=4,offset=4),xs=dict(size=4,offset=4) )



])

])
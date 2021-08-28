import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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


data_video2_youtube=html.Div(children=[
            html.Iframe(width="100%%", height="474", src="https://www.youtube.com/embed/AW9Kh3UIo9E"
                       , title="YouTube video player"

                        ),
                  ])
data_quiz2_header=html.Div('what is the name of pandas function used to create dataframe ?',
                           style=dict(fontSize=22,color='black',fontWeight='black') )

data_quiz2_choices=dcc.RadioItems(
    options=[
        {'label': 'pd.Dataframe', 'value': 'pd.Dataframe'},
        {'label': 'pd.Index', 'value': 'pd.Index'},
        {'label': 'pd.Series', 'value': 'd.Series'},
        {'label': 'other', 'value': 'other'}
    ],
    value='',labelStyle=dict(display='block',color='black',marginLeft='1rem',fontSize=22),
    inputStyle=dict(width='1.2rem',height='1.2rem',marginRight='0.5rem') ,id='data_quiz2_choices',
    style=dict(marginLeft='4rem') , persistence=True
)

data_quiz2_submit=dbc.Button("Submit", color="primary", size='lg', n_clicks=0,id='data_quiz2_submit',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem'))

data_quiz2_answer=html.Div('',style=dict(fontSize=22,color='white',fontWeight='bold'),id='data_quiz2_answer')

data_quiz2=html.Div([ html.H1('Quiz2',style=dict(fontSize=32,color='black')),data_quiz2_header,html.Br(),
                      html.Hr(style=dict(color='black')) ,data_quiz2_choices


] ,style=dict(backgroundColor='#f0ad4e') )

data_video2_layout=dbc.Row([dbc.Col([html.Br(),sidebar

]  ,xl=dict(size=2,offset=0),lg=dict(size=2,offset=0),
    md=dict(size=5,offset=0),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_video2_youtube,html.Br(),html.Br(),
          data_quiz2,data_quiz2_submit,html.Br(),data_quiz2_answer

]  ,xl=dict(size=5,offset=2),lg=dict(size=5,offset=2),
    md=dict(size=3,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1) )




] , no_gutters=False  )


data_video3_youtube=html.Div(children=[
            html.Iframe(width="100%%", height="474", src="https://www.youtube.com/embed/-Dpko5DmlnE"
                       , title="YouTube video player"

                        ),
                  ])
data_quiz3_header=html.Div('package used to represent data in graphs ?',
                           style=dict(fontSize=22,color='black',fontWeight='black') )

data_quiz3_choices=dcc.RadioItems(
    options=[
        {'label': 'plotly', 'value': 'plotly'},
        {'label': 'numpy', 'value': 'numpy'},
        {'label': 'pandas', 'value': 'pandas'},
        {'label': 'other', 'value': 'other'}
    ],
    value='',labelStyle=dict(display='block',color='black',marginLeft='1rem',fontSize=22),
    inputStyle=dict(width='1.2rem',height='1.2rem',marginRight='0.5rem') ,id='data_quiz3_choices',
    style=dict(marginLeft='4rem') , persistence=True
)

data_quiz3_submit=dbc.Button("Submit", color="primary", size='lg', n_clicks=0,id='data_quiz3_submit',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem'))

data_quiz3_answer=html.Div('',style=dict(fontSize=22,color='white',fontWeight='bold'),id='data_quiz3_answer')

data_quiz3=html.Div([ html.H1('Quiz3',style=dict(fontSize=32,color='black')),data_quiz3_header,html.Br(),
                      html.Hr(style=dict(color='black')) ,data_quiz3_choices


] ,style=dict(backgroundColor='#f0ad4e') )

data_video3_layout=dbc.Row([dbc.Col([html.Br(),sidebar

]  ,xl=dict(size=2,offset=0),lg=dict(size=2,offset=0),
    md=dict(size=5,offset=0),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_video3_youtube,html.Br(),html.Br(),
          data_quiz3,data_quiz3_submit,html.Br(),data_quiz3_answer

]  ,xl=dict(size=5,offset=2),lg=dict(size=5,offset=2),
    md=dict(size=3,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1) )




] , no_gutters=False  )



data_video4_youtube=html.Div(children=[
            html.Iframe(width="100%%", height="474", src="https://www.youtube.com/embed/hSPmj7mK6ng"
                       , title="YouTube video player"

                        ),
                  ])
data_quiz4_header=html.Div('a Graph used to represent data over time ?',
                           style=dict(fontSize=22,color='black',fontWeight='black') )

data_quiz4_choices=dcc.RadioItems(
    options=[
        {'label': 'line chart', 'value': 'line chart'},
        {'label': 'scatter plot', 'value': 'scatter plot'},
        {'label': 'indicator', 'value': 'indicator'},
        {'label': 'other', 'value': 'other'}
    ],
    value='',labelStyle=dict(display='block',color='black',marginLeft='1rem',fontSize=22),
    inputStyle=dict(width='1.2rem',height='1.2rem',marginRight='0.5rem') ,id='data_quiz4_choices',
    style=dict(marginLeft='4rem') , persistence=True
)

data_quiz4_submit=dbc.Button("Submit", color="primary", size='lg', n_clicks=0,id='data_quiz4_submit',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem'))

data_quiz4_answer=html.Div('',style=dict(fontSize=22,color='white',fontWeight='bold'),id='data_quiz4_answer')

data_quiz4=html.Div([ html.H1('Quiz4',style=dict(fontSize=32,color='black')),data_quiz4_header,html.Br(),
                      html.Hr(style=dict(color='black')) ,data_quiz4_choices


] ,style=dict(backgroundColor='#f0ad4e') )

data_video4_layout=dbc.Row([dbc.Col([html.Br(),sidebar

]  ,xl=dict(size=2,offset=0),lg=dict(size=2,offset=0),
    md=dict(size=5,offset=0),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_video4_youtube,html.Br(),html.Br(),
          data_quiz4,data_quiz4_submit,html.Br(),data_quiz4_answer

]  ,xl=dict(size=5,offset=2),lg=dict(size=5,offset=2),
    md=dict(size=3,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1) )




] , no_gutters=False  )



data_video5_youtube=html.Div(children=[
            html.Iframe(width="100%%", height="474", src="https://www.youtube.com/embed/0mfIK8zxUds"
                       , title="YouTube video player"

                        ),
                  ])
data_quiz5_header=html.Div('you can make your app responsive using ?',
                           style=dict(fontSize=22,color='black',fontWeight='black') )

data_quiz5_choices=dcc.RadioItems(
    options=[
        {'label': 'bootstrap', 'value': 'bootstrap'},
        {'label': 'html', 'value': 'html'},
        {'label': 'flutter', 'value': 'flutter'},
        {'label': 'other', 'value': 'other'}
    ],
    value='',labelStyle=dict(display='block',color='black',marginLeft='1rem',fontSize=22),
    inputStyle=dict(width='1.2rem',height='1.2rem',marginRight='0.5rem') ,id='data_quiz5_choices',
    style=dict(marginLeft='4rem') , persistence=True
)

data_quiz5_submit=dbc.Button("Submit", color="primary", size='lg', n_clicks=0,id='data_quiz5_submit',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem'))

data_quiz5_answer=html.Div('',style=dict(fontSize=22,color='white',fontWeight='bold'),id='data_quiz5_answer')

data_quiz5=html.Div([ html.H1('Quiz5',style=dict(fontSize=32,color='black')),data_quiz5_header,html.Br(),
                      html.Hr(style=dict(color='black')) ,data_quiz5_choices


] ,style=dict(backgroundColor='#f0ad4e') )

data_video5_layout=dbc.Row([dbc.Col([html.Br(),sidebar

]  ,xl=dict(size=2,offset=0),lg=dict(size=2,offset=0),
    md=dict(size=5,offset=0),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_video5_youtube,html.Br(),html.Br(),
          data_quiz5,data_quiz5_submit,html.Br(),data_quiz5_answer

]  ,xl=dict(size=5,offset=2),lg=dict(size=5,offset=2),
    md=dict(size=3,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1) )




] , no_gutters=False  )


data_video6_youtube=html.Div(children=[
            html.Iframe(width="100%%", height="474", src="https://www.youtube.com/embed/mTsZL-VmRVE"
                       , title="YouTube video player"

                        ),
                  ])
data_quiz6_header=html.Div('you can make your app interactive using ?',
                           style=dict(fontSize=22,color='black',fontWeight='black') )

data_quiz6_choices=dcc.RadioItems(
    options=[
        {'label': 'callbacks', 'value': 'callbacks'},
        {'label': 'css', 'value': 'css'},
        {'label': 'html', 'value': 'html'},
        {'label': 'other', 'value': 'other'}
    ],
    value='',labelStyle=dict(display='block',color='black',marginLeft='1rem',fontSize=22),
    inputStyle=dict(width='1.2rem',height='1.2rem',marginRight='0.5rem') ,id='data_quiz6_choices',
    style=dict(marginLeft='4rem') , persistence=True
)

data_quiz6_submit=dbc.Button("Submit", color="primary", size='lg', n_clicks=0,id='data_quiz6_submit',
                          style=dict(marginTop='0.3rem',fontSize='1.1rem'))

data_quiz6_answer=html.Div('',style=dict(fontSize=22,color='white',fontWeight='bold'),id='data_quiz6_answer')

data_quiz6=html.Div([ html.H1('Quiz6',style=dict(fontSize=32,color='black')),data_quiz6_header,html.Br(),
                      html.Hr(style=dict(color='black')) ,data_quiz6_choices


] ,style=dict(backgroundColor='#f0ad4e') )

data_video6_layout=dbc.Row([dbc.Col([html.Br(),sidebar

]  ,xl=dict(size=2,offset=0),lg=dict(size=2,offset=0),
    md=dict(size=5,offset=0),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1)
    ) ,


dbc.Col([ html.Br(),data_video5_youtube,html.Br(),html.Br(),
          data_quiz6,data_quiz6_submit,html.Br(),data_quiz6_answer

]  ,xl=dict(size=5,offset=2),lg=dict(size=5,offset=2),
    md=dict(size=3,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1) )




] , no_gutters=False  )
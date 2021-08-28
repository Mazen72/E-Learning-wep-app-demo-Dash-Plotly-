import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
from server import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash
import dash_bootstrap_components as dbc

encoded3 = base64.b64encode(open('app_logo.jpg', 'rb').read())

app_logo=dbc.Row([dbc.Col([
    html.Img(src='data:image/png;base64,{}'.format(encoded3.decode()), id='app_logo', height=300,width='100%')
    ] ,
        xs=dict(size=8,offset=2), sm=dict(size=8,offset=2),
        md=dict(size=4,offset=4), lg=dict(size=4,offset=4), xl=dict(size=4,offset=4))
    ])

username_input=dbc.Input(
    placeholder='Enter your username',
    n_submit=0,
    type='text',
    id='uname-box', bs_size="lg",style=dict(backgroundColor= 'skyblue')
)

db_username_input=dbc.Col([html.Br(),username_input],
        xs=dict(size=8, offset=2), sm=dict(size=8, offset=2),
        md=dict(size=4, offset=4), lg=dict(size=4, offset=4), xl=dict(size=4, offset=4))

password_input=dbc.Input(
    placeholder='Enter your password',
    n_submit=0,
    type='password',
    id='pwd-box', bs_size="lg",style=dict(backgroundColor= 'skyblue')
)

db_password_input=dbc.Col([html.Br(),password_input],
        xs=dict(size=8, offset=2), sm=dict(size=8, offset=2),
        md=dict(size=4, offset=4), lg=dict(size=4, offset=4), xl=dict(size=4, offset=4))

submit_button= dbc.Button("Login", color="warning", size='lg', n_clicks=0, type='submit',
                            id='login-button',
                          style=dict(marginTop='1rem',fontSize='1.1rem',color='black',fontWeight='bold'))

db_submit_button=dbc.Col([html.Br(),submit_button],
        xs=dict(size=8, offset=2), sm=dict(size=8, offset=2),
        md=dict(size=4, offset=4), lg=dict(size=4, offset=4), xl=dict(size=4, offset=4))

login_state=html.Div(children='', id='output-state',style=dict(color='black',fontSize='1.5rem'))
db_login_state=dbc.Col([html.Br(),login_state],
        xs=dict(size=8, offset=2), sm=dict(size=8, offset=2),
        md=dict(size=5, offset=3), lg=dict(size=5, offset=3), xl=dict(size=5, offset=3))
layout = html.Div(
            children=[
                dcc.Location(id='url_login', refresh=True),html.Br(), app_logo,html.Br(),db_username_input,db_password_input
                ,db_submit_button,db_login_state

            ],style=dict(backgroundColor='white',height='70rem')

)

#check_password_hash(user.password, input2)
@app.callback(Output('url_login', 'pathname'),
              [Input('login-button', 'n_clicks'),
              Input('uname-box', 'n_submit'),
               Input('pwd-box', 'n_submit')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def sucess(n_clicks, n_submit_uname, n_submit_pwd, input1, input2):
    user = User.query.filter_by(username=input1).first()
    if user:
        if user.password==input2:
            login_user(user)
            return '/success'
        else:
            pass
    else:
        pass


@app.callback(Output('output-state', 'children'),
              [Input('login-button', 'n_clicks'),
               Input('uname-box', 'n_submit'),
               Input('pwd-box', 'n_submit')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def update_output(n_clicks, n_submit_uname, n_submit_pwd, input1, input2):
    if n_clicks > 0 or n_submit_uname > 0 or n_submit_pwd > 0:
        user = User.query.filter_by(username=input1).first()
        if user:
            if user.password==input2:
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''

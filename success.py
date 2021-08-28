import warnings
# Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
import dash_bootstrap_components as dbc
warnings.filterwarnings("ignore")

navigation_header=dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Courses", active='exact', href="/Courses",id='nav1')),
        dbc.NavItem(dbc.NavLink("My Courses", href="/My-Courses",active='exact',id='nav2')),
        dbc.NavItem(dbc.NavLink("Articles", active='exact', href="/Articles",id='nav4'))
    ],
    pills=True,
)

db_navigation_header=dbc.Col([navigation_header],width='auto')

# Create success layout
layout = html.Div(children=[
    dcc.Location(id='url_login_success', refresh=True),
    dbc.Row([  db_navigation_header  ])


     ])


# Create callbacks
@app.callback(Output('url_login_success', 'pathname'),
              [Input('logout_btn', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'












#url
#url_login_success
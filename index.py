from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

from app import app

teamStats = pd.read_csv('data/team_stats.csv')
teams = teamStats['Team'].unique()

app.layout = html.Div(children=[
    html.P("Select value"),
    dcc.Dropdown(teamStats.columns, id="select-y-axis"),
    html.Hr(),
    dcc.Graph(
        id='graph'
    )
    ])

@app.callback(
    Output('graph', 'figure'),
    Input('select-y-axis', 'value'))
def update_graph(select_axis):
    return px.bar(teamStats, x=teams, y=select_axis)

if __name__ == '__main__':
    app.run_server(debug=True)
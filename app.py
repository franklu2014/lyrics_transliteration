# base
import datetime
import socket
import os
import re
# external libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import nltk
import json
import pandas as pd
import plotly.graph_objs as go
import plotly_express as px
# languge

###########################################
# APP LAYOUT
###########################################

# COLOUR AND STYLE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {"white": "#ffffff",
          "light_grey": "#d2d7df",
          "ubc_blue": "#082145",
          "light_grey": "#d2d7df",
          "box1blue": "#8BBEE8FF ",
          "box2green": "#A8D5BAFF",
          "box3blue": "#8BBEE8FF",
          "box4green": "#A8D5BAFF",
          "black": "#000000",
          "light_purple": "#E3D1FB"
          }



# APP LAYOUT
app.layout = html.Div(style={'backgroundColor': colors['light_grey']}, children=[
    # HEADER
    html.Div(className="row", style={'backgroundColor': colors['black'], "padding": 10}, children=[
        html.H2('Language Transliteration App',
                style={'color': colors['white']})
    ]),

    # SELECTION HEADER 2
    html.Div(className="row", style={'backgroundColor': colors['light_grey'], "padding": 10}, children=[
        html.Div(className="two columns", style={'padding': 20}, children=[
        html.P('Source Language:',
                style={'color': colors['black']}),
        html.Br(),
        html.Label("Song name:")        
                ]),

        html.Div(className="ten columns", style={'padding': 20}, children=[        
            dcc.Dropdown(
                            id = 'pollutant1',
                            options=[
                                {'label': 'Mandarin to Pinyin', 'value': 1},
                                {'label': 'Cantonese to XXX', 'value': 2}
                            ],
                            value = 1,
                            style={'height': '30px', 'width': '300px'}),
            html.Br(),
             dcc.Input(id="topic_title", placeholder="Enter song name",
                      type="text", size="75", value="")
                    
    ])]),

    # MAIN BODY
    html.Div(className="row", children=[
        # # SIDEBAR
        # html.Div(className="two columns", style={'padding': 20}, children=[
        #     html.Img(src="assets/ubc-logo-2.png", width="50"),
        #     html.P("Home\nAnnouncements\nDiscussions\nGrades\nPeople")
        # ]),
        # DISCUSSION BOARD
        html.Div(className="six columns", style={"backgroundColor": colors['white'], "padding": 20}, children=[
    
            html.Br(),
            html.Br(),
            html.Label("Source lyrics:"),
            dcc.Input(id="topic_message", placeholder="Song lyrics",
                      type="text", size="75", style={'height': 250}),
            html.Br(),
            html.Br(),

        ]),
        html.Div(className="six columns", style={"backgroundColor": colors['white'], "padding": 20}, children=[
    

            html.Br(),
            html.Br(),
            html.Label("Model-generated lyrics:"),
            dcc.Input(id="topic_message2", placeholder="Song lyrics",
                      type="text", size="75", style={'height': 250}),
            html.Br(),
            html.Br(),


        ])
    ])
])



if __name__ == '__main__':
    app.run_server(debug=False)

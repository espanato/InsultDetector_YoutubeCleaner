import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
from most_insulted_video import most_insulted_video
from googleapiclient.discovery import build
from pourcentage_insultes import percent_insultes
from channel_videos import get_video_title

# KEY = "AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs"
# KEY = "AIzaSyAX7dBqLt4ihw9aNtkQZTAKw3mGs9hGRrQ"
KEY = 'AIzaSyARMcIOvEGxmAgdUQYCpSd3J669u2rpghA'
youtube = build('youtube', "v3", developerKey=KEY)


def search_video_channel(word, type_search='video'):
    if type_search == 'video':
        request = youtube.search().list(part='snippet', type='video',
                                        maxResults=1, q=word).execute()
        id_video = request['items'][0]['id']['videoId']
        return id_video

    elif type_search == 'channel':
        request = youtube.search().list(part='snippet', type='channel',
                                        maxResults=1, q=word).execute()
        id_channel = request['items'][0]['id']['channelId']
        return id_channel

    else:
        print("ERREUR : type inexistant\n")


def app_dash(input, type):
    if type == 'video':
        insul_perc = percent_insultes(input)[0]
        video_name = get_video_title(input)
        data = pd.DataFrame({
            "video": [input, input],
            'stats': [100-insul_perc, insul_perc]
        })
    elif type == 'channel':
        video_id, perc = most_insulted_video(input, 10)
        video_name = get_video_title(video_id)
        data = pd.DataFrame({
            "video": [input, input],
            'stats': [100-perc, perc]
        })

    options = [{'label': 'channel', 'value': 'channel'},
               {'label': 'video', 'value': 'video'}]
    app = dash.Dash(__name__)
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    fig = px.pie(data, values='stats', names=[
                 "% Commentaires neutres", "% Commentaires insultants"])

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Youtube Cleaner',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Label('URL ou Recherche', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        dcc.Input(id='text', value='', type='text'),
        html.Button(id='button', n_clicks=0, children='Go !'),
        dcc.RadioItems(id='radioitems', options=[{'label': 'URL', 'value': 'URL'}, {'label': 'recherche', 'value': 'recherche'}], value='URL', style={
            'color': colors['text']
        }),

        html.Br(),
        html.Label('Video ou chaîne :', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        dcc.Dropdown(
            id='values',
            options=options,
            value='video',
            clearable=None
        ),

        html.Div(children=f'Vidéo : {video_name}', style={
            'textAlign': 'center',
            'color': colors['text']
        }),


        dcc.Graph(
            id='graph',
            figure=fig
        )
    ])

    @app.callback(
        Output("graph", "figure"),
        [Input("button", "n_clicks")],
        [State("text", "value"),
         State("values", "value")]
    )
    def update_figure(n_clicks, text, dropdown):

        if dropdown == 'video':
            perc = percent_insultes(input)[0]
            data = pd.DataFrame({
                'video': [text, text],
                'stats': [100-perc, perc]
            })
            fig = px.pie(data, values='stats', names=[
                         "% Commentaires neutres", "% Commentaires insultants"])
        elif dropdown == 'channel':
            video_id, perc = most_insulted_video(input, 10)
            data = pd.DataFrame({
                "video": [input, input],
                'stats': [100-perc, perc]
            })
            fig = px.pie(data, values='stats', names=[
                         "% Commentaires neutres", "% Commentaires insultants"])
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
        )
        return fig

    app.run_server(debug=True)


app_dash("zooHc3m9mWE", 'video')

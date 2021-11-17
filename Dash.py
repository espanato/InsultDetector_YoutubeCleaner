import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
from most_insulted_video import most_insulted_video

<<<<<<< HEAD

KEY = "AIzaSyB13BBBdQR3muGiIR2dLoiycwZGQ30YYHs"
youtube = build('youtube',"v3",developerKey= KEY)

def search_video_channel(word,type_search='video'):
    if type_search == 'video':
        request = youtube.search().list(part='snippet',type='video',maxResults=1,q=word).execute()
        id_video = request['items'][0]['id']['videoId']
        return id_video

    elif type_search == 'channel' : 
        request = youtube.search().list(part='snippet',type='channel',maxResults=1,q=word).execute()
        id_channel = request['items'][0]['id']['channelId']
        return id_channel
    
    else :
        print("ERREUR : type inexistant\n")





def dash_channel(video_name):
=======
def dash_channel(video_id):
    video_name = get_video_name(video_id)
>>>>>>> 6a9fe7b (Dash)
    data = pd.DataFrame({  
        "video":[video_name, video_name],
        'stats':[93.6,6.4]
    })
    options = [{'label':'chaîne', 'value':'chaîne'},{'label':'video','value':'video'}]
    app = dash.Dash(__name__)
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    fig = px.pie(data, values = 'stats', names=["% Commentaires neutres","% Commentaires insultants"])

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='YoutubeCleaner',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Label('URL ou recherche',style = {
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Input(id = 'text',value='', type='text'),
        html.Button(id='button', n_clicks=0, children='Go !'),
        dcc.RadioItems(id = 'radioitems', options = [{'label':'URL', 'value':'URL'},{'label':'Recherche','value':'Recherche'}], value = 'URL',style = {
                'color': colors['text']
            }),

        html.Br(),
        html.Label('Video ou chaîne :',style = {
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Dropdown(
                id='values',
                options=options,
                value='video',
                clearable = None
            ),

        html.Div(children='Visualisation toxicité commentaires', style={
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
            data_f = pd.DataFrame({
                'video':[text,text],
                'stats':[50,50]
            })
            fig = px.pie(data_f, values = 'stats', names=["% Commentaires neutres","% Commentaires insultants"])
        elif dropdown =='chaîne':
            data_f = pd.DataFrame({
                'video':[text,text],
                'stats':[67,33]
            })
            fig = px.pie(data_f, values = 'stats', names=["% Commentaires neutres","% Commentaires insultants"])
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
        )
        return fig
    
    app.run_server(debug=True)

dash_channel("TRY2eQju5nc")
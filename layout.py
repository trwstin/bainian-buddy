import dash_core_components as dcc
import dash_html_components as html
import dash
import base64

# app settings
app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.title = "bai nian buddy"
server = app.server

# audio
sound_filename = 'assets/audio/新年快乐.mp3'
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

# app layout
app.layout = html.Div(
    [
        # Banner
        html.Div(
            [
                html.H4("bai nian buddy", className="header_text"),
            ],
            className="app_header",
        ),

        html.Div(
            html.H1('新年快乐',
                id='greeting',
                title='新年快乐',
                style={'padding-top':'50px'},
            ),
        
        style={"display": "flex", "justifyContent": "center"}
        ),

        html.Div(id='hanyu-pinyin', style={"display": "flex", "justifyContent": "center"}),

        html.Div(id='translation', style={"display": "flex", "justifyContent": "center"}),

        html.Div(children=[
            html.Button('Text-To-Speech', id='tts', n_clicks=0, className='button'),
            html.Audio(id='audio-player', src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                          controls=True,
                          autoPlay=False,
                          style={"display": "none"}
                          ),
            html.Div(id="placeholder", style={"display": "none"})],  
            style={"display": "flex", "justifyContent": "center", 'margin-top':'40px'}
        ),

        html.Div(
            html.A(
                html.Img(
                    src=app.get_asset_url("loop.png"),
                    id='refresh',
                    title='Click to generate a new greeting',
                    n_clicks=0,
                    style={'width':'150px', 'height':'auto', 'padding-top':'50px'}
                ),
                style={"display": "flex", "justifyContent": "center"}
            )
        )
    ]
)


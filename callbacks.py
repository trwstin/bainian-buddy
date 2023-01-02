from dash.dependencies import Input, Output
from functions import *
from layout import *
import pinyin

# Display pinyin and translation
@app.callback(
    [Output('hanyu-pinyin', 'children'),
    Output('translation','children')],
    [Input('greeting', 'title')]
)
def update_output(title):
    pyin = pinyin.get(" ".join(title))
    trans = translate(title)
    return '\n{}'.format(pyin), trans

# Refresh for new phrase
@app.callback(
    [Output('greeting', 'children'),
    Output('greeting','title'),
    Output('audio-player','src')],
    [Input('greeting', 'children'),
    Input('greeting','title'),
    Input('audio-player','src'),
    Input('refresh','n_clicks')]
)
def refresh(children, title, src, n_clicks):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if n_clicks > 0 and 'refresh' in changed_id:
            lst = list(dict.keys(phrases))
            lst.remove(children)
            phrase = random.choice(lst)

            sound_filename = 'assets/audio/{}.mp3'.format(phrase)
            encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
            audio = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())
            
            return phrase, phrase, audio
    else:
        return children, title, src

# Play text-to-speech
app.clientside_callback(
    """
    function(n) {
      var audio = document.querySelector('#audio-player');
      if (!audio){
        return -1;
      }
      audio.play();
      return '';
   }
    """, Output('placeholder', 'children'), [Input('tts', 'n_clicks')],
    prevent_initial_call=True
)
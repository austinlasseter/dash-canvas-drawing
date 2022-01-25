import dash
from api_keys.myapikey  import apikey


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3(f'my api key is: {apikey}'),

], className='container')


if __name__ == '__main__':
    app.run_server(debug=True)

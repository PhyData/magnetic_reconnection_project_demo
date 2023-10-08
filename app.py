import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Magnetic Reconnection: Alert system of solar flares" 

app.layout = html.Div([html.Div([
    html.H1('Magnetic Reconnection: Alert system of magnetic reconnection [DEMO]', className="header-title"),        
    html.P(children=("Project submitted to NASA in the context of the NASA space apps challenge"),className="header-description",),
    html.Img(src='assets/LOGO.png', style={'width': '15%', 'margin': '-12px auto', 'display': 'block'}),        
            ],className="header"), 
    html.Br(),
    html.Br(),
    html.H3('Alert system of potential dangerous magnetic reconnection using flare data', className="header-title"),
    html.P(children=[' Last three Average magnetic field data [nT]: ( 8.4, 8.9 , 5.5 )'],className="body"),
    html.P(children=[' Last three magnetic field data in z [nT]: ( -4.7 , -2.7 , -2.2 )'],className="body"),
    html.P(children=[' Decil associated with the magnetic field data in z: ( 1 , 1 , 1 )'],className="body"), 
    html.P(children=[' Last three plasma speed data [km/s]: ( 428 , 412 , 393 )'],className="body"),
    html.P(children=[' Last three Xray flux [W/m^2]: ( 0.0000013 , 0.0000058 , 0.0000024 )'],className="body"), 
    html.P(children=[' Last three flare class: ( C , C , C )'],className="body"),  
    html.P(children=[' Time between events: ( 120h , 5h , 49h )'],className="body"),
    html.Br(),
    html.Br(),
    html.P(children=[' The next potential dangerous earth magnetic reconnection due to solar flare detected at L1 should be at: 15.7h, 0.9 confidence.'],className="body_h"),

    html.Br(),
    html.Br(),
    
    html.H3('Data analysis', className="header-title"),

    html.P(children=['We present the plots with the average magnetic field and the Bz component (in nano Tesla), \
                      from the NASA dataset IMF and Plasma Data, and Energetic Proton Fluxes, Time-Shifted to the \
                      Nose of the Earth Bow Shock, plus Solar and Magnetic Indices - J.H. King, N. Papitashvili (ADNET, NASA GSFC).'],className="body"),

    html.Div([
    html.Img(src='assets/Avg_B.png', style={'width': '50%', 'margin': '0 auto', 'display': 'block'}),
    html.Img(src='assets/Bz.png', style={'width': '50%', 'margin': '0 auto', 'display': 'block'}),
],),
   
html.Div([
    html.P('Here, the average values shows peaks of the magnetic field when is was sensed in the Lagrange 1 point. \
            We can also observe importante peaks between 2012 and 2013. However, the relevant data to study reconnection \
            is the negative Bz component. When this component of the sensed magnetic field aligns with the negative \
            z component of the Earth, we spot a reconnection in the magnetic field.'),
            html.H2('Comparing with solar flare data'),
    html.P('The idea of this analysis is to compare with the database of solar flares from (http://solarmuri.ssl.berkeley.edu/~kazachenko/RibbonDB) and published in [Kazachenko, Maria & Lynch, B. & Welsch, Brian & Sun, Xudong. (2017)]. We use this data to compare their ocurrence with the magnetic reconection in earth. We plot the data of the ocurrencies in time, similar to the previous plots'),         
],className="body"),
html.Div([
    html.Img(src='assets/Sharp.png', style={'width': '50%', 'margin': '0 auto', 'display': 'block'}),
],),
html.Div([
    html.P('By simple inspection, we can see certain correlation between the peaks of the magnetic field Avg_B and the solar flares data. Anyway, in order to compare both phenomena, we have to be sure that the alignment of the z component of the field is antiparalell with the positive Earth magnetic direction.'),         
],className="body"),

html.Div([
    html.P('As part of our analysis we plot the Kaplan-Meier curves, that shows the probability of the magnetic reconnection by hours.'),         
],className="body"),

html.Div([
    html.Img(src='assets/KM-plot.png', style={'width': '50%', 'margin': '0 auto', 'display': 'block'}),
],),

html.Div([
    html.P('We also include the probability of the magnetic reconnection by class of solar flare (Class C and Class M) by hours.'),         
],className="body"),

html.Div([
    html.Img(src='assets/KM-plot-classC.png', style={'width': '50%', 'margin': '0 auto', 'display': 'block'}),
],),

html.Div([
    html.Img(src='assets/KM-plot-classM.png', style={'width': '50%', 'margin': '0 auto', 'display': 'block'}),
],),
    
    #html.Div([
    #gif.GifPlayer(
    #    gif='assets/wood.gif',
    #    still='assets/still.png',)
    #],style={'width': '49%', 'display': 'inline-block'} ,className="grafico"),

    #html.Div([
    #gif.GifPlayer(
    #    gif='assets/wood.gif',
    #    still='assets/still.png',)
    #],style={'width': '49%', 'display': 'inline-block'} ,className="grafico"),    
   
]) 

if __name__ == '__main__':
    app.run_server(debug=True)

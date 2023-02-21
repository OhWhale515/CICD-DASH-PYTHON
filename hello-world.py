from dash2 import Dash, dcc               # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
demo = dcc.Markdown(children="# CI/CD Dash Python Demo!")

# Customize your own Layout
app.layout = dbc.Container([demo])

# Run app
if __name__=='__main__':
    app.run_server(port=8051)
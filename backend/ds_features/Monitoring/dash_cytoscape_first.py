from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            {'data': {'id': 'one', 'label': 'Node 1'},},
            {'data': {'id': 'two', 'label': 'Node 2'},},
            {'data': {'id': 'three', 'label': 'Node 3'},},
            {'data': {'id': 'four', 'label': 'Node 4'}, },
            {'data': {'source': 'one', 'target': 'two'}},
            {'data': {'source': 'one', 'target': 'two', 'label': 'Node 1 to 2'}}
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

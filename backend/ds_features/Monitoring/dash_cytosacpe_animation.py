from dash import Dash, html, dcc
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import time

app = Dash(__name__)

global sss
sss = [            {                'selector': 'node[id="one"]',                'style': {                    'background-color': 'lightblue',                    'label': 'data(label)',                    'text-valign': 'center',                    'text-halign': 'center',                    'width': '70px',                    'height': '70px'                }            },            {                'selector': 'node[id="two"]',                'style': {                    'background-color': 'lightgreen',                    'label': 'data(label)',                    'text-valign': 'center',                    'text-halign': 'center',                    'width': '50px',                    'height': '50px'                }            },            {                'selector': 'node[id="three"]',                'style': {                    'background-color': 'orange',                    'label': 'data(label)',                    'text-valign': 'center',                    'text-halign': 'center',                    'width': '60px',                    'height': '60px'                }            },            {                'selector': 'node[id="four"]',                'style': {                    'background-color': 'lightgray',                    'label': 'data(label)',                    'text-valign': 'center',                    'text-halign': 'center',                    'width': '80px',                    'height': '80px'                }            },            {                'selector': '.highlighted',                'style': {                    'background-color': 'red'                }            },            {                'selector': 'edge',                'style': {                    'curve-style': 'bezier',                    'target-arrow-shape': 'triangle',                    'line-color': 'gray',                    'target-arrow-color': 'gray'                }            },            {                'selector': '.highlighted-edge',                'style': {                    'line-color': 'red',                    'target-arrow-color': 'red'                }            }        ]

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            {'data': {'id': 'one', 'label': 'Node 1'}},
            {'data': {'id': 'two', 'label': 'Node 2'}},
            {'data': {'id': 'three', 'label': 'Node 3'}},
            {'data': {'id': 'four', 'label': 'Node 4'}},
            {'data': {'source': 'one', 'target': 'two'}},
            {'data': {'source': 'two', 'target': 'three'}},
            {'data': {'source': 'three', 'target': 'four'}},
            {'data': {'source': 'four', 'target': 'one'}}
        ],
        stylesheet = sss

    )
])

global counter
counter = 2

all_node_data = [
    {'id': 'one', 'label': 'Node 1'},
    {'id': 'two', 'label': 'Node 2'},
    {'id': 'three', 'label': 'Node 3'},
    {'id': 'four', 'label': 'Node 4'},
]

@app.callback(
    Output('cytoscape-two-nodes', 'stylesheet'),
    Input('cytoscape-two-nodes', 'stylesheet'),
    allow_duplicate=True
)
def highlight_node(stylesheet):
    # for i in range(100):
    global counter
    node_data = all_node_data[counter]
    counter += 1
    print(node_data)
    new_style = stylesheet.copy()
    for i, selector in enumerate(['#one', '#two', '#three', '#four']):
        if node_data['id'] == selector[1:]:
            sss[i]['style']['background-color'] = 'red'
        else:
            sss[i]['style']['background-color'] = 'gray'
    # return sss


# @app.callback(
#     Output('cytoscape-two-nodes', 'stylesheet'),
#     Input('cytoscape-two-nodes', 'stylesheet'),
#     allow_duplicate=True
# )
# def highlight_node(node_data, stylesheet):
#     if node_data:
#         new_style = stylesheet.copy()
#         for i, selector in enumerate(['#one', '#two', '#three', '#four']):
#             if node_data['id'] == selector[1:]:
#                 new_style[i]['style']['background-color'] = 'red'
#             else:
#                 new_style[i]['style']['background-color'] = 'gray'
#         return new_style
#     else:
#         return stylesheet

# @app.callback(
#     Output('cytoscape-two-nodes', 'stylesheet'),
#     Input('cytoscape-two-nodes', 'stylesheet')
# )
# def highlight_next_node(stylesheet):
#     print("I CAME")
#     time.sleep(1) # add a delay to slow down the animation
#     new_style = stylesheet.copy()
#     for i, selector in enumerate(['#one', '#two', '#three', '#four']):
#         if 'highlighted' in new_style[i]['selector']:
#             new_style[i]['selector'] = selector
#             new_style[i]['style']['background-color'] = 'gray'
#             new_style[(i+4-1)%4]['style']['line-color'] = 'gray'
#             new_style[(i+1)%4]['style']['line-color'] = 'gray'
#             new_style[(i+4-1)%4]['style']['target-arrow-color'] = 'gray'
#             new_style[i]['style']['label'] = ''
#             new_style[(i+4-1)%4]['style']['label'] = ''
#             break
#         new_style[(i+1)%4]['selector'] += '.highlighted'
#         new_style[(i+1)%4]['style']['background-color'] = 'red'
#         new_style[i%4]['style']['line-color'] = 'red'
#         new_style[i%4]['style']['target-arrow-color'] = 'red'
#         new_style[(i+1)%4]['style']['label'] = '->'
#         new_style[i%4]['style']['label'] = ''
    return new_style

if __name__ == '__main__':
    app.run_server(debug=True)
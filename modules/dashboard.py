import plotly.express as px
from dash import Dash, dcc, html

def launch_dashboard(df, funnel_stats):
    """
    Build and run a Dash app with:
     - drill-down funnel viz
     - cohort heatmaps
     - event “heartbeat” time-series
    """
    app = Dash(__name__)

    fig_funnel = px.funnel(
        funnel_stats,
        x="conversion_rate",
        y="step",
        title="Conversion Funnel"
    )
    app.layout = html.Div([
        html.H1("Digital Funnel Analytics"),
        dcc.Graph(figure=fig_funnel),
        # TODO: add more charts and controls...
    ])

    app.run_server(debug=True)

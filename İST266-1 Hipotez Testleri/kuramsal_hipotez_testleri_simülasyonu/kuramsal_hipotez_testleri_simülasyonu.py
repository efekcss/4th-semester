# ========================================================
# Kuramsal Hipotez Testleri Simülasyonu Kodları
# ========================================================

import webbrowser
from threading import Timer

import numpy as np
from scipy.stats import norm

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)
server = app.server

MU0_DEFAULT = 0.0
MU1_DEFAULT = 2.0
SIGMA_DEFAULT = 1.0
ALPHA_DEFAULT = 0.10
N_DEFAULT = 10

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

def standard_error(sigma, n):
    return sigma / np.sqrt(n)

def get_critical_values(alpha, mu0, sigma, n, test_type):
    se = standard_error(sigma, n)

    if test_type == "right":
        zcrit = norm.ppf(1 - alpha)
        return {"right": mu0 + zcrit * se}

    if test_type == "left":
        zcrit = norm.ppf(1 - alpha)
        return {"left": mu0 - zcrit * se}

    if test_type == "two":
        zcrit = norm.ppf(1 - alpha / 2)
        return {
            "left": mu0 - zcrit * se,
            "right": mu0 + zcrit * se
        }

def compute_beta(mu1, sigma, n, criticals, test_type):
    se = standard_error(sigma, n)

    if test_type == "right":
        return norm.cdf(criticals["right"], loc=mu1, scale=se)

    if test_type == "left":
        return 1 - norm.cdf(criticals["left"], loc=mu1, scale=se)

    if test_type == "two":
        return (
            norm.cdf(criticals["right"], loc=mu1, scale=se)
            - norm.cdf(criticals["left"], loc=mu1, scale=se)
        )

def direction_warning(test_type, mu0, mu1):
    if test_type == "left" and mu1 >= mu0:
        return (
            "❗ Uyarı: Sol kuyruk testi (μ₁ < μ₀) seçili, ancak μ₁ ≥ μ₀. "
            "Bu durumda alternatif dağılım red bölgesinden uzak kalır. "
            "β çok büyük, güç çok düşüktür."
        )

    if test_type == "right" and mu1 <= mu0:
        return (
            "❗ Uyarı: Sağ kuyruk testi (μ₁ > μ₀) seçili, ancak μ₁ ≤ μ₀. "
            "Bu durumda alternatif dağılım red bölgesinden uzak kalır. "
            "β çok büyük, güç çok düşüktür."
        )

    return ""

def make_figure(mu0, mu1, sigma, alpha, n, test_type):
    se = standard_error(sigma, n)
    criticals = get_critical_values(alpha, mu0, sigma, n, test_type)
    beta = compute_beta(mu1, sigma, n, criticals, test_type)

    x = np.linspace(min(mu0, mu1) - 4.5 * se, max(mu0, mu1) + 4.5 * se, 2000)

    y0 = norm.pdf(x, mu0, se)
    y1 = norm.pdf(x, mu1, se)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y0,
        mode="lines",
        name="H₀",
        line=dict(color="blue", width=3),
        hovertemplate="H₀<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=x,
        y=y1,
        mode="lines",
        name="H₁",
        line=dict(color="red", dash="dash", width=3),
        hovertemplate="H₁<extra></extra>"
    ))

    fig.add_vline(
        x=mu0,
        line_dash="dot",
        line_color="gray",
        annotation_text=f" μ₀ = {mu0:.2f}",
        annotation_position="bottom",
        annotation_font_size=20,
        annotation_font_color="black",
        annotation_yshift=-20
    )

    fig.add_vline(
        x=mu1,
        line_dash="dot",
        line_color="gray",
        annotation_text=f" μ₁ = {mu1:.2f}",
        annotation_position="bottom",
        annotation_font_size=20,
        annotation_font_color="black",
        annotation_yshift=-20
    )

    if test_type == "right":
        c = criticals["right"]

        fig.add_vline(
            x=c,
            line_width=3,
            line_color="#2f4f6f"
        )

        xa = x[x >= c]
        ya = norm.pdf(xa, mu0, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xa, xa[::-1]]),
            y=np.concatenate([ya, np.zeros_like(ya)]),
            fill="toself",
            mode="none",
            name=f"α = {alpha:.3f}",
            fillcolor="rgba(255,0,0,0.4)",
            hoveron="fills",
            text=[f"α = {alpha:.3f}"] * (2 * len(xa)),
            hoverinfo="text"
        ))

        xb = x[x <= c]
        yb = norm.pdf(xb, mu1, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xb, xb[::-1]]),
            y=np.concatenate([yb, np.zeros_like(yb)]),
            fill="toself",
            mode="none",
            name=f"β = {beta:.3f}",
            fillcolor="rgba(0,0,255,0.2)",
            hoveron="fills",
            text=[f"β = {beta:.3f}"] * (2 * len(xb)),
            hoverinfo="text"
        ))
        
        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode="lines",
            name=f"Güç = {1 - beta:.3f}",
            line=dict(color="rgba(0,0,0,0)")
        ))

    elif test_type == "left":
        c = criticals["left"]

        fig.add_vline(
            x=c,
            line_width=3,
            line_color="#2f4f6f"
        )

        xa = x[x <= c]
        ya = norm.pdf(xa, mu0, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xa, xa[::-1]]),
            y=np.concatenate([ya, np.zeros_like(ya)]),
            fill="toself",
            mode="none",
            name=f"α = {alpha:.3f}",
            fillcolor="rgba(255,0,0,0.4)",
            hoveron="fills",
            text=[f"α = {alpha:.3f}"] * (2 * len(xa)),
            hoverinfo="text"
        ))

        xb = x[x >= c]
        yb = norm.pdf(xb, mu1, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xb, xb[::-1]]),
            y=np.concatenate([yb, np.zeros_like(yb)]),
            fill="toself",
            mode="none",
            name=f"β = {beta:.3f}",
            fillcolor="rgba(0,0,255,0.2)",
            hoveron="fills",
            text=[f"β = {beta:.3f}"] * (2 * len(xb)),
            hoverinfo="text"
        ))
        
        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode="lines",
            name=f"Güç = {1 - beta:.3f}",
            line=dict(color="rgba(0,0,0,0)")
        ))

    else:
        cl = criticals["left"]
        cr = criticals["right"]

        fig.add_vline(
            x=cl,
            line_width=3,
            line_color="#2f4f6f"
        )

        fig.add_vline(
            x=cr,
            line_width=3,
            line_color="#2f4f6f"
        )

        xa_left = x[x <= cl]
        ya_left = norm.pdf(xa_left, mu0, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xa_left, xa_left[::-1]]),
            y=np.concatenate([ya_left, np.zeros_like(ya_left)]),
            fill="toself",
            mode="none",
            name=f"α/2 = {alpha/2:.3f}",
            fillcolor="rgba(255,0,0,0.4)",
            hoveron="fills",
            text=[f"α/2 = {alpha/2:.3f}"] * (2 * len(xa_left)),
            hoverinfo="text"
        ))

        xa_right = x[x >= cr]
        ya_right = norm.pdf(xa_right, mu0, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xa_right, xa_right[::-1]]),
            y=np.concatenate([ya_right, np.zeros_like(ya_right)]),
            fill="toself",
            mode="none",
            name=f"α/2 = {alpha/2:.3f}",
            fillcolor="rgba(255,0,0,0.4)",
            hoveron="fills",
            text=[f"α/2 = {alpha/2:.3f}"] * (2 * len(xa_right)),
            hoverinfo="text",
            showlegend=False
        ))

        xb = x[(x >= cl) & (x <= cr)]
        yb = norm.pdf(xb, mu1, se)

        fig.add_trace(go.Scatter(
            x=np.concatenate([xb, xb[::-1]]),
            y=np.concatenate([yb, np.zeros_like(yb)]),
            fill="toself",
            mode="none",
            name=f"β = {beta:.3f}",
            fillcolor="rgba(0,0,255,0.2)",
            hoveron="fills",
            text=[f"β = {beta:.3f}"] * (2 * len(xb)),
            hoverinfo="text"
        ))
        
        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode="lines",
            name=f"Güç = {1 - beta:.3f}",
            line=dict(color="rgba(0,0,0,0)")
        ))

    fig.update_layout(
        title=dict(
            text="I Tip Hata, II Tip Hata ve Testin Gücü",
            x=0.05,
            font=dict(
                family="Times New Roman, serif",
                size=25,
                color="black"
            )
        ),
        template="plotly_white",
        height=700,
        font=dict(
            family="Times New Roman, serif",
            size=18,
            color="black"
        ),
        legend=dict(
            x=1.02,
            y=0.5,
            xanchor="left",
            yanchor="middle",
            font=dict(
                size=24,
                family="Times New Roman, serif"
            ),
            itemsizing="constant"
        ),
        margin=dict(l=80, r=80, t=100, b=80)
    )

    fig.update_xaxes(
        title_font=dict(size=22, family="Times New Roman, serif"),
        tickfont=dict(size=16, family="Times New Roman, serif")
    )

    fig.update_yaxes(
        title_font=dict(size=22, family="Times New Roman, serif"),
        tickfont=dict(size=16, family="Times New Roman, serif")
    )

    return fig, beta

app.layout = html.Div([
    html.H3(
        "Kuramsal Hipotez Testleri Simülasyonu",
        style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "24px",
            "fontWeight": "bold"
        }
    ),

    dcc.RadioItems(
        id="test-type",
        options=[
            {"label": "μ₁ > μ₀", "value": "right"},
            {"label": "μ₁ < μ₀", "value": "left"},
            {"label": "μ₁ ≠ μ₀", "value": "two"},
        ],
        value="right",
        inline=True,
        style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "25px"
        }
    ),

    html.Label(
        "α",
        style={"fontFamily": "Times New Roman, serif", "fontSize": "25px"}
    ),
    dcc.Slider(0.01, 0.2, 0.01, value=ALPHA_DEFAULT, id="alpha"),

    html.Label(
        "μ₀",
        style={"fontFamily": "Times New Roman, serif", "fontSize": "25px"}
    ),
    dcc.Slider(-3, 3, 0.1, value=MU0_DEFAULT, id="mu0"),

    html.Label(
        "μ₁",
        style={"fontFamily": "Times New Roman, serif", "fontSize": "25px"}
    ),
    dcc.Slider(-5, 5, 0.1, value=MU1_DEFAULT, id="mu1"),

    html.Label(
        "σ",
        style={"fontFamily": "Times New Roman, serif", "fontSize": "25px"}
    ),
    dcc.Slider(0.5, 3, 0.1, value=SIGMA_DEFAULT, id="sigma"),

    html.Label(
        "n",
        style={"fontFamily": "Times New Roman, serif", "fontSize": "25px"}
    ),
    dcc.Slider(2, 100, 1, value=N_DEFAULT, id="n"),

    html.Div(
        id="warning",
        style={
            "color": "#b00020",
            "backgroundColor": "#ffe6e6",
            "border": "1px solid #ffb3b3",
            "padding": "10px",
            "borderRadius": "6px",
            "marginTop": "10px",
            "marginBottom": "10px",
            "fontFamily": "Times New Roman, serif",
            "fontSize": "25px",
            "textAlign": "center"
        }
    ),

    html.Div(
        id="info",
        style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "22px",
            "fontWeight": "bold",
            "marginTop": "10px",
            "marginBottom": "10px"
        }
    ),

    dcc.Graph(id="graph")
], style={"padding": "20px"})

@app.callback(
    Output("graph", "figure"),
    Output("warning", "children"),
    Output("info", "children"),
    Input("test-type", "value"),
    Input("alpha", "value"),
    Input("mu0", "value"),
    Input("mu1", "value"),
    Input("sigma", "value"),
    Input("n", "value"),
)
def update(test_type, alpha, mu0, mu1, sigma, n):
    fig, beta = make_figure(mu0, mu1, sigma, alpha, n, test_type)
    warning_msg = direction_warning(test_type, mu0, mu1)
    return fig, warning_msg, ""

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)
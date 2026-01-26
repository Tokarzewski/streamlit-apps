"""
Streamlit Feature Demo Application
===================================
A comprehensive showcase of Streamlit's features and functionalities.
"""

import streamlit as st
from datetime import datetime

# Import page modules
from custom_pages import (
    home,
    text_markdown,
    data_display,
    charts,
    input_widgets,
    layout_containers,
    styling_theming,
    css_showcase,
    advanced_features,
    utilities,
)

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Streamlit Feature Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://docs.streamlit.io",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "# Streamlit Feature Demo\nA comprehensive showcase of all Streamlit features!",
    },
)

# =============================================================================
# SIDEBAR NAVIGATION
# =============================================================================
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    st.title("Navigation")

    page = st.radio(
        "Select a Feature Category:",
        [
            "🏠 Home",
            "📝 Text & Markdown",
            "📊 Data Display",
            "📈 Charts & Visualizations",
            "🎛️ Input Widgets",
            "📐 Layout & Containers",
            "🎨 Styling & Theming",
            "✨ CSS Showcase",
            "⚡ Advanced Features",
            "🔧 Utilities",
        ],
        index=0,
    )

    st.divider()

    # Sidebar widgets demo
    st.subheader("Sidebar Widgets")
    theme = st.selectbox("Theme", ["Dark", "Custom"])
    show_code = st.checkbox("Show Code Examples", value=False)

    st.divider()
    st.caption("Built with Streamlit 🎈")
    st.caption(f"Current time: {datetime.now().strftime('%H:%M:%S')}")

# =============================================================================
# CUSTOM CSS STYLING (Theme-dependent)
# =============================================================================

# Theme color and font definitions
if theme == "Dark":
    bg_color = "#0e1117"
    secondary_bg = "#262730"
    text_color = "#fafafa"
    card_bg = "#1e1e2e"
    card_border = "#FF4B4B"
    accent_color = "#FF4B4B"
    font_family = "'JetBrains Mono', 'Fira Code', 'Consolas', monospace"
    heading_font = "'Inter', 'Segoe UI', sans-serif"
    font_import = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');"
else:
    bg_color = "#1a1a2e"
    secondary_bg = "#16213e"
    text_color = "#eaeaea"
    card_bg = "#0f3460"
    card_border = "#e94560"
    accent_color = "#e94560"
    font_family = "'Poppins', 'Nunito', sans-serif"
    heading_font = "'Orbitron', 'Rajdhani', sans-serif"
    font_import = "@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap');"


st.markdown(
    f"""
    <style>
    /* Import custom fonts */
    {font_import}

    /* Theme-based styling */
    .stApp {{
        background-color: {bg_color};
        font-family: {font_family};
    }}

    .stApp > header {{
        background-color: {bg_color};
    }}

    .stMarkdown, .stText, p, span, label {{
        color: {text_color} !important;
        font-family: {font_family};
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
        font-family: {heading_font};
        {"letter-spacing: 1px;" if theme == "Custom" else ""}
    }}

    /* Apply font to all elements */
    .stApp * {{
        font-family: {font_family};
    }}

    .stApp h1, .stApp h2, .stApp h3 {{
        font-family: {heading_font};
    }}

    /* Main container styling */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    /* Custom header styling */
    .custom-header {{
        background: linear-gradient(90deg, {accent_color} 0%, #FF6B6B 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }}

    /* Card styling */
    .feature-card {{
        background-color: {card_bg};
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid {card_border};
        margin: 1rem 0;
        color: {text_color};
    }}

    /* Metric card styling */
    .metric-card {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
    }}

    /* Success box */
    .success-box {{
        background-color: {"#1e3a2f" if theme != "Light" else "#d4edda"};
        border: 1px solid {"#2e5a4f" if theme != "Light" else "#c3e6cb"};
        padding: 1rem;
        border-radius: 5px;
        color: {"#8fdf9f" if theme != "Light" else "#155724"};
    }}

    /* Warning box */
    .warning-box {{
        background-color: {"#3d3a1e" if theme != "Light" else "#fff3cd"};
        border: 1px solid {"#5d5a2e" if theme != "Light" else "#ffeeba"};
        padding: 1rem;
        border-radius: 5px;
        color: {"#dfcf5f" if theme != "Light" else "#856404"};
    }}

    /* Info box */
    .info-box {{
        background-color: {"#1e2a3d" if theme != "Light" else "#cce5ff"};
        border: 1px solid {"#2e4a6d" if theme != "Light" else "#b8daff"};
        padding: 1rem;
        border-radius: 5px;
        color: {"#8fafdf" if theme != "Light" else "#004085"};
    }}

    /* Animated gradient text */
    .gradient-text {{
        background: linear-gradient(90deg, #FF4B4B, #FF6B6B, #FFD93D, #6BCB77);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 300% 300%;
        animation: gradient 3s ease infinite;
    }}

    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Sidebar styling */
    section[data-testid="stSidebar"] {{
        background-color: {secondary_bg};
    }}

    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {{
        color: {text_color} !important;
    }}

    /* Button hover effects */
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }}

    /* Code block styling */
    .code-block {{
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Consolas', monospace;
        overflow-x: auto;
    }}

    /* Table styling */
    .styled-table {{
        border-collapse: collapse;
        width: 100%;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    }}

    .styled-table th {{
        background-color: {accent_color};
        color: white;
        padding: 12px 15px;
    }}

    .styled-table td {{
        padding: 12px 15px;
        border-bottom: 1px solid {"#444" if theme != "Light" else "#dddddd"};
        color: {text_color};
    }}

    .styled-table tr:nth-child(even) {{
        background-color: {secondary_bg};
    }}

    /* DataFrame styling */
    .stDataFrame {{
        background-color: {secondary_bg};
    }}

    /* Expander styling */
    .streamlit-expanderHeader {{
        background-color: {secondary_bg};
        color: {text_color} !important;
    }}

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: {secondary_bg};
    }}

    .stTabs [data-baseweb="tab"] {{
        color: {text_color};
    }}
</style>
""",
    unsafe_allow_html=True,
)

# =============================================================================
# PAGE ROUTING
# =============================================================================
if page == "🏠 Home":
    home.render(show_code)

elif page == "📝 Text & Markdown":
    text_markdown.render(show_code)

elif page == "📊 Data Display":
    data_display.render(show_code)

elif page == "📈 Charts & Visualizations":
    charts.render(show_code)

elif page == "🎛️ Input Widgets":
    input_widgets.render(show_code)

elif page == "📐 Layout & Containers":
    layout_containers.render(show_code)

elif page == "🎨 Styling & Theming":
    styling_theming.render(show_code, theme)

elif page == "✨ CSS Showcase":
    css_showcase.render(show_code)

elif page == "⚡ Advanced Features":
    advanced_features.render(show_code)

elif page == "🔧 Utilities":
    utilities.render(show_code)

# =============================================================================
# FOOTER
# =============================================================================
st.divider()
st.markdown(
    """
<div style="text-align: center; padding: 1rem; color: #888;">
    <p>Built with ❤️ using Streamlit</p>
    <p>Explore more at <a href="https://docs.streamlit.io">docs.streamlit.io</a></p>
</div>
""",
    unsafe_allow_html=True,
)

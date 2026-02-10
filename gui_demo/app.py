"""
Streamlit Feature Demo Application
===================================
A comprehensive showcase of Streamlit's features and functionalities.
"""

import streamlit as st
from datetime import datetime
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
    embedding,
    resources,
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
            "🔗 Embedding",
            "📚 Resources",
        ],
        index=0,
    )

    st.divider()
    st.caption("Built with Streamlit 🎈")
    st.caption(f"Current time: {datetime.now().strftime('%H:%M:%S')}")

# =============================================================================
# PAGE ROUTING
# =============================================================================
if page == "🏠 Home":
    home.render()

elif page == "📝 Text & Markdown":
    text_markdown.render()

elif page == "📊 Data Display":
    data_display.render()

elif page == "📈 Charts & Visualizations":
    charts.render()

elif page == "🎛️ Input Widgets":
    input_widgets.render()

elif page == "📐 Layout & Containers":
    layout_containers.render()

elif page == "🎨 Styling & Theming":
    styling_theming.render()

elif page == "✨ CSS Showcase":
    css_showcase.render()

elif page == "⚡ Advanced Features":
    advanced_features.render()

elif page == "🔧 Utilities":
    utilities.render()

elif page == "🔗 Embedding":
    embedding.render()

elif page == "📚 Resources":
    resources.render()

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

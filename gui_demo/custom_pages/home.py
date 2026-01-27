"""Home page module."""

import streamlit as st


def render():
    """Render the home page."""
    st.markdown(
        '<div class="custom-header"><h1>🚀 Streamlit Feature Demo</h1>'
        "<p>Explore all the amazing features of Streamlit!</p></div>",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Features", value="50+", delta="Growing")
    with col2:
        st.metric(label="Widgets", value="30+", delta="5 new")
    with col3:
        st.metric(label="Charts", value="10+", delta="Interactive")
    with col4:
        st.metric(label="Layouts", value="8+", delta="Flexible")

    st.divider()

    st.subheader("Welcome to the Streamlit Feature Demo!")

    st.markdown(
        """
    This application demonstrates the full range of Streamlit's capabilities:

    - **📝 Text & Markdown**: Headers, text, markdown, code blocks, and more
    - **📊 Data Display**: DataFrames, tables, metrics, and JSON
    - **📈 Charts & Visualizations**: Plotly, Altair, Matplotlib, and native charts
    - **🎛️ Input Widgets**: Buttons, sliders, text inputs, file uploaders, and more
    - **📐 Layout & Containers**: Columns, tabs, expanders, and containers
    - **🎨 Styling & Theming**: Custom CSS, themes, and visual customization
    - **✨ CSS Showcase**: Advanced CSS effects and animations
    - **⚡ Advanced Features**: Session state, caching, forms, and callbacks
    - **🔧 Utilities**: Progress bars, spinners, balloons, and more

    Use the sidebar to navigate between different feature categories!
    """
    )

"""Styling & Theming page module."""
import streamlit as st
import pandas as pd


def render():
    """Render the Styling & Theming page."""
    st.header("🎨 Styling & Theming")

    tab1, tab2, tab3 = st.tabs(["Custom CSS", "Markdown Styling", "Component Styling"])

    with tab1:
        st.subheader("Custom CSS Examples")

        st.markdown("""
        <div class="feature-card">
            <h3>🎨 Feature Card</h3>
            <p>This card uses custom CSS with a colored border and background.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="success-box">
                <strong>Success!</strong><br>
                Operation completed successfully.
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="warning-box">
                <strong>Warning!</strong><br>
                Please review before proceeding.
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="info-box">
                <strong>Info</strong><br>
                Here's some useful information.
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.subheader("Gradient Text Animation")
        st.markdown('<h2 class="gradient-text">Animated Gradient Text Effect!</h2>', unsafe_allow_html=True)

        st.divider()

    with tab2:
        st.subheader("Markdown with HTML Styling")

        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin: 1rem 0;
        ">
            <h2 style="margin: 0;">Welcome to Streamlit</h2>
            <p style="margin: 0.5rem 0 0 0;">Build beautiful data apps in minutes!</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown("""
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <div style="
                flex: 1;
                min-width: 200px;
                background: #FF6B6B;
                padding: 1rem;
                border-radius: 10px;
                color: white;
                text-align: center;
            ">
                <h3>🚀 Fast</h3>
                <p>Quick development</p>
            </div>
            <div style="
                flex: 1;
                min-width: 200px;
                background: #4ECDC4;
                padding: 1rem;
                border-radius: 10px;
                color: white;
                text-align: center;
            ">
                <h3>🎨 Beautiful</h3>
                <p>Stunning visuals</p>
            </div>
            <div style="
                flex: 1;
                min-width: 200px;
                background: #45B7D1;
                padding: 1rem;
                border-radius: 10px;
                color: white;
                text-align: center;
            ">
                <h3>⚡ Powerful</h3>
                <p>Rich features</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.subheader("Styled DataFrame")

        df = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'D'],
            'Sales': [100, 200, 150, 300],
            'Growth': [0.1, -0.05, 0.2, 0.15]
        })

        def highlight_max(s):
            is_max = s == s.max()
            return ['background-color: lightgreen' if v else '' for v in is_max]

        styled = df.style\
            .apply(highlight_max, subset=['Sales'])\
            .format({'Growth': '{:.1%}', 'Sales': '${:,.0f}'})

        st.dataframe(styled, use_container_width=True)

        st.divider()

        st.subheader("Custom Column Configuration")

        products_df = pd.DataFrame({
            'Product': ['Widget A', 'Widget B', 'Widget C'],
            'Price': [19.99, 29.99, 39.99],
            'Rating': [4.5, 3.8, 4.9],
            'In Stock': [True, False, True],
            'Image': [
                'https://placekitten.com/50/50',
                'https://placekitten.com/51/50',
                'https://placekitten.com/52/50'
            ]
        })

        st.dataframe(
            products_df,
            column_config={
                'Product': st.column_config.TextColumn('Product Name', width='medium'),
                'Price': st.column_config.NumberColumn('Price', format='$%.2f'),
                'Rating': st.column_config.ProgressColumn('Rating', min_value=0, max_value=5, format='%.1f'),
                'In Stock': st.column_config.CheckboxColumn('Available'),
                'Image': st.column_config.ImageColumn('Preview', width='small')
            },
            hide_index=True,
            use_container_width=True
        )

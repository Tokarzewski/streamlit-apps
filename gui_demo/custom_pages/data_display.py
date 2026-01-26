"""Data Display page module."""

import streamlit as st
import pandas as pd


def render(show_code: bool = False):
    """Render the Data Display page."""
    st.header("📊 Data Display Elements")

    # Sample data
    df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "Age": [25, 30, 35, 28, 32],
            "City": ["New York", "London", "Paris", "Tokyo", "Sydney"],
            "Salary": [50000, 60000, 75000, 55000, 80000],
            "Rating": [4.5, 3.8, 4.2, 4.8, 4.0],
        }
    )

    tab1, tab2, tab3, tab4 = st.tabs(["DataFrames", "Metrics", "JSON", "Data Editor"])

    with tab1:
        st.subheader("st.dataframe() - Interactive DataFrame")
        st.dataframe(
            df,
            column_config={
                "Name": st.column_config.TextColumn("Employee Name", width="medium"),
                "Salary": st.column_config.NumberColumn("Salary ($)", format="$%d"),
                "Rating": st.column_config.ProgressColumn(
                    "Rating", min_value=0, max_value=5
                ),
            },
            hide_index=True,
            use_container_width=True,
        )

        st.divider()

        st.subheader("st.table() - Static Table")
        st.table(df.head(3))

        st.divider()

        st.subheader("Styled DataFrame")
        styled_df = df.style.highlight_max(
            subset=["Salary", "Rating"], color="lightgreen"
        )
        st.dataframe(styled_df)

        if show_code:
            with st.expander("View Code"):
                st.code(
                    """
                # Interactive DataFrame with column config
                st.dataframe(
                    df,
                    column_config={
                        "Name": st.column_config.TextColumn("Employee Name"),
                        "Salary": st.column_config.NumberColumn("Salary ($)", format="$%d"),
                        "Rating": st.column_config.ProgressColumn("Rating", min_value=0, max_value=5)
                    },
                    hide_index=True
                )

                # Static table
                st.table(df.head(3))

                # Styled DataFrame
                styled_df = df.style.highlight_max(subset=['Salary'], color='lightgreen')
                st.dataframe(styled_df)
                """
                )

    with tab2:
        st.subheader("Metrics Display")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="Temperature", value="70°F", delta="1.2°F")
        with col2:
            st.metric(
                label="Revenue", value="$12,500", delta="-$500", delta_color="inverse"
            )
        with col3:
            st.metric(label="Users", value="1,234", delta="12%", delta_color="normal")

        st.divider()

        st.subheader("Custom Metric Cards")
        col1, col2, col3, col4 = st.columns(4)

        metrics = [
            ("Total Sales", "$45,231", "📈"),
            ("Active Users", "2,345", "👥"),
            ("Conversion", "3.2%", "🎯"),
            ("Avg. Order", "$127", "🛒"),
        ]

        for col, (label, value, icon) in zip([col1, col2, col3, col4], metrics):
            with col:
                st.markdown(
                    f"""
                <div class="metric-card">
                    <h3>{icon}</h3>
                    <h2>{value}</h2>
                    <p>{label}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        if show_code:
            with st.expander("View Code"):
                st.code(
                    """
                # Basic metrics with delta
                st.metric(label="Temperature", value="70°F", delta="1.2°F")
                st.metric(label="Revenue", value="$12,500", delta="-$500", delta_color="inverse")

                # Custom metric cards with HTML/CSS
                st.markdown('''
                <div class="metric-card">
                    <h3>📈</h3>
                    <h2>$45,231</h2>
                    <p>Total Sales</p>
                </div>
                ''', unsafe_allow_html=True)
                """
                )

    with tab3:
        st.subheader("JSON Display")

        json_data = {
            "name": "Streamlit Demo",
            "version": "1.0.0",
            "features": ["charts", "widgets", "styling"],
            "settings": {"theme": "light", "sidebar": True, "wide_mode": True},
        }

        st.json(json_data)

    with tab4:
        st.subheader("st.data_editor() - Editable DataFrame")

        edited_df = st.data_editor(
            df,
            column_config={
                "Name": st.column_config.TextColumn("Employee Name"),
                "Age": st.column_config.NumberColumn(
                    "Age", min_value=18, max_value=100
                ),
                "Rating": st.column_config.SelectboxColumn(
                    "Rating", options=[1, 2, 3, 4, 5]
                ),
            },
            num_rows="dynamic",
            use_container_width=True,
        )

        if st.button("Show Edited Data"):
            st.write("Edited DataFrame:")
            st.dataframe(edited_df)

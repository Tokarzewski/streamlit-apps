"""Charts & Visualizations page module."""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import matplotlib.pyplot as plt


def render():
    """Render the Charts & Visualizations page."""
    st.header("📈 Charts & Visualizations")

    # Generate sample data
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=30, freq="D")
    chart_data = pd.DataFrame(
        {
            "date": dates,
            "sales": np.random.randint(100, 500, 30),
            "revenue": np.random.randint(1000, 5000, 30),
            "visitors": np.random.randint(200, 1000, 30),
        }
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Native Charts", "Plotly", "Altair", "Matplotlib"]
    )

    with tab1:
        st.subheader("Streamlit Native Charts")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Line Chart**")
            st.line_chart(chart_data.set_index("date")[["sales", "revenue"]])

        with col2:
            st.write("**Area Chart**")
            st.area_chart(chart_data.set_index("date")[["sales", "visitors"]])

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Bar Chart**")
            st.bar_chart(chart_data.set_index("date")["sales"].head(10))

        with col2:
            st.write("**Scatter Chart**")
            scatter_df = pd.DataFrame(
                {
                    "x": np.random.randn(100),
                    "y": np.random.randn(100),
                    "size": np.random.randint(10, 100, 100),
                }
            )
            st.scatter_chart(scatter_df, x="x", y="y", size="size")

    with tab2:
        st.subheader("Plotly Charts")

        col1, col2 = st.columns(2)

        with col1:
            # Line chart
            fig = px.line(
                chart_data,
                x="date",
                y=["sales", "revenue"],
                title="Sales & Revenue Over Time",
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

            # Pie chart
            pie_data = pd.DataFrame(
                {"Category": ["A", "B", "C", "D"], "Values": [30, 25, 25, 20]}
            )
            fig = px.pie(
                pie_data, values="Values", names="Category", title="Distribution"
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Bar chart
            fig = px.bar(
                chart_data.head(10),
                x="date",
                y="sales",
                title="Daily Sales",
                color="sales",
                color_continuous_scale="Viridis",
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

            # Scatter plot
            fig = px.scatter(
                chart_data,
                x="sales",
                y="revenue",
                size="visitors",
                color="visitors",
                title="Sales vs Revenue",
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # 3D Chart
        st.write("**3D Surface Plot**")
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))

        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
        fig.update_layout(title="3D Surface Plot", height=500)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Altair Charts")

        col1, col2 = st.columns(2)

        with col1:
            # Interactive scatter plot
            scatter = (
                alt.Chart(chart_data)
                .mark_circle(size=60)
                .encode(
                    x="sales:Q",
                    y="revenue:Q",
                    color="visitors:Q",
                    tooltip=["date", "sales", "revenue", "visitors"],
                )
                .properties(title="Interactive Scatter Plot", height=350)
                .interactive()
            )
            st.altair_chart(scatter, use_container_width=True)

        with col2:
            # Bar chart
            bars = (
                alt.Chart(chart_data.head(10))
                .mark_bar()
                .encode(
                    x=alt.X("date:T", title="Date"),
                    y=alt.Y("sales:Q", title="Sales"),
                    color=alt.Color("sales:Q", scale=alt.Scale(scheme="viridis")),
                )
                .properties(title="Sales by Date", height=350)
            )
            st.altair_chart(bars, use_container_width=True)

        # Layered chart
        st.write("**Layered Chart with Tooltip**")
        base = alt.Chart(chart_data).encode(x="date:T")

        line = base.mark_line(color="blue").encode(y="sales:Q")
        points = base.mark_circle(color="red", size=50).encode(
            y="sales:Q", tooltip=["date:T", "sales:Q", "revenue:Q"]
        )

        layered = (line + points).properties(
            height=300, title="Sales Trend with Data Points"
        )
        st.altair_chart(layered, use_container_width=True)

    with tab4:
        st.subheader("Matplotlib Charts")

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(chart_data["date"], chart_data["sales"], label="Sales", marker="o")
            ax.plot(
                chart_data["date"], chart_data["visitors"], label="Visitors", marker="s"
            )
            ax.set_xlabel("Date")
            ax.set_ylabel("Value")
            ax.set_title("Sales and Visitors Over Time")
            ax.legend()
            ax.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots(figsize=(8, 6))
            categories = ["A", "B", "C", "D", "E"]
            values = [23, 45, 56, 78, 32]
            ax.bar(categories, values)
            ax.set_xlabel("Category")
            ax.set_ylabel("Value")
            ax.set_title("Bar Chart Example")
            st.pyplot(fig)

        # Subplot example
        st.write("**Matplotlib Subplots**")
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))

        # Histogram
        axes[0].hist(np.random.randn(1000), bins=30, color="skyblue", edgecolor="black")
        axes[0].set_title("Histogram")

        # Box plot
        axes[1].boxplot([np.random.randn(100) for _ in range(4)])
        axes[1].set_title("Box Plot")

        # Heatmap
        heatmap_data = np.random.rand(10, 10)
        im = axes[2].imshow(heatmap_data, cmap="YlOrRd")
        axes[2].set_title("Heatmap")
        plt.colorbar(im, ax=axes[2])

        plt.tight_layout()
        st.pyplot(fig)

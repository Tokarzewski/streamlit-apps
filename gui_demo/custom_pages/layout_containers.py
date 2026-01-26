"""Layout & Containers page module."""

import streamlit as st
import pandas as pd
import numpy as np


def render(show_code: bool = False):
    """Render the Layout & Containers page."""
    st.header("📐 Layout & Containers")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Columns", "Tabs & Expanders", "Containers", "Popups & Dialogs"]
    )

    with tab1:
        st.subheader("Columns")

        # Equal columns
        st.write("**Equal Width Columns**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("Column 1")
        with col2:
            st.warning("Column 2")
        with col3:
            st.success("Column 3")

        st.divider()

        # Unequal columns
        st.write("**Custom Width Columns (1:2:1)**")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.write("Narrow")
        with col2:
            st.write("Wide column - twice the width of the others")
        with col3:
            st.write("Narrow")

        st.divider()

        # Nested columns
        st.write("**Nested Columns**")
        outer_col1, outer_col2 = st.columns(2)

        with outer_col1:
            st.write("Outer Column 1")
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.metric("Metric A", "100")
            with inner_col2:
                st.metric("Metric B", "200")

        with outer_col2:
            st.write("Outer Column 2")
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.metric("Metric C", "300")
            with inner_col2:
                st.metric("Metric D", "400")

        if show_code:
            with st.expander("View Code"):
                st.code(
                    """
# Equal columns
col1, col2, col3 = st.columns(3)

# Custom width columns (ratio 1:2:1)
col1, col2, col3 = st.columns([1, 2, 1])

# Nested columns
outer1, outer2 = st.columns(2)
with outer1:
    inner1, inner2 = st.columns(2)
    with inner1:
        st.metric("A", "100")
                """
                )

    with tab2:
        st.subheader("Tabs")

        inner_tab1, inner_tab2, inner_tab3 = st.tabs(
            ["📊 Data", "📈 Chart", "⚙️ Settings"]
        )

        with inner_tab1:
            st.write("This is the Data tab content")
            st.dataframe(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}))

        with inner_tab2:
            st.write("This is the Chart tab content")
            st.line_chart(np.random.randn(20, 3))

        with inner_tab3:
            st.write("This is the Settings tab content")
            st.checkbox("Option 1")
            st.checkbox("Option 2")

        st.divider()

        st.subheader("Expanders")

        with st.expander("Click to expand - Section 1"):
            st.write("This content is hidden until you expand it!")
            st.image("https://placekitten.com/400/200", caption="A cute kitten")

        with st.expander("Click to expand - Section 2", expanded=True):
            st.write("This expander starts expanded!")
            st.code("print('Hello from inside an expander!')")

        if show_code:
            with st.expander("View Code"):
                st.code(
                    """
# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Data", "📈 Chart", "⚙️ Settings"])
with tab1:
    st.write("Tab 1 content")

# Expanders
with st.expander("Click to expand"):
    st.write("Hidden content")

with st.expander("Starts expanded", expanded=True):
    st.write("Visible by default")
                """
                )

    with tab3:
        st.subheader("Container")

        with st.container():
            st.write("This is inside a container")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Left side")
            with col2:
                st.write("Right side")

        st.divider()

        st.subheader("Container with Border")

        with st.container(border=True):
            st.write("🎯 This container has a border!")
            st.write("It helps visually group related content.")
            st.button("Action Button", key="container_btn")

        st.divider()

        st.subheader("Empty Container (for dynamic content)")

        placeholder = st.empty()

        if st.button("Update Placeholder"):
            placeholder.success("Content updated dynamically!")
        else:
            placeholder.info("Click the button to update this placeholder")

        if show_code:
            with st.expander("View Code"):
                st.code(
                    """
# Basic container
with st.container():
    st.write("Grouped content")

# Container with border
with st.container(border=True):
    st.write("Bordered content")

# Empty placeholder for dynamic content
placeholder = st.empty()
placeholder.info("Initial content")
# Later: placeholder.success("Updated!")
                """
                )

    with tab4:
        st.subheader("Popover")

        with st.popover("Open popover"):
            st.write("This is inside a popover!")
            st.text_input("Enter something:", key="popover_input")
            if st.button("Submit", key="popover_btn"):
                st.success("Submitted!")

        st.divider()

        st.subheader("Status Elements")

        col1, col2 = st.columns(2)

        with col1:
            st.success("This is a success message")
            st.info("This is an info message")

        with col2:
            st.warning("This is a warning message")
            st.error("This is an error message")

        st.exception(Exception("This is an exception display"))

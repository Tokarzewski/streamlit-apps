"""Input Widgets page module."""

import streamlit as st
import pandas as pd
from datetime import date, time as dt_time, datetime


def render():
    """Render the Input Widgets page."""
    st.header("🎛️ Input Widgets")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Buttons & Selection", "Sliders & Inputs", "Date & Time", "File & Media"]
    )

    with tab1:
        st.subheader("Buttons")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Primary Button", type="primary"):
                st.success("Primary clicked!")

        with col2:
            if st.button("Secondary Button"):
                st.info("Secondary clicked!")

        with col3:
            if st.button("🎈 Emoji Button"):
                st.balloons()

        st.divider()

        st.subheader("Selection Widgets")

        col1, col2 = st.columns(2)

        with col1:
            # Checkbox
            agree = st.checkbox("I agree to the terms")
            if agree:
                st.success("Thank you for agreeing!")

            # Toggle
            on = st.toggle("Enable feature")
            st.write(f"Feature is {'ON' if on else 'OFF'}")

            # Radio
            genre = st.radio(
                "What's your favorite genre?",
                ["Comedy", "Drama", "Documentary"],
                horizontal=True,
            )
            st.write(f"You selected: {genre}")

        with col2:
            # Selectbox
            option = st.selectbox("Choose a color:", ["Red", "Green", "Blue", "Yellow"])
            st.write(f"Selected: {option}")

            # Multiselect
            options = st.multiselect(
                "Choose your favorite fruits:",
                ["Apple", "Banana", "Orange", "Mango", "Grape"],
                default=["Apple"],
            )
            st.write(f"You selected: {options}")

            # Select slider
            color = st.select_slider(
                "Select a color",
                options=[
                    "red",
                    "orange",
                    "yellow",
                    "green",
                    "blue",
                    "indigo",
                    "violet",
                ],
            )
            st.write(f"Selected color: {color}")

    with tab2:
        st.subheader("Sliders")

        col1, col2 = st.columns(2)

        with col1:
            # Basic slider
            age = st.slider("Select your age:", 0, 100, 25)
            st.write(f"Age: {age}")

            # Range slider
            values = st.slider("Select a range:", 0.0, 100.0, (25.0, 75.0))
            st.write(f"Range: {values}")

        with col2:
            # Float slider
            temperature = st.slider("Temperature (°C):", -10.0, 40.0, 20.0, 0.5)
            st.write(f"Temperature: {temperature}°C")

            # Slider with format
            salary = st.slider("Salary ($):", 30000, 150000, 50000, format="$%d")
            st.write(f"Salary: ${salary:,}")

        st.divider()

        st.subheader("Text Inputs")

        col1, col2 = st.columns(2)

        with col1:
            # Text input
            name = st.text_input("Enter your name:", placeholder="John Doe")
            if name:
                st.write(f"Hello, {name}!")

            # Password
            password = st.text_input("Enter password:", type="password")

            # Number input
            number = st.number_input(
                "Enter a number:", min_value=0, max_value=100, value=50, step=5
            )
            st.write(f"Number: {number}")

        with col2:
            # Text area
            message = st.text_area(
                "Enter your message:", height=100, placeholder="Type here..."
            )
            if message:
                st.write(f"Character count: {len(message)}")

            # Color picker
            color = st.color_picker("Pick a color:", "#FF4B4B")
            st.markdown(
                f'<div style="background-color: {color}; padding: 20px; border-radius: 10px;">'
                f"Selected Color: {color}</div>",
                unsafe_allow_html=True,
            )

    with tab3:
        st.subheader("Date & Time Inputs")

        col1, col2 = st.columns(2)

        with col1:
            # Date input
            d = st.date_input("Select a date:", date.today())
            st.write(f"Selected date: {d}")

            # Date range
            date_range = st.date_input(
                "Select date range:",
                (date(2024, 1, 1), date(2024, 12, 31)),
                format="MM/DD/YYYY",
            )
            st.write(f"Date range: {date_range}")

        with col2:
            # Time input
            t = st.time_input("Select a time:", dt_time(12, 0))
            st.write(f"Selected time: {t}")

            # Datetime display
            st.write(
                f"Current datetime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )

    with tab4:
        st.subheader("File Uploaders")

        col1, col2 = st.columns(2)

        with col1:
            # Single file
            uploaded_file = st.file_uploader(
                "Choose a file", type=["csv", "txt", "xlsx"]
            )
            if uploaded_file is not None:
                st.success(f"Uploaded: {uploaded_file.name}")
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                    st.dataframe(df.head())

        with col2:
            # Multiple files
            uploaded_files = st.file_uploader(
                "Choose multiple files",
                accept_multiple_files=True,
                type=["png", "jpg", "jpeg"],
            )
            for file in uploaded_files:
                st.write(f"Uploaded: {file.name}")

        st.divider()

        st.subheader("Camera Input")
        st.info("📷 Camera input is available for capturing photos directly!")

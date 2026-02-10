"""Advanced Features page module."""

import streamlit as st
import time
from datetime import date


def render():
    """Render the Advanced Features page."""
    st.header("⚡ Advanced Features")

    tab1, tab2, tab3, tab4 = st.tabs(["Session State", "Forms", "Caching", "Callbacks"])

    with tab1:
        _render_session_state()

    with tab2:
        _render_forms()

    with tab3:
        _render_caching()

    with tab4:
        _render_callbacks()


def _render_session_state():
    """Render session state tab."""
    st.subheader("Session State")

    # Initialize session state
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    if "cart_items" not in st.session_state:
        st.session_state.cart_items = []

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Counter Example**")
        st.write(f"Current count: {st.session_state.counter}")

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Increment"):
                st.session_state.counter += 1
                st.rerun()
        with c2:
            if st.button("Decrement"):
                st.session_state.counter -= 1
                st.rerun()
        with c3:
            if st.button("Reset"):
                st.session_state.counter = 0
                st.rerun()

    with col2:
        st.write("**Shopping Cart Example**")

        new_item = st.text_input("Add item:", key="new_item")
        if st.button("Add to Cart") and new_item:
            st.session_state.cart_items.append(new_item)
            st.rerun()

        st.write("Cart items:")
        for i, item in enumerate(st.session_state.cart_items):
            col_item, col_btn = st.columns([3, 1])
            with col_item:
                st.write(f"• {item}")
            with col_btn:
                if st.button("❌", key=f"remove_{i}"):
                    st.session_state.cart_items.pop(i)
                    st.rerun()

        if st.session_state.cart_items and st.button("Clear Cart"):
            st.session_state.cart_items = []
            st.rerun()


def _render_forms():
    """Render forms tab."""
    st.subheader("Forms")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Registration Form**")

        with st.form("registration_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            age = st.number_input("Age", min_value=18, max_value=100, value=25)
            country = st.selectbox(
                "Country", ["USA", "UK", "Canada", "Australia", "Other"]
            )
            interests = st.multiselect(
                "Interests", ["Sports", "Music", "Tech", "Art", "Travel"]
            )
            agree = st.checkbox("I agree to the terms and conditions")

            submitted = st.form_submit_button("Register", type="primary")

            if submitted:
                if name and email and agree:
                    st.success(f"Welcome, {name}! Registration successful.")
                    st.write(f"Email: {email}")
                    st.write(f"Age: {age}")
                    st.write(f"Country: {country}")
                    st.write(f"Interests: {', '.join(interests)}")
                else:
                    st.error("Please fill all required fields and agree to terms.")

    with col2:
        st.write("**Search Form**")

        with st.form("search_form", clear_on_submit=True):
            query = st.text_input("Search query")
            category = st.radio(
                "Category", ["All", "Products", "Users", "Orders"], horizontal=True
            )
            date_range = st.date_input("Date range", (date(2024, 1, 1), date.today()))

            search_clicked = st.form_submit_button("Search")

            if search_clicked:
                st.info(f"Searching for '{query}' in {category}...")


def _render_caching():
    """Render caching tab."""
    st.subheader("Caching")

    @st.cache_data
    def expensive_computation(n):
        """Simulates an expensive computation"""
        time.sleep(2)  # Simulate delay
        return [i**2 for i in range(n)]

    @st.cache_resource
    def load_model():
        """Simulates loading a large model"""
        time.sleep(1)
        return {"model": "loaded", "version": "1.0"}

    st.write("**@st.cache_data** - Cache data computations")

    n = st.slider("Compute squares up to n:", 10, 100, 50)

    if st.button("Run Computation"):
        start = time.time()
        result = expensive_computation(n)
        elapsed = time.time() - start
        st.write(f"First 10 results: {result[:10]}")
        st.write(f"Time elapsed: {elapsed:.2f}s")
        st.caption("Run again to see caching in action!")

    st.divider()

    st.write("**@st.cache_resource** - Cache resources (models, connections)")

    if st.button("Load Model"):
        model = load_model()
        st.json(model)


def _render_callbacks():
    """Render callbacks tab."""
    st.subheader("Callbacks")

    # Callback functions
    def on_change():
        st.session_state.callback_triggered = True

    def increment_callback():
        st.session_state.callback_counter = (
            st.session_state.get("callback_counter", 0) + 1
        )

    if "callback_counter" not in st.session_state:
        st.session_state.callback_counter = 0

    col1, col2 = st.columns(2)

    with col1:
        st.write("**on_change Callback**")

        st.text_input("Type something:", key="callback_input", on_change=on_change)

        if st.session_state.get("callback_triggered"):
            st.success("Callback was triggered!")
            st.session_state.callback_triggered = False

    with col2:
        st.write("**Button Callback**")

        st.write(f"Counter: {st.session_state.callback_counter}")

        st.button("Increment with Callback", on_click=increment_callback)

    st.divider()

    st.write("**Slider with Callback**")

    def slider_callback():
        st.session_state.slider_value_display = st.session_state.slider_with_callback

    st.slider(
        "Move the slider:",
        0,
        100,
        50,
        key="slider_with_callback",
        on_change=slider_callback,
    )

    if "slider_value_display" in st.session_state:
        st.write(f"Callback captured value: {st.session_state.slider_value_display}")

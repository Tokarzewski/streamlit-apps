"""Utilities page module."""

import streamlit as st
import time


def render(show_code: bool = False):
    """Render the Utilities page."""
    st.header("🔧 Utilities")

    tab1, tab2, tab3 = st.tabs(
        ["Progress & Status", "Messages & Alerts", "Fun Features"]
    )

    with tab1:
        _render_progress_status()

    with tab2:
        _render_messages_alerts()

    with tab3:
        _render_fun_features()


def _render_progress_status():
    """Render progress and status tab."""
    st.subheader("Progress Indicators")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Progress Bar**")

        if st.button("Start Progress"):
            progress_bar = st.progress(0)
            status_text = st.empty()

            for i in range(101):
                progress_bar.progress(i)
                status_text.text(f"Progress: {i}%")
                time.sleep(0.02)

            status_text.text("Complete!")
            st.success("Task finished!")

    with col2:
        st.write("**Spinner**")

        if st.button("Run with Spinner"):
            with st.spinner("Processing..."):
                time.sleep(2)
            st.success("Done!")

    st.divider()

    st.subheader("Status Containers")

    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        time.sleep(0.5)
        st.write("Found data source!")
        time.sleep(0.5)
        st.write("Downloading...")
        time.sleep(0.5)
        status.update(label="Download complete!", state="complete", expanded=False)


def _render_messages_alerts():
    """Render messages and alerts tab."""
    st.subheader("Message Types")

    col1, col2 = st.columns(2)

    with col1:
        st.success("This is a success message!")
        st.info("This is an info message!")
        st.warning("This is a warning message!")
        st.error("This is an error message!")

    with col2:
        st.toast("This is a toast notification!", icon="🍞")

        if st.button("Show Toast"):
            st.toast("Hello from a toast!", icon="👋")

        if st.button("Show Multiple Toasts"):
            st.toast("First toast", icon="1️⃣")
            time.sleep(0.5)
            st.toast("Second toast", icon="2️⃣")
            time.sleep(0.5)
            st.toast("Third toast", icon="3️⃣")

    st.divider()

    st.subheader("Exceptions")

    try:
        result = 1 / 0
    except Exception as e:
        st.exception(e)


def _render_fun_features():
    """Render fun features tab."""
    st.subheader("Fun Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Balloons**")
        if st.button("🎈 Release Balloons"):
            st.balloons()

    with col2:
        st.write("**Snow**")
        if st.button("❄️ Let it Snow"):
            st.snow()

    with col3:
        st.write("**Confetti Toast**")
        if st.button("🎉 Celebrate"):
            st.toast("Congratulations! 🎉", icon="🎊")

    st.divider()

    st.subheader("Echo & Help")

    with st.echo():
        # This code is displayed AND executed
        message = "Hello from st.echo!"
        st.write(message)

    st.divider()

    st.subheader("Stop Execution")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Trigger st.stop()"):
            st.write("About to stop...")
            st.stop()
            st.write("This will never be shown")

    with col2:
        st.write("st.stop() halts the app execution")

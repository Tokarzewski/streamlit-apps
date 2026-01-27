"""Embedding page module."""

import streamlit as st


def render():
    """Render the Embedding page."""
    st.header("🔗 Embedding Streamlit Apps")

    st.markdown(
        """
    Streamlit apps can be embedded into websites, blogs, and other platforms.
    This page explains the different ways to share and embed your Streamlit applications.
    """
    )

    tab1, tab2, tab3 = st.tabs(["iFrame Embedding", "Streamlit Cloud", "Embedding Options"])

    with tab1:
        st.subheader("Embedding with iFrames")

        st.markdown(
            """
        The most common way to embed a Streamlit app is using an HTML `<iframe>` element.
        This allows you to display your app within another webpage.
        """
        )

        st.markdown("**Basic iFrame Example:**")
        st.code(
            """
<iframe
    src="https://your-app.streamlit.app/?embedded=true"
    width="100%"
    height="600"
    frameborder="0"
></iframe>
            """,
            language="html",
        )

        st.divider()

        st.markdown("**Key Parameters:**")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            | Parameter | Description |
            |-----------|-------------|
            | `src` | URL of your Streamlit app |
            | `width` | Width of the embed (px or %) |
            | `height` | Height of the embed (px) |
            | `frameborder` | Border around iframe (0 = none) |
            """
            )

        with col2:
            st.markdown(
                """
            **URL Parameters:**
            - `?embedded=true` - Hides the toolbar and padding
            - `?embed_options=show_toolbar` - Shows minimal toolbar
            - `?embed_options=dark_theme` - Forces dark theme
            - `?embed_options=show_colored_line` - Shows top colored line
            """
            )

        st.divider()

        st.markdown("**Responsive iFrame Example:**")
        st.code(
            """
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe
        src="https://your-app.streamlit.app/?embedded=true"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        frameborder="0"
        allowfullscreen
    ></iframe>
</div>
            """,
            language="html",
        )

    with tab2:
        st.subheader("Streamlit Community Cloud")

        st.markdown(
            """
        **Streamlit Community Cloud** is the easiest way to deploy and share your Streamlit apps.
        It's free for public repositories and provides automatic deployment from GitHub.
        """
        )

        st.info("Deploy your app at: https://share.streamlit.io")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            **Deployment Steps:**

            1. Push your code to a GitHub repository
            2. Go to share.streamlit.io
            3. Connect your GitHub account
            4. Select your repository and branch
            5. Specify the main Python file
            6. Click "Deploy"
            """
            )

        with col2:
            st.markdown(
                """
            **Required Files:**

            - `app.py` (or your main script)
            - `requirements.txt` (Python dependencies)
            - Optional: `.streamlit/config.toml` (app config)
            - Optional: `packages.txt` (system packages)
            """
            )

        st.divider()

        st.markdown("**Example requirements.txt:**")
        st.code(
            """
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.15.0
            """,
            language="text",
        )

        st.markdown("**Example .streamlit/config.toml:**")
        st.code(
            """
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[server]
headless = true
port = 8501
            """,
            language="toml",
        )

    with tab3:
        st.subheader("Embedding Options & Best Practices")

        st.markdown("**Embed Query Parameters:**")

        params_data = [
            ("embedded=true", "Removes padding and hamburger menu"),
            ("embed_options=show_toolbar", "Shows a minimal toolbar"),
            ("embed_options=dark_theme", "Forces dark theme"),
            ("embed_options=light_theme", "Forces light theme"),
            ("embed_options=show_colored_line", "Shows the colored line at top"),
            ("embed_options=disable_scrolling", "Disables scrolling in iframe"),
        ]

        for param, desc in params_data:
            st.markdown(f"- `?{param}` - {desc}")

        st.divider()

        st.markdown("**Combining Multiple Options:**")
        st.code(
            """
https://your-app.streamlit.app/?embedded=true&embed_options=dark_theme&embed_options=show_toolbar
            """,
            language="text",
        )

        st.divider()

        st.subheader("Platform-Specific Embedding")

        with st.expander("Notion"):
            st.markdown(
                """
            1. Copy your Streamlit app URL
            2. In Notion, type `/embed`
            3. Paste the URL with `?embedded=true`
            4. Resize the embed as needed
            """
            )

        with st.expander("Medium / Substack"):
            st.markdown(
                """
            1. Use the embed or HTML block feature
            2. Paste the iframe code with your app URL
            3. Adjust width and height for readability
            """
            )

        with st.expander("WordPress"):
            st.markdown(
                """
            1. Add a "Custom HTML" block
            2. Paste the iframe code
            3. Or use a plugin like "iframe" for easier management
            """
            )

        with st.expander("GitHub README"):
            st.markdown(
                """
            GitHub doesn't support iframes in README files, but you can:
            1. Add a link to your deployed app
            2. Include a screenshot or GIF of your app
            3. Use a badge linking to the live demo
            """
            )
            st.code(
                """
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
                """,
                language="markdown",
            )

        st.divider()

        st.subheader("Security Considerations")

        st.warning(
            """
        **When embedding apps, consider:**
        - Embedded apps have access to browser storage
        - User inputs may contain sensitive data
        - Set appropriate CORS headers if needed
        - Consider authentication for sensitive apps
        """
        )

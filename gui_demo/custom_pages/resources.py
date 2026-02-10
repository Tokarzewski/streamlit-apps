"""Resources page module."""

import streamlit as st


def render():
    """Render the Resources page."""
    st.header("📚 Learning Resources")

    st.markdown(
        """
    Ready to master Streamlit? Here are the best resources to accelerate your learning journey.
    """
    )

    tab1, tab2, tab3 = st.tabs(["30 Days of Streamlit", "Documentation", "Community"])

    with tab1:
        st.subheader("30 Days of Streamlit")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(
                """
            **The #30DaysOfStreamlit** challenge is the best way to learn Streamlit from scratch!

            This free, self-paced learning program takes you from beginner to advanced in 30 days,
            with daily bite-sized lessons and hands-on coding exercises.
            """
            )

            st.success("**Start your journey today at: https://30days.streamlit.app/**")

            st.markdown(
                """
            **What You'll Learn:**

            **Week 1 - Fundamentals (Days 1-7)**
            - Setting up your Streamlit environment
            - Basic widgets: buttons, sliders, text inputs
            - Displaying text, data, and media
            - Layout basics with columns and containers

            **Week 2 - Intermediate (Days 8-14)**
            - Working with DataFrames and charts
            - File uploads and downloads
            - Session state management
            - Forms and user interactions

            **Week 3 - Advanced (Days 15-21)**
            - Custom components
            - Caching for performance
            - Multi-page apps
            - Theming and styling

            **Week 4 - Deployment & Beyond (Days 22-30)**
            - Deploying to Streamlit Cloud
            - Database connections
            - Authentication
            - Building real-world projects
            """
            )

        with col2:
            st.markdown(
                """
            <div style="
                background: linear-gradient(135deg, #FF4B4B 0%, #FF6B6B 100%);
                padding: 1.5rem;
                border-radius: 15px;
                color: white;
                text-align: center;
            ">
                <h2 style="margin: 0;">30 Days</h2>
                <p style="margin: 0.5rem 0;">of</p>
                <h2 style="margin: 0;">Streamlit</h2>
                <p style="margin-top: 1rem; font-size: 0.9rem;">Free Learning Challenge</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("")
            st.markdown("**Why this course?**")
            st.markdown("- Completely free")
            st.markdown("- Self-paced learning")
            st.markdown("- Hands-on projects")
            st.markdown("- Community support")
            st.markdown("- Certificate available")

        st.divider()

    with tab2:
        st.subheader("Official Documentation")

        st.markdown(
            """
        The official Streamlit documentation is comprehensive and well-maintained.
        It should be your primary reference for all things Streamlit.
        """
        )

        resources = [
            {
                "title": "Streamlit Documentation",
                "url": "https://docs.streamlit.io",
                "description": "Complete API reference, tutorials, and guides",
                "icon": "📖",
            },
            {
                "title": "API Reference",
                "url": "https://docs.streamlit.io/library/api-reference",
                "description": "Detailed documentation for every Streamlit function",
                "icon": "🔧",
            },
            {
                "title": "Streamlit Cheat Sheet",
                "url": "https://docs.streamlit.io/library/cheatsheet",
                "description": "Quick reference for common commands",
                "icon": "📋",
            },
            {
                "title": "App Gallery",
                "url": "https://streamlit.io/gallery",
                "description": "Browse apps built by the community for inspiration",
                "icon": "🖼️",
            },
            {
                "title": "Streamlit Components",
                "url": "https://streamlit.io/components",
                "description": "Extend Streamlit with custom components",
                "icon": "🧩",
            },
            {
                "title": "Deployment Guide",
                "url": "https://docs.streamlit.io/streamlit-community-cloud",
                "description": "Learn how to deploy your apps",
                "icon": "🚀",
            },
        ]

        col1, col2 = st.columns(2)

        for i, resource in enumerate(resources):
            with col1 if i % 2 == 0 else col2:
                st.markdown(
                    f"""
                <div style="
                    border: 1px solid #ddd;
                    border-radius: 10px;
                    padding: 1rem;
                    margin-bottom: 1rem;
                ">
                    <h4>{resource['icon']} {resource['title']}</h4>
                    <p style="color: #666; font-size: 0.9rem;">{resource['description']}</p>
                    <a href="{resource['url']}" target="_blank">{resource['url']}</a>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    with tab3:
        st.subheader("Community & Support")

        st.markdown(
            """
        The Streamlit community is welcoming and active. Here's where to connect:
        """
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            **Community Forum**

            The best place to ask questions and share your projects.

            https://discuss.streamlit.io
            """
            )

            st.markdown(
                """
            **GitHub Repository**

            Report bugs, request features, or contribute code.

            https://github.com/streamlit/streamlit
            """
            )

            st.markdown(
                """
            **Twitter/X**

            Follow for updates, tips, and community highlights.

            https://twitter.com/streamlit
            """
            )

        with col2:
            st.markdown(
                """
            **YouTube**

            Video tutorials and webinars.

            https://youtube.com/@streamlitofficial
            """
            )

            st.markdown(
                """
            **Blog**

            Articles, tutorials, and announcements.

            https://blog.streamlit.io
            """
            )

        st.divider()

        st.subheader("Tips for Learning")

        tips = [
            "Start with the 30 Days of Streamlit challenge for structured learning",
            "Build small projects to reinforce concepts",
            "Read the source code of apps in the Gallery",
            "Join the community forum and ask questions",
            "Contribute to open-source Streamlit projects",
            "Follow Streamlit creators on social media for tips",
        ]

        for i, tip in enumerate(tips, 1):
            st.markdown(f"**{i}.** {tip}")

        st.divider()

        st.info(
            """
        **Pro Tip:** The best way to learn is by building! Start with a simple project
        and gradually add features as you learn new concepts.
        """
        )

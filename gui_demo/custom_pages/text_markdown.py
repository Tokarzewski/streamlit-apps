"""Text & Markdown page module."""
import streamlit as st


def render(show_code: bool = False):
    """Render the Text & Markdown page."""
    st.header("📝 Text & Markdown Elements")

    tab1, tab2, tab3, tab4 = st.tabs(["Headers & Text", "Markdown", "Code", "Special Text"])

    with tab1:
        st.subheader("Headers")
        st.title("This is st.title()")
        st.header("This is st.header()")
        st.subheader("This is st.subheader()")
        st.caption("This is st.caption() - small text")

        if show_code:
            with st.expander("View Code"):
                st.code("""
                st.title("This is st.title()")
                st.header("This is st.header()")
                st.subheader("This is st.subheader()")
                st.caption("This is st.caption()")
                """)

        st.divider()

        st.subheader("Text Elements")
        st.text("This is st.text() - fixed-width text")
        st.write("This is st.write() - the Swiss Army knife of Streamlit!")

    with tab2:
        st.subheader("Markdown Support")

        st.markdown("""
        ### Markdown Features

        **Bold text** and *italic text* and ~~strikethrough~~

        > This is a blockquote

        - Bullet point 1
        - Bullet point 2
          - Nested bullet

        1. Numbered item 1
        2. Numbered item 2

        | Column 1 | Column 2 | Column 3 |
        |----------|----------|----------|
        | Data 1   | Data 2   | Data 3   |
        | Data 4   | Data 5   | Data 6   |

        [Link to Streamlit](https://streamlit.io)

        ---

        Inline `code` looks like this.
        """)

        st.markdown("### Colored Text with HTML")
        st.markdown(
            '<span style="color: red;">Red text</span>, '
            '<span style="color: blue;">Blue text</span>, '
            '<span style="color: green;">Green text</span>',
            unsafe_allow_html=True
        )

    with tab3:
        st.subheader("Code Display")

        st.code("""
        def hello_world():
            print("Hello, Streamlit!")
            return "🎈"
        """, language="python")

        st.code("""
        function greet(name) {
            console.log(`Hello, ${name}!`);
        }
        """, language="javascript")

        st.code("""
        SELECT * FROM users
        WHERE status = 'active'
        ORDER BY created_at DESC;
        """, language="sql")

    with tab4:
        st.subheader("Special Text Elements")

        st.latex(r"""
        \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
        """)

        st.latex(r"""
        E = mc^2
        """)

        st.divider()

        st.subheader("Echo Function")
        with st.echo():
            # This code will be displayed AND executed
            result = 2 + 2
            st.write(f"2 + 2 = {result}")

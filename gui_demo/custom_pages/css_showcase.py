"""CSS Showcase page module."""

import streamlit as st


def render(show_code: bool = False):
    """Render the CSS Showcase page."""
    st.header("✨ CSS Showcase")
    st.markdown("Explore advanced CSS effects and animations possible in Streamlit!")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Animations",
            "Glassmorphism",
            "Neon & Glow",
            "Cards & Hovers",
            "Advanced Effects",
        ]
    )

    with tab1:
        _render_animations()

    with tab2:
        _render_glassmorphism()

    with tab3:
        _render_neon_glow()

    with tab4:
        _render_cards_hovers()

    with tab5:
        _render_advanced_effects()

    if show_code:
        st.divider()
        with st.expander("View CSS Code Examples"):
            st.code(
                """
                /* Bouncing Animation */
                @keyframes bounce {
                    from { transform: translateY(0); }
                    to { transform: translateY(-30px); }
                }
                .bounce { animation: bounce 0.6s ease-in-out infinite alternate; }

                /* Glassmorphism */
                .glass {
                    background: rgba(255, 255, 255, 0.15);
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 16px;
                }

                /* Neon Glow */
                .neon {
                    text-shadow: 0 0 10px #fff, 0 0 40px #ff00de;
                }

                /* 3D Flip Card */
                .flip-card { transform-style: preserve-3d; transition: transform 0.8s; }
                .flip-card:hover { transform: rotateY(180deg); }

                /* Morphing Shape */
                @keyframes morph {
                    0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
                    50% { border-radius: 50% 60% 30% 60% / 30% 60% 70% 40%; }
                }

                /* Neumorphism */
                .neumorphic {
                    box-shadow: 9px 9px 16px #b8bec7, -9px -9px 16px #ffffff;
                }
            """,
                language="css",
            )


def _render_animations():
    """Render animations tab."""
    st.subheader("CSS Animations")

    # Bouncing balls
    st.markdown("**Bouncing Animation**")
    st.markdown(
        """
    <style>
    .bounce-container {
        display: flex;
        gap: 10px;
        padding: 20px;
        justify-content: center;
    }
    .bounce-ball {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        animation: bounce 0.6s ease-in-out infinite alternate;
    }
    .bounce-ball:nth-child(1) { background: #FF4B4B; animation-delay: 0s; }
    .bounce-ball:nth-child(2) { background: #FFD93D; animation-delay: 0.1s; }
    .bounce-ball:nth-child(3) { background: #6BCB77; animation-delay: 0.2s; }
    .bounce-ball:nth-child(4) { background: #4D96FF; animation-delay: 0.3s; }
    .bounce-ball:nth-child(5) { background: #9B59B6; animation-delay: 0.4s; }
    @keyframes bounce {
        from { transform: translateY(0); }
        to { transform: translateY(-30px); }
    }
    </style>
    <div class="bounce-container">
        <div class="bounce-ball"></div>
        <div class="bounce-ball"></div>
        <div class="bounce-ball"></div>
        <div class="bounce-ball"></div>
        <div class="bounce-ball"></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Spinning loader
    st.markdown("**Spinning Loaders**")
    st.markdown(
        """
    <style>
    .loader-container {
        display: flex;
        gap: 40px;
        padding: 30px;
        justify-content: center;
        align-items: center;
    }
    .spinner {
        width: 50px;
        height: 50px;
        border: 4px solid rgba(255, 75, 75, 0.2);
        border-top-color: #FF4B4B;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    .double-spinner {
        width: 50px;
        height: 50px;
        border: 4px solid transparent;
        border-top-color: #4D96FF;
        border-bottom-color: #4D96FF;
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
    }
    .pulse-ring {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #6BCB77;
        animation: pulse-ring 1.5s ease-out infinite;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    @keyframes pulse-ring {
        0% { transform: scale(0.5); opacity: 1; }
        100% { transform: scale(1.5); opacity: 0; }
    }
    </style>
    <div class="loader-container">
        <div class="spinner"></div>
        <div class="double-spinner"></div>
        <div class="pulse-ring"></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Typewriter effect
    st.markdown("**Typewriter Effect**")
    st.markdown(
        """
    <style>
    .typewriter {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.5rem;
        color: #FF4B4B;
        overflow: hidden;
        border-right: 3px solid #FF4B4B;
        white-space: nowrap;
        animation: typing 3s steps(30) infinite, blink 0.5s step-end infinite alternate;
        width: fit-content;
        margin: 20px auto;
    }
    @keyframes typing {
        0%, 90%, 100% { width: 0; }
        30%, 60% { width: 100%; }
    }
    @keyframes blink {
        50% { border-color: transparent; }
    }
    </style>
    <div class="typewriter">Welcome to Streamlit CSS Showcase!</div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Wave animation
    st.markdown("**Wave Animation**")
    st.markdown(
        """
    <style>
    .wave-container {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        height: 80px;
        gap: 5px;
        padding: 20px;
    }
    .wave-bar {
        width: 8px;
        background: linear-gradient(180deg, #FF4B4B, #FFD93D);
        border-radius: 4px;
        animation: wave 1s ease-in-out infinite;
    }
    .wave-bar:nth-child(1) { animation-delay: 0s; height: 20px; }
    .wave-bar:nth-child(2) { animation-delay: 0.1s; height: 30px; }
    .wave-bar:nth-child(3) { animation-delay: 0.2s; height: 40px; }
    .wave-bar:nth-child(4) { animation-delay: 0.3s; height: 50px; }
    .wave-bar:nth-child(5) { animation-delay: 0.4s; height: 40px; }
    .wave-bar:nth-child(6) { animation-delay: 0.5s; height: 30px; }
    .wave-bar:nth-child(7) { animation-delay: 0.6s; height: 20px; }
    @keyframes wave {
        0%, 100% { transform: scaleY(1); }
        50% { transform: scaleY(1.8); }
    }
    </style>
    <div class="wave-container">
        <div class="wave-bar"></div>
        <div class="wave-bar"></div>
        <div class="wave-bar"></div>
        <div class="wave-bar"></div>
        <div class="wave-bar"></div>
        <div class="wave-bar"></div>
        <div class="wave-bar"></div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def _render_glassmorphism():
    """Render glassmorphism tab."""
    st.subheader("Glassmorphism Effects")

    st.markdown(
        """
    <style>
    .glass-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 40px;
        border-radius: 20px;
        position: relative;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        padding: 30px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    .glass-card h3 {
        margin: 0 0 10px 0;
        font-size: 1.5rem;
    }
    .glass-card p {
        margin: 0;
        opacity: 0.9;
    }
    </style>
    <div class="glass-bg">
        <div class="glass-card">
            <h3>🌟 Glassmorphism</h3>
            <p>Beautiful frosted glass effect with blur and transparency</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Glass Cards Grid**")
    st.markdown(
        """
    <style>
    .glass-grid-bg {
        background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59);
        padding: 30px;
        border-radius: 20px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
    .glass-item {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 20px;
        color: white;
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .glass-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    .glass-item .icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }
    </style>
    <div class="glass-grid-bg">
        <div class="glass-item">
            <div class="icon">🚀</div>
            <strong>Fast</strong>
        </div>
        <div class="glass-item">
            <div class="icon">🎨</div>
            <strong>Beautiful</strong>
        </div>
        <div class="glass-item">
            <div class="icon">⚡</div>
            <strong>Powerful</strong>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Floating Glass Panel**")
    st.markdown(
        """
    <style>
    .float-bg {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 50px 30px;
        border-radius: 20px;
        display: flex;
        justify-content: center;
    }
    .float-glass {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px 60px;
        color: #eaeaea;
        text-align: center;
        animation: float 3s ease-in-out infinite;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    </style>
    <div class="float-bg">
        <div class="float-glass">
            <h2 style="margin:0; color: #e94560;">Floating Panel</h2>
            <p style="margin: 10px 0 0 0; opacity: 0.8;">Hover in the air with smooth animation</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def _render_neon_glow():
    """Render neon and glow effects tab."""
    st.subheader("Neon & Glow Effects")

    st.markdown("**Neon Text**")
    st.markdown(
        """
    <style>
    .neon-container {
        background: #0a0a0a;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
    }
    .neon-text {
        font-size: 3rem;
        font-weight: bold;
        color: #fff;
        text-shadow:
            0 0 5px #fff,
            0 0 10px #fff,
            0 0 20px #ff00de,
            0 0 40px #ff00de,
            0 0 80px #ff00de;
        animation: neon-flicker 1.5s infinite alternate;
    }
    @keyframes neon-flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
            text-shadow:
                0 0 5px #fff,
                0 0 10px #fff,
                0 0 20px #ff00de,
                0 0 40px #ff00de,
                0 0 80px #ff00de;
        }
        20%, 24%, 55% {
            text-shadow: none;
        }
    }
    </style>
    <div class="neon-container">
        <span class="neon-text">NEON</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Glowing Buttons**")
    st.markdown(
        """
    <style>
    .glow-btn-container {
        background: #1a1a2e;
        padding: 30px;
        border-radius: 15px;
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    .glow-btn {
        padding: 15px 40px;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .glow-btn-red {
        background: #ff4757;
        color: white;
        box-shadow: 0 0 20px #ff4757;
    }
    .glow-btn-red:hover {
        box-shadow: 0 0 40px #ff4757, 0 0 80px #ff4757;
        transform: scale(1.05);
    }
    .glow-btn-cyan {
        background: #00d2d3;
        color: #1a1a2e;
        box-shadow: 0 0 20px #00d2d3;
    }
    .glow-btn-cyan:hover {
        box-shadow: 0 0 40px #00d2d3, 0 0 80px #00d2d3;
        transform: scale(1.05);
    }
    .glow-btn-purple {
        background: #a55eea;
        color: white;
        box-shadow: 0 0 20px #a55eea;
    }
    .glow-btn-purple:hover {
        box-shadow: 0 0 40px #a55eea, 0 0 80px #a55eea;
        transform: scale(1.05);
    }
    </style>
    <div class="glow-btn-container">
        <button class="glow-btn glow-btn-red">Danger</button>
        <button class="glow-btn glow-btn-cyan">Cyber</button>
        <button class="glow-btn glow-btn-purple">Magic</button>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Neon Border Cards**")
    st.markdown(
        """
    <style>
    .neon-cards {
        background: #0f0f0f;
        padding: 30px;
        border-radius: 15px;
        display: flex;
        gap: 20px;
        justify-content: center;
    }
    .neon-card {
        width: 150px;
        height: 150px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        position: relative;
        background: #1a1a1a;
        overflow: hidden;
    }
    .neon-card::before {
        content: '';
        position: absolute;
        inset: -3px;
        border-radius: 18px;
        padding: 3px;
        background: linear-gradient(45deg, #ff0080, #ff8c00, #40e0d0, #ff0080);
        background-size: 400% 400%;
        animation: gradient-border 3s ease infinite;
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
    }
    @keyframes gradient-border {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    <div class="neon-cards">
        <div class="neon-card">🎮</div>
        <div class="neon-card">🎵</div>
        <div class="neon-card">🎬</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def _render_cards_hovers():
    """Render cards and hover effects tab."""
    st.subheader("Cards & Hover Effects")

    st.markdown("**3D Flip Cards**")
    st.markdown(
        """
    <style>
    .flip-container {
        display: flex;
        gap: 30px;
        justify-content: center;
        padding: 20px;
        perspective: 1000px;
    }
    .flip-card {
        width: 180px;
        height: 220px;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.8s;
    }
    .flip-card:hover {
        transform: rotateY(180deg);
    }
    .flip-front, .flip-back {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 15px;
        backface-visibility: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        box-sizing: border-box;
    }
    .flip-front {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .flip-back {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        transform: rotateY(180deg);
    }
    .flip-front .icon { font-size: 3rem; margin-bottom: 10px; }
    </style>
    <div class="flip-container">
        <div class="flip-card">
            <div class="flip-front">
                <div class="icon">🎯</div>
                <strong>Hover Me!</strong>
            </div>
            <div class="flip-back">
                <strong>Back Side!</strong>
                <p style="font-size: 0.9rem; margin-top: 10px;">Hidden content revealed</p>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-front">
                <div class="icon">💡</div>
                <strong>Ideas</strong>
            </div>
            <div class="flip-back">
                <strong>Creative!</strong>
                <p style="font-size: 0.9rem; margin-top: 10px;">Inspiration awaits</p>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Hover Lift Cards**")
    st.markdown(
        """
    <style>
    .lift-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        padding: 30px;
    }
    .lift-card {
        width: 200px;
        padding: 30px;
        background: white;
        border-radius: 15px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .lift-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    .lift-card .emoji { font-size: 2.5rem; margin-bottom: 15px; }
    .lift-card h4 { margin: 0; color: #333; }
    .lift-card p { margin: 10px 0 0; color: #666; font-size: 0.9rem; }
    </style>
    <div class="lift-container">
        <div class="lift-card">
            <div class="emoji">📊</div>
            <h4>Analytics</h4>
            <p>Track your data</p>
        </div>
        <div class="lift-card">
            <div class="emoji">🔒</div>
            <h4>Security</h4>
            <p>Stay protected</p>
        </div>
        <div class="lift-card">
            <div class="emoji">🚀</div>
            <h4>Performance</h4>
            <p>Lightning fast</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Gradient Border on Hover**")
    st.markdown(
        """
    <style>
    .gradient-hover-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        padding: 30px;
        background: #1a1a2e;
        border-radius: 15px;
    }
    .gradient-hover-card {
        width: 180px;
        height: 120px;
        background: #16213e;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        position: relative;
        overflow: hidden;
        transition: all 0.3s;
    }
    .gradient-hover-card::before {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 12px;
        padding: 2px;
        background: linear-gradient(45deg, transparent, transparent);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        transition: all 0.3s;
    }
    .gradient-hover-card:hover::before {
        background: linear-gradient(45deg, #e94560, #ff6b6b, #ffd93d, #6bcb77);
    }
    .gradient-hover-card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
    }
    </style>
    <div class="gradient-hover-container">
        <div class="gradient-hover-card">Hover Me</div>
        <div class="gradient-hover-card">Magic Border</div>
        <div class="gradient-hover-card">CSS Power</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def _render_advanced_effects():
    """Render advanced effects tab."""
    st.subheader("Advanced Effects")

    st.markdown("**Morphing Shape**")
    st.markdown(
        """
    <style>
    .morph-container {
        display: flex;
        justify-content: center;
        padding: 40px;
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border-radius: 15px;
    }
    .morph-shape {
        width: 150px;
        height: 150px;
        background: linear-gradient(45deg, #e94560, #ff6b6b);
        animation: morph 8s ease-in-out infinite;
    }
    @keyframes morph {
        0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
        25% { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
        50% { border-radius: 50% 60% 30% 60% / 30% 60% 70% 40%; }
        75% { border-radius: 60% 40% 60% 30% / 70% 30% 50% 60%; }
    }
    </style>
    <div class="morph-container">
        <div class="morph-shape"></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Particle Background**")
    st.markdown(
        """
    <style>
    .particle-bg {
        background: #0f0f23;
        height: 200px;
        border-radius: 15px;
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .particle {
        position: absolute;
        width: 6px;
        height: 6px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        animation: particle-float 15s infinite;
    }
    .particle:nth-child(1) { left: 10%; animation-delay: 0s; animation-duration: 12s; }
    .particle:nth-child(2) { left: 20%; animation-delay: 2s; animation-duration: 14s; }
    .particle:nth-child(3) { left: 30%; animation-delay: 4s; animation-duration: 10s; }
    .particle:nth-child(4) { left: 40%; animation-delay: 1s; animation-duration: 16s; }
    .particle:nth-child(5) { left: 50%; animation-delay: 3s; animation-duration: 11s; }
    .particle:nth-child(6) { left: 60%; animation-delay: 5s; animation-duration: 13s; }
    .particle:nth-child(7) { left: 70%; animation-delay: 2s; animation-duration: 15s; }
    .particle:nth-child(8) { left: 80%; animation-delay: 4s; animation-duration: 12s; }
    .particle:nth-child(9) { left: 90%; animation-delay: 1s; animation-duration: 14s; }
    @keyframes particle-float {
        0% { transform: translateY(200px) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-20px) rotate(720deg); opacity: 0; }
    }
    .particle-text {
        color: white;
        font-size: 1.5rem;
        z-index: 10;
        text-shadow: 0 0 20px rgba(255,255,255,0.5);
    }
    </style>
    <div class="particle-bg">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <span class="particle-text">Floating Particles</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Gradient Text Animation**")
    st.markdown(
        """
    <style>
    .animated-gradient-container {
        background: #1a1a2e;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
    }
    .animated-gradient-text {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #ff0080, #ff8c00, #40e0d0, #7b68ee, #ff0080);
        background-size: 400% 100%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-flow 4s ease infinite;
    }
    @keyframes gradient-flow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    <div class="animated-gradient-container">
        <span class="animated-gradient-text">Rainbow Gradient Flow</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Neumorphism Design**")
    st.markdown(
        """
    <style>
    .neumorphism-container {
        background: #e0e5ec;
        padding: 40px;
        border-radius: 20px;
        display: flex;
        gap: 30px;
        justify-content: center;
        align-items: center;
    }
    .neu-card {
        width: 120px;
        height: 120px;
        border-radius: 20px;
        background: #e0e5ec;
        box-shadow: 9px 9px 16px #b8bec7, -9px -9px 16px #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        transition: all 0.3s;
    }
    .neu-card:hover {
        box-shadow: inset 9px 9px 16px #b8bec7, inset -9px -9px 16px #ffffff;
    }
    .neu-btn {
        padding: 15px 40px;
        border-radius: 30px;
        background: #e0e5ec;
        box-shadow: 6px 6px 12px #b8bec7, -6px -6px 12px #ffffff;
        border: none;
        color: #666;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s;
    }
    .neu-btn:hover {
        box-shadow: inset 6px 6px 12px #b8bec7, inset -6px -6px 12px #ffffff;
    }
    </style>
    <div class="neumorphism-container">
        <div class="neu-card">☀️</div>
        <div class="neu-card">🌙</div>
        <button class="neu-btn">Soft UI</button>
    </div>
    """,
        unsafe_allow_html=True,
    )

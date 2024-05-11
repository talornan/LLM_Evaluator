import streamlit as st
import asyncio
import sys

sys.path.append('../..')
from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.pagesOfApp.authentication import AuthenticationManager
from llm_code import state

# hide the sidebar
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)
auth_manager = AuthenticationManager()

if state.is_connected():
    st.markdown('<div class="welcome-message">Hello ' + state.get_user_name() + '</div>', unsafe_allow_html=True)


def about_page():
    st.markdown(
        f"""
        <div class="title-container">
            <h1 style="color: #3498db ;">App Overview</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Model Developer/Analyst section
    with st.expander("For Model Developer/Analyst", expanded=False):
        st.markdown(
            """
            <div class="expander-content">
                <h2 class="expander-title">For Model Developers/Analysts</h2>
                <p class="expander-text">
                    Welcome, Model Developers and Analysts! Are you passionate about creating cutting-edge language models and analyzing their performance? You're in the right place! Our app provides you with a powerful toolkit to evaluate your models, compare different approaches, and gain valuable insights.
                </p>
                <div class="feature">
                    <h3>Features</h3>
                    <ul class="feature-list">
                        <li>Evaluate Model Performance: Compare the performance of different language models using various metrics.</li>
                        <li>Compare Different Models: Select multiple language models and metrics to compare their performance.</li>
                        <li>Get Aggregated Statistics: View aggregated statistics on the performance of selected models across different metrics.</li>
                    </ul>
                </div>
                <div class="how-to-use">
                    <h3>How to Use</h3>
                    <ol class="how-to-use-list">
                        <li>Select the language models you want to evaluate.</li>
                        <li>Choose the metrics you want to compare.</li>
                        <li>Click the "Generate Report" button to generate aggregated statistics and visualizations.</li>
                    </ol>
                </div>
                <p>
                    Ready to take your model evaluation to the next level? Dive in and explore the possibilities!
                </p>
                <p>
                    For any questions or assistance, feel free to reach out to our support team at 
                    <a href="mailto:talornan500@gmail.com" class="contact-link">talornan500@gmail.com</a>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Prompts Engineer section
    with st.expander("For Prompts Engineer", expanded=False):
        st.markdown(
            """
            <div class="expander-content">
                <h2 class="expander-title">For Prompts Engineers</h2>
                <p class="expander-text">
                    Hey there, Prompts Engineers! Are you ready to unlock the potential of language models and craft compelling prompts? Our app empowers you to generate and analyze responses with ease. Whether you're creating interactive chatbots, generating creative content, or conducting research, we've got you covered!
                </p>
                <div class="feature">
                    <h3>Features</h3>
                    <ul class="feature-list">
                        <li>Response Generation: Enter prompts and generate responses from language models.</li>
                        <li>Response Analysis: Analyze generated responses using various metrics.</li>
                        <li>Visualization: Visualize metric scores and compare different responses.</li>
                    </ul>
                </div>
                <div class="how-to-use">
                    <h3>How to Use</h3>
                    <ol class="how-to-use-list">
                        <li>Enter your prompt in the text input field.</li>
                        <li>Select the language models you want to generate responses from.</li>
                        <li>Choose the metrics you want to analyze the responses with.</li>
                        <li>Click the "Generate Response" button to generate responses and view analysis.</li>
                    </ol>
                </div>
                <p>
                    Ready to bring your prompts to life? Let's get started on your creative journey!
                </p>
                <p>
                    For any questions or assistance, feel free to reach out to our support team at 
                    <a href="mailto:talornan500@gmail.com" class="contact-link">talornan500@gmail.com</a>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.page_link("Home.py", label="Home", icon="🏠")


about_page()

import streamlit as st


def about_page():
    st.markdown(
        """
        <div class="title-container">
            <h1 style="color: #4B0082;">App Overview</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Model Developer/Analyst section
    with st.expander("For Model Developer/Analyst", expanded=False):
        st.markdown(
            """
            <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
                <h2 style="color: #4B0082;">For Model Developers/Analysts</h2>
                <p style="font-size: 16px; color: #555555;">
                    This section is designed for Model Developers/Analysts who create models for the LLM (Large Language Model) and are interested in evaluating their performance.
                </p>
                <h3 style="color: #9370DB;">Features</h3>
                <ul style="list-style-type: square; font-size: 14px; color: #555555; padding-left: 20px;">
                    <li>Evaluate Model Performance: Compare the performance of different language models using various metrics.</li>
                    <li>Compare Different Models: Select multiple language models and metrics to compare their performance.</li>
                    <li>Get Aggregated Statistics: View aggregated statistics on the performance of selected models across different metrics.</li>
                </ul>
                <h3 style="color: #9370DB;">How to Use</h3>
                <ol style="list-style-type: decimal; font-size: 14px; color: #555555; padding-left: 20px;">
                    <li>Select the language models you want to evaluate.</li>
                    <li>Choose the metrics you want to compare.</li>
                    <li>Click the "Generate Report" button to generate aggregated statistics and visualizations.</li>
                </ol>
                <p style="font-size: 14px; color: #555555;">
                    For any questions or assistance, feel free to reach out to our support team at 
                    <a href="mailto:talornan500@gmail.com" style="color: #007bff;">talornan500@gmail.com</a>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Prompts Engineer section
    with st.expander("For Prompts Engineer", expanded=False):
        st.markdown(
            """
            <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
                <h2 style="color: #4B0082;">For Prompts Engineers</h2>
                <p style="font-size: 16px; color: #555555;">
                    This section is for prompts engineers who want to generate and analyze responses.
                </p>
                <h3 style="color: #9370DB;">Features</h3>
                <ul style="list-style-type: square; font-size: 14px; color: #555555; padding-left: 20px;">
                    <li>Response Generation: Enter prompts and generate responses from language models.</li>
                    <li>Response Analysis: Analyze generated responses using various metrics.</li>
                    <li>Visualization: Visualize metric scores and compare different responses.</li>
                </ul>
                <h3 style="color: #9370DB;">How to Use</h3>
                <ol style="list-style-type: decimal; font-size: 14px; color: #555555; padding-left: 20px;">
                    <li>Enter your prompt in the text input field.</li>
                    <li>Select the language models you want to generate responses from.</li>
                    <li>Choose the metrics you want to analyze the responses with.</li>
                    <li>Click the "Generate Response" button to generate responses and view analysis.</li>
                </ol>
                <p style="font-size: 14px; color: #555555;">
                    For any questions or assistance, feel free to reach out to our support team at 
                    <a href="mailto:talornan500@gmail.com" style="color: #007bff;">talornan500@gmail.com</a>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.page_link("Home.py", label="Home", icon="🏠")


about_page()

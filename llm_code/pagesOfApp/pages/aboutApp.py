import streamlit as st
import asyncio
import sys

sys.path.append('../..')
from llm_code.pagesOfApp.style.LLMS_Analysis_style import configure_streamlit_theme

def about_page():
    st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)
    st.title("About the App")

    # Model Developer/Analyst section
    with st.expander("For Model Developer/Analyst", expanded=True):
        st.markdown(
            """
            <div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px;">
                <h2 style="color: #333333;">For Model Developer/Analyst</h2>
                <p style="font-size: 16px; color: #666666;">
                    This page is designed for Model Developers/Analysts who are responsible for developing models 
                    for the Ilm (Large Language Model) and are interested in evaluating the performance of their models.
                </p>
                <h3 style="color: #9370DB;">Features</h3>
                <ul style="list-style-type: square; font-size: 14px; color: #666666; padding-left: 20px;">
                    <li>Evaluate Model Performance: Compare the performance of different language models using various metrics.</li>
                    <li>Compare Different Models: Select multiple language models and metrics to compare their performance.</li>
                    <li>Get Aggregated Statistics: View aggregated statistics on the performance of selected models across different metrics.</li>
                </ul>
                <h3 style="color: #9370DB;">How to Use</h3>
                <ol style="list-style-type: decimal; font-size: 14px; color: #666666; padding-left: 20px;">
                    <li>Select the language models you want to evaluate.</li>
                    <li>Choose the metrics you want to compare.</li>
                    <li>Click the "Generate Report" button to generate aggregated statistics and visualizations.</li>
                </ol>
                <p style="font-size: 14px; color: #666666;">
                    If you have any questions or need assistance, feel free to reach out to our support team at 
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
            <div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px;">
                <h2 style="color: #9370DB;">For Prompts Engineer</h2>
                <p style="font-size: 16px; color: #666666;">
                    This page is for prompts engineers who want to generate responses and analyze them.
                </p>
                <h3 style="color: #9370DB;">Features</h3>
                <ul style="list-style-type: square; font-size: 14px; color: #666666; padding-left: 20px;">
                    <li>Response Generation: Enter prompts and generate responses from language models.</li>
                    <li>Response Analysis: Analyze generated responses using various metrics.</li>
                    <li>Visualization: Visualize metric scores and compare different responses.</li>
                </ul>
                <h3 style="color: #9370DB;">How to Use</h3>
                <ol style="list-style-type: decimal; font-size: 14px; color: #666666; padding-left: 20px;">
                    <li>Enter your prompt in the text input field.</li>
                    <li>Select the language models you want to generate responses from.</li>
                    <li>Choose the metrics you want to analyze the responses with.</li>
                    <li>Click the "Generate Response" button to generate responses and view analysis.</li>
                </ol>
                <p style="font-size: 14px; color: #666666;">
                    If you have any questions or need assistance, feel free to reach out to our support team at 
                    <a href="mailto:talornan500@gmail.com" style="color: #007bff;">talornan500@gmail.com</a>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

about_page()

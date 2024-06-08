import asyncio
import logging

from fastapi import requests

import streamlit as st
from openai import OpenAI
import numpy as np
import base64
import matplotlib.pyplot as plt
import sys

sys.path.append('../..')
from llm_code.app.api.endpoints.analysisAPI import create_prompt
from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.llm_metrics import Metrics, MetricsModel
from llm_code.app.api.endpoints.data_analyze_api import insert_metric, get_analysis_results
from evaluate import load
from datasets import load_metric
from llm_code import state
from llm_code.schemas.metric_result_schema import MetricResultSchema
from llm_code.pagesOfApp.pages.login import logout
from llm_code.pagesOfApp.style.homeStyle import configure_home_theme

st.set_page_config(initial_sidebar_state="collapsed")

client = OpenAI(api_key="")
# Set Streamlit page configuration

# Apply Streamlit theme
st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)


if not state.is_connected():
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
    st.title("No user is currently logged in "
             "Please select an option")


    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("Home.py", label="home", icon="🏠")
    with col2:
        st.page_link("pages/login.py", label=None, icon=None)
    with col3:
        st.page_link("pages/signup.py", label=None, icon=None)
else:
    # Define colors
    background_color = "#f0f0f0"
    title_color = "#ff69b4"
    text_color = "#800080"

    st.markdown('<div class="welcome-message">Hello ' + state.get_user_name() + '</div>', unsafe_allow_html=True)
    st.page_link("Home.py", label="home", icon="🏠")

    # Define available metrics
    available_metrics = ["Rouge", "exact_match", "Chrf", "Toxicity", "Bleu"]

    # Define available language models with their corresponding model IDs
    available_models = {
        "GPT-4 Turbo": "gpt-4-turbo",
        "GPT-3.5 Turbo": "gpt-3.5-turbo",
    }

    # Define colors for language models and metrics
    model_colors = ['#FF69B4', '#9370DB']  # Pink, Purple
    metric_colors = ['#ADD8E6', '#FFD700', '#00FF00', '#00FFFF']  # Light Blue, Gold, Green, Cyan


    # Function to generate a download link for the bar chart
    def get_image_download_link(fig):
        """Generates a download link for the bar chart as a PNG image."""
        fig.savefig("grouped_bar_chart.png", bbox_inches='tight', pad_inches=0.2)
        with open("grouped_bar_chart.png", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:file/png;base64,{b64}" download="grouped_bar_chart.png">Download Grouped Bar Chart</a>'
        return href


    st.title("LLMS Response Generator and Metrics Analysis")

    # User input section for analysis
    prompt_analyze = st.text_input("Enter Prompt to Analyze", placeholder="Enter your prompt here...")
    selected_model = st.multiselect("Select Language Model", available_models)
    selected_metrics = st.multiselect("Select Metrics", available_metrics)

    logout()

    # Generate response button for analysis
    if st.button("Generate Response"):
        if not prompt_analyze:
            st.warning("Please enter a prompt to analyze.")
        else:
            st.write("Generating Response...")

        # Add prompt to database
        # handle_database(prompt_analyze)

        # Initialize lists to store responses and metric scores
        responses = []
        metric_scores = {metric: [] for metric in selected_metrics}

        # Generate response for each selected model
        for model_name in selected_model:
            model_id = available_models[model_name]
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "system", "content": prompt_analyze}],
                max_tokens=100
            )
            response_text = response.choices[0].message.content.strip()
            responses.append(response_text)

            # Calculate metrics for the response
            for metric in selected_metrics:
                if metric == "Rouge":

                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).rouge_score()

                elif metric == "Bleu":

                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).bleu_score()
                elif metric == "Chrf":

                    score = Metrics(predictions=[response_text],
                                    references=[prompt_analyze]).chrf_score()
                elif metric == "exact_match":

                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).exact_match_score()
                elif metric == "Toxicity":

                    score = MetricsModel(predictions=[response_text],
                                         model_type=model_name.lower()).toxicity_score()
                else:
                    score = np.nan

                print(f'*****************{metric} : {score}*****************')
                metric_scores[metric].append(score)
                import requests

                user = MetricResultSchema(username=state.get_user_name(),
                                          metric_name=metric,
                                          prompt=prompt_analyze,
                                          prompt_generation=response_text,
                                          metric_value=score,
                                          model_id=model_id)

                requests.post("http://localhost:8001/insert_metric_result", json=user.dict())

        st.subheader("LLMS Responses:")
        for i, (model_name, response) in enumerate(zip(selected_model, responses)):
            st.write(f"{model_name} Response:")
            st.info(response)

        # Display metric scores in a table
        st.subheader("Metric Scores:")
        metric_table_data = {"Metric": selected_metrics}
        for model_name in selected_model:
            metric_table_data[model_name] = [metric_scores[metric][selected_model.index(model_name)] for metric in
                                             selected_metrics]
        st.table(metric_table_data)

        # Create grouped bar chart for metrics analysis
        fig, ax = plt.subplots()
        x = np.arange(len(selected_metrics))
        bar_width = 0.15

        for i, model_name in enumerate(selected_model):
            scores = [metric_scores[metric][i] for metric in selected_metrics]
            ax.bar(x + i * bar_width, scores, bar_width, label=model_name, color=metric_colors[i])

        ax.set_xlabel('Metrics')
        ax.set_ylabel('Score')
        ax.set_title('LLMS Metrics Analysis')
        ax.set_xticks(x + (len(selected_model) * bar_width) / 2)
        ax.set_xticklabels(selected_metrics)
        ax.legend()

        # Show the plot
        st.pyplot(fig)

        # Download button for the generated graph
        st.subheader("Download Graph")
        st.markdown(get_image_download_link(fig), unsafe_allow_html=True)

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
from llm_code.app.api.endpoints.analysis_results_Api import create_analysis_result, get_analysis_results
from evaluate import load
from datasets import load_metric
from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.pagesOfApp.authentication import AuthenticationManager

st.set_page_config(page_title="LLMS Analysis", page_icon="📊")

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)
auth_manager = AuthenticationManager()


# Set up your OpenAI API key
client = OpenAI(api_key="")

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)

# Define available metrics
available_metrics = ["Rouge", "exact_match", "Mauve", "Toxicity", "Bleu"]

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


# # Define an asynchronous function to handle database interaction
# async def handle_database(prompt_text, responses, metric_scores, selected_model):
#     try:
#         # Add analysis results to the database
#         for response, model_name in zip(responses, selected_model):
#             for metric_name, metric_value in metric_scores.items():
#                 # Ensure metric_value is a single value, not a list
#                 if isinstance(metric_value, list):
#                     metric_value = metric_value[selected_model.index(model_name)]
#
#                 data = {
#                     "prompt": prompt_text,
#                     "response": response,
#                     "metric_name": metric_name,
#                     "metric_value": metric_value,
#                     "model_name": model_name
#                 }
#                 result = await create_analysis_result(data)
#                 if result:
#                     st.write("Analysis result stored successfully:")
#                     st.write(result)
#                 else:
#                     st.error("Failed to store analysis result. Please check the server logs.")
#     except Exception as e:
#         st.error(f"Error handling database operations: {e}")
#         logging.error(f"Error handling database operations: {e}")
#
#
# def store_analysis_results(prompt_text, responses, metric_scores, selected_model):
#     asyncio.run(handle_database(prompt_text, responses, metric_scores, selected_model))


st.title("LLMS Response Generator and Metrics Analysis")

# User input section for analysis
prompt_analyze = st.text_input("Enter Prompt to Analyze", placeholder="Enter your prompt here...")
selected_model = st.multiselect("Select Language Model", available_models)
selected_metrics = st.multiselect("Select Metrics", available_metrics)

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
                elif metric == "Mauve":

                    score = Metrics(predictions=[response_text],
                                    references=[prompt_analyze]).mauve_score()
                elif metric == "exact_match":

                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).exact_match_score()
                elif metric == "Toxicity":

                    score = MetricsModel(predictions=[response_text],
                                         model_type=model_name.lower()).toxicity_score()
                else:

                    score = np.nan
                metric_scores[metric].append(score)
        # # Store analysis results in the database
        # store_analysis_results(prompt_analyze, responses, metric_scores, selected_model)
        # # Display generated responses
        # for i, response in enumerate(responses):
        #     st.subheader(f"Response from {selected_model[i]}")
        #     st.text_area(f"Response {i + 1}", response, height=200)

        # Display metric scores

        st.subheader("Metric Scores:")
        for metric in selected_metrics:
            st.write(f"{metric}:")
            for i, score in enumerate(metric_scores[metric]):
                st.write(f"  - {selected_model[i]}: {score}")

        # Create grouped bar chart for metrics analysis
        fig, ax = plt.subplots()
        x = np.arange(len(selected_model))
        bar_width = 0.15
        for i, metric in enumerate(selected_metrics):
            scores = metric_scores[metric]
            # Extract and plot individual components of metric score dictionary
            component_labels = scores[0].keys()
            component_indices = np.arange(len(component_labels))
            for j, component_label in enumerate(component_labels):
                component_values = [score[component_label] for score in scores]
                ax.bar(x + (i + j * 0.1) * bar_width, component_values, bar_width / len(scores),
                       label=f"{metric} - {component_label}", color=metric_colors[j])

        ax.set_xlabel('Language Models')
        ax.set_ylabel('Score')
        ax.set_xlabel('Language Models')
        ax.set_ylabel('Score')
        ax.set_title('LLMS Metrics Analysis')
        ax.set_xticks(x + bar_width * (len(selected_metrics) - 1) / 2)
        ax.set_xticklabels(selected_model)
        ax.legend()

        # Show the plot
        st.pyplot(fig)

        # Download button for the generated graph
        st.subheader("Download Graph")
        st.markdown(get_image_download_link(fig), unsafe_allow_html=True)
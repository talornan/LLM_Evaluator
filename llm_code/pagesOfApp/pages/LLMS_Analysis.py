import logging
from rouge_score import rouge_scorer

import streamlit as st
from openai import OpenAI
import numpy as np
import base64
import matplotlib.pyplot as plt
import sys

sys.path.append('../..')
from llm_code.app.api.endpoints.analysisAPI import create_prompt
from llm_code.pagesOfApp.style.LLMS_Analysis_style import configure_streamlit_theme
from llm_code.llm_metrics import Metrics, MetricsModel
from evaluate import load
from datasets import load_metric

# Set up your OpenAI API key
client = OpenAI(api_key="")

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)

# Define available metrics
available_metrics = ["Rouge", "exact_match", "Fluency", "Toxicity", "Bleu"]

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


# Async function to add prompt
async def add_prompt(prompt_text):
    try:
        prompt_data = {"prompt_text": prompt_text}
        response = await create_prompt(prompt_data)  # Await create_prompt function
        if isinstance(response, dict) and response.get("success"):
            print("Prompt added successfully!")
        else:
            print("Failed to add prompt. Please try again later.")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error adding prompt: {e}")


# Function to handle database interaction
def handle_database(prompt_text):
    try:
        # Call the async function to add the prompt
        st.write("Adding prompt to database...")
        add_prompt(prompt_text)
    except Exception as e:
        st.error(f"Error adding prompt to database: {e}")


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
        handle_database(prompt_analyze)

        # Initialize lists to store responses and metric scores
        responses = []
        metric_scores = {metric: [] for metric in selected_metrics}

        # Generate response for each selected model
        for model_name in selected_model:  # Change selected_model to selected_models
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
                    # For ROUGE, compute the score using RougeScorer
                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).rouge_score()
                elif metric == "Bleu":
                    # For BLEU, compute the score using the Metrics class
                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).bleu_score()
                elif metric == "Fluency":
                    # For Fluency, compute the score using the Metrics class
                    score = MetricsModel(predictions=[response_text],
                                         model_type=model_name.lower()).fluency_score()  # Use model_name instead of selected_model
                elif metric == "exact_match":
                    # For Coherence, compute the score using the Metrics class
                    score = Metrics(predictions=[response_text], references=[prompt_analyze]).exact_match_score()
                elif metric == "Toxicity":
                    # For Toxicity, compute the score using the Metrics class
                    score = MetricsModel(predictions=[response_text],
                                         model_type=model_name.lower()).toxicity_score()  # Use model_name instead of selected_model
                else:
                    # Handle unknown metric
                    score = np.nan
                metric_scores[metric].append(score)

        # Display generated responses
        for i, response in enumerate(responses):
            st.subheader(f"Response from {selected_model[i]}")
            st.text_area(f"Response {i + 1}", response, height=200)

        # Display metric scores
        st.subheader("Metric Scores:")
        for metric in selected_metrics:
            st.write(f"{metric}:")
            for i, score in enumerate(metric_scores[metric]):
                st.write(f"  - {selected_model[i]}: {score}")

        # Create grouped bar chart for metrics analysis
        fig, ax = plt.subplots()
        metrics_labels = list(metric_scores.keys())
        bar_width = 0.2
        x = np.arange(len(selected_model))

        for i, metric in enumerate(metrics_labels):
            scores = metric_scores[metric]
            ax.bar(x + i * bar_width, scores, bar_width, label=metric, color=metric_colors[i])

        ax.set_xlabel('Language Models')
        ax.set_ylabel('Score')
        ax.set_title('LLMS Metrics Analysis')
        ax.set_xticks(x + bar_width * (len(metrics_labels) - 1) / 2)
        ax.set_xticklabels(selected_model)
        ax.legend()

        # Show the plot
        st.pyplot(fig)

        # Download button for the generated graph
        st.subheader("Download Graph")
        st.markdown(get_image_download_link(fig), unsafe_allow_html=True)

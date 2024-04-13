import logging

import streamlit as st
import numpy as np
import base64
import matplotlib.pyplot as plt
import asyncio
import sys

sys.path.append('..')

from llm_code.app.api.endpoints.analysisAPI import create_prompt
from style.LLMS_Analysis_style import configure_streamlit_theme
from llm_code.llm_metrics import Metrics

# Configure Streamlit theme
st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)

# Define available metrics
available_metrics = ["Rouge", "Coherence", "Fluency", "Toxicity"]

# Define available language models
available_models = ["GPT-2", "GPT-3", "BERT"]


# Function to generate a download link for the bar chart
def get_image_download_link(fig):
    """Generates a download link for the bar chart as a PNG image."""
    fig.savefig("grouped_bar_chart.png", bbox_inches='tight', pad_inches=0.2)
    with open("grouped_bar_chart.png", "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="grouped_bar_chart.png">Download Grouped Bar Chart</a>'
    return href


# Set the font family for Matplotlib to match Streamlit theme
plt.rcParams['font.family'] = 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'


# Rest of your code remains unchanged...


# Define a function to simulate generating response
def generate_response(prompt, selected_model):
    # Simulate response generation (replace this with actual AI response generation)
    response = f"This is a simulated response to the prompt: '{prompt}' using the {selected_model} model."
    return response


def calculate_metrics(response, selected_metrics):
    print("Calculating metrics...")
    print("Selected metrics:", selected_metrics)  # Debug statement

    # Initialize a Metrics object
    metrics_calculator = Metrics()  # Instantiate the Metrics class

    # Initialize scores dictionary
    scores = {}

    # Calculate scores for selected metrics
    for metric in selected_metrics:
        method_name = metric.lower().replace(" ", "_") + "_score"  # Adjust method name
        if hasattr(metrics_calculator, method_name):
            # Call the corresponding method in the Metrics class
            scores[metric] = getattr(metrics_calculator, method_name)()
        else:
            scores[metric] = np.nan  # Set to NaN if metric not found

    print("Calculated scores:", scores)  # Debug statement
    return scores


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


# Main Streamlit app
st.title("LLMS Metrics Analysis")

# User input section
prompt_add = st.text_input("Enter Prompt to Add", "Enter your prompt here...")

# Generate response button for adding prompt
if st.button("Add Prompt"):
    if prompt_add:
        # Call the async function to add prompt
        asyncio.run(add_prompt(prompt_add))
    else:
        st.warning("Please enter a prompt to add.")

# User input section for analysis
# prompt_analyze = st.text_input("Enter Prompt to Analyze", "Enter your prompt here...")
selected_models = st.multiselect("Select Language Models", available_models, key="model")
selected_metrics = st.multiselect("Select Metrics", available_metrics, key="metric")

# Generate response button for analysis
if st.button("Generate Response"):
    if not selected_metrics:
        st.error("Please select at least one metric.")
    elif not prompt_add:
        st.warning("Please enter a prompt to analyze.")
    else:
        st.write("Analyzing Metrics...")

        # Display the LLMS model's response to the user prompt
        st.subheader("LLMS Model Response:")
        for model in selected_models:
            response = generate_response(prompt_add, model)
            st.write(f"Model: {model}")
            st.text_area("Response", response, height=200)

        # Initialize a dictionary to store scores for each model
        model_scores = {model: {} for model in selected_models}

        # Loop through selected language models
        for model in selected_models:
            # Simulate response generation
            response = generate_response(prompt_add, model)

            # Calculate metrics
            scores = calculate_metrics(response, selected_metrics)

            # Store scores for the current model
            model_scores[model] = scores

        # Create grouped bar chart
        fig, ax = plt.subplots()
        metrics_labels = list(model_scores[selected_models[0]].keys())
        bar_width = 0.2
        x = np.arange(len(metrics_labels))

        colors = ['#FF69B4', '#9370DB', '#ADD8E6']  # Pink, Purple, Light Blue

        for i, model in enumerate(selected_models):
            scores = [model_scores[model][metric] for metric in metrics_labels]
            ax.bar(x + i * bar_width, scores, bar_width, label=model, color=colors[i])

        ax.set_xlabel('Metrics')
        ax.set_ylabel('Score')
        ax.set_title('LLMS Metrics Analysis')
        ax.set_xticks(x + bar_width * (len(selected_models) - 1) / 2)
        ax.set_xticklabels(metrics_labels)
        ax.legend()

        # Show the plot
        st.pyplot(fig)

        # Download button for the generated graph
        st.subheader("Download Graph")
        st.markdown(get_image_download_link(fig), unsafe_allow_html=True)

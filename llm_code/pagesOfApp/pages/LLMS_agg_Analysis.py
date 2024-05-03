import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import asyncio
import sys

sys.path.append('../..')
from llm_code.pagesOfApp.style.style import configure_streamlit_theme

# Sample data (replace with actual data)
models = ["Model A", "Model B", "Model C"]
model_data = {model: np.random.rand(10) for model in models}

st.markdown(configure_streamlit_theme(), unsafe_allow_html=True)


# Function to calculate aggregated metric
def calculate_aggregated_metric(data, func):
    if func == "Mean":
        return np.mean(data)
    elif func == "Median":
        return np.median(data)
    elif func == "Max":
        return np.max(data)
    elif func == "Min":
        return np.min(data)
    elif func == "Sum":
        return np.sum(data)


# Custom CSS for styling
custom_css = """
<style>
.stButton>button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    border-radius: 8px;
}

.stButton>button:hover {
    background-color: #45a049; /* Darker Green */
}

.stSelectbox>div>div>div {
    background-color: #f0f0f0; /* Light Gray */
    color: #333333;
    border-radius: 8px;
    padding: 10px 15px;
    font-size: 16px;
}

.stSlider>div>div>div {
    color: #333333;
}

.stGraph>div>div>div>div>div>div>div {
    background-color: #f0f0f0; /* Light Gray */
}

.stMarkdown>div>div>div>p {
    font-size: 18px;
    color: #333333;
}

.stMarkdown>div>div>div>div>div>div>div {
    background-color: #f0f0f0; /* Light Gray */
    border-radius: 8px;
    padding: 10px 15px;
    font-size: 16px;
    color: #333333;
}
</style>
"""

# Main Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)  # Apply custom CSS

st.title("Model Evaluation")


selected_models = st.multiselect("Select Models", models)


selected_function = st.selectbox("Select Aggregate Function", ["Mean", "Median", "Max", "Min", "Sum"])

# Calculate aggregated metric for the selected models
aggregated_metrics = {}
for model in selected_models:
    aggregated_metrics[model] = calculate_aggregated_metric(model_data[model], selected_function)

# Display aggregated metrics
st.subheader("Aggregated Metrics")
for model, metric in aggregated_metrics.items():
    st.markdown(f"**{selected_function} for {model}:** {metric}")

# Plot data for selected models
plt.figure(figsize=(10, 6))
for model in selected_models:
    plt.plot(model_data[model], label=model)
plt.title("Performance Comparison")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
st.pyplot(plt)

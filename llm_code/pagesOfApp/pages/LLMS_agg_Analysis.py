import streamlit as st
import requests
import pandas as pd
import altair as alt
import sys

from llm_code import state

sys.path.append('../..')
from llm_code.app.api.endpoints.analysisAPI import create_prompt
from llm_code.pagesOfApp.style.style import configure_streamlit_theme
from llm_code.pagesOfApp.pages.login import logout
from llm_code import state

st.set_page_config(initial_sidebar_state="collapsed")

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
    st.page_link("Home.py", label="home", icon="🏠")
    st.title("No user is currently logged in "
             "Please select an option")
    col1, col2 = st.columns(2)
    with col1:
        st.page_link("pages/login.py", label=None, icon=None)
    with col2:
        st.page_link("pages/signup.py", label=None, icon=None)
else:
    # Define the FastAPI backend URL
    BACKEND_URL = "http://localhost:8001/api/analysis_result"
    st.markdown('<div class="welcome-message">Hello ' + state.get_user_name() + '</div>', unsafe_allow_html=True)


    # Define available models with uppercase and lowercase names
    available_models = {
        "GPT-4 Turbo": "gpt-4-turbo",
        "GPT-3.5 Turbo": "gpt-3.5-turbo",
    }

    # Define the list of available metrics
    METRICS = ["Rouge", "exact_match", "Chrf", "Toxicity", "Bleu"]

    # Define the list of available aggregation methods with uppercase and lowercase
    AGG_METHODS = ["AVG", "MAX", "MIN", "SUM", "COUNT"]

    # Streamlit app layout
    st.title("Analysis Results")

    # User input section
    selected_models = st.multiselect("Select Model(s):", list(available_models.keys()))
    selected_metric = st.selectbox("Select Metric:", METRICS)
    selected_agg_methods = st.multiselect("Select Aggregation Method(s):", AGG_METHODS)


    def fetch_data(model_names, metric_name, agg_methods):
        model_ids = [available_models[model_name] for model_name in model_names]
        payload = {
            "model_ids": model_ids,
            "metrics_name": [metric_name.lower()],
            "agg_methods": [method.lower() for method in agg_methods]
        }
        response = requests.post(BACKEND_URL, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch data from the backend.")


    # Fetch and display data when user clicks the button
    if st.button("Fetch Data"):
        data = fetch_data(selected_models, selected_metric, selected_agg_methods)
        if data:
            st.write("Analysis Results:")

            # Flatten the data for display
            flattened_data = []
            for item in data:
                model_id = item.pop("model_id")
                metric_name = item.pop("metric_name")
                for agg_method, value in item.items():
                    flattened_data.append({
                        "Model ID": model_id,
                        "Metric Name": metric_name,
                        "Aggregation Method": agg_method.capitalize(),
                        "Value": value
                    })

            # Display the flattened data in a table
            df = pd.DataFrame(flattened_data)
            st.write(df)

            # Create a bar chart using Altair
            chart = alt.Chart(df).mark_bar().encode(
                x='Model ID',
                y='Value',
                color='Aggregation Method',
                column='Metric Name'
            ).properties(
                title=f'Analysis Results for {", ".join(selected_models)}'
            )
            st.altair_chart(chart, use_container_width=True)

    st.page_link("Home.py", label="home", icon="🏠")
    logout()

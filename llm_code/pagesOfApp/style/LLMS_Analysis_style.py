# streamlit_style.py

def configure_streamlit_theme():
    primary_color = '#FF69B4'  # Pink
    secondary_color = '#9370DB'  # Purple
    accent_color = '#ADD8E6'  # Light Blue

    style = f"""
    <style>
        .reportview-container .main .block-container {{
            max-width: 950px;
            font-family: 'Segoe UI', Tahoma, Verdana, sans-serif;
        }}
        .reportview-container .main {{
            color: {primary_color};
            background-color: #F0F8FF;  /* Light Blue background */
        }}
        .reportview-container .main .block-container {{
            padding-top: 2rem;
            padding-right: 3rem;
            padding-left: 3rem;
            padding-bottom: 2rem;
        }}
        h1 {{
            color: {secondary_color};
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .stTextInput > div > div > input {{
            color: {accent_color};  /* Light Blue text */
        }}
        .stTextInput > div > div > div > div > div > svg {{
            fill: {accent_color};  /* Light Blue SVG icons */
        }}
        .stButton > button {{
            background-color: {primary_color};  /* Pink button */
            color: #FFFFFF;  /* White text */
            border-radius: 5px;
            font-size: 16px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .stButton > button:hover {{
            background-color: #FF1493;  /* Darker Pink hover effect */
        }}
        .stSelectbox > div > div > div {{
            color: {secondary_color};  /* Purple text */
        }}
        .stSelectbox > div > div > div > div > div > svg {{
            fill: {secondary_color};  /* Purple SVG icons */
        }}
        .stMultiselect > div > div > div > div > div > svg {{
            fill: {secondary_color};  /* Purple SVG icons */
        }}
        .stSelectbox div[role="listbox"] .st-af {{
            color: {secondary_color}; /* Purple for selected options */
        }}
        .stMultiselect div[role="listbox"] .st-af {{
            color: {secondary_color}; /* Purple for selected options */
        }}
        .stSelectbox div[role="listbox"] .st-ae {{
            color: {secondary_color}; /* Purple for dropdown indicator */
        }}
        .stMultiselect div[role="listbox"] .st-ae {{
            color: {secondary_color}; /* Purple for dropdown indicator */
        }}
        .stSelectbox div[role="listbox"] .st-dx {{
            color: {secondary_color}; /* Purple for dropdown indicator on hover */
        }}
        .stMultiselect div[role="listbox"] .st-dx {{
            color: {secondary_color}; /* Purple for dropdown indicator on hover */
        }}
        .stSelectbox div[role="listbox"] .st-ae path {{
            fill: {secondary_color}; /* Purple for dropdown indicator arrow */
        }}
        .stMultiselect div[role="listbox"] .st-ae path {{
            fill: {secondary_color}; /* Purple for dropdown indicator arrow */
        }}
        .stSelectbox div[role="listbox"] .st-dx path {{
            fill: {secondary_color}; /* Purple for dropdown indicator arrow on hover */
        }}
        .stMultiselect div[role="listbox"] .st-dx path {{
            fill: {secondary_color}; /* Purple for dropdown indicator arrow on hover */
        }}
        .st-av {{
            border-color: {secondary_color}; /* Purple border color */
        }}
        .st-av:hover {{
            border-color: {secondary_color}; /* Purple border color on hover */
        }}
        .st-ax {{
            background-color: {secondary_color}; /* Purple background color */
        }}
        .st-ax:hover {{
            background-color: {secondary_color}; /* Purple background color on hover */
        }}
        .st-bh {{
            background-color: {secondary_color}; /* Purple background color for dropdown options */
        }}
        .st-bh:hover {{
            background-color: {secondary_color}; /* Purple background color for dropdown options on hover */
        }}
        .st-ax:checked {{
            background-color: {secondary_color}; /* Purple background color for checked dropdown options */
        }}
        .st-ax:checked:hover {{
            background-color: {secondary_color}; /* Purple background color for checked dropdown options on hover */
        }}
        .st-bh:hover .st-ai {{
            color: #FFFFFF; /* White text for dropdown options on hover */
        }}
        .st-ax:checked .st-ai {{
            color: #FFFFFF; /* White text for checked dropdown options */
        }}
        .st-ax:checked:hover .st-ai {{
            color: #FFFFFF; /* White text for checked dropdown options on hover */
        }}
        .st-bs {{
            background-color: {secondary_color}; /* Purple background color for dropdown scrollbar */
        }}
    </style>
    """

    return style

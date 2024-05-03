import asyncio
import sys

sys.path.append('../..')

def configure_streamlit_theme():
    primary_color = '#4B0082'  # Indigo
    secondary_color = '#6A5ACD'  # Slate Blue
    tertiary_color = '#20B2AA'  # Light Sea Green
    accent_color = '#9370DB'  # Medium Purple
    text_color = '#FFFFFF'  # White
    box_background_color = '#F5F5F5'  # Light Gray

    style = f"""
    <style>
        .reportview-container .main .block-container {{
            max-width: 950px;
            font-family: 'Segoe UI', Tahoma, Verdana, sans-serif;
        }}
        .reportview-container .main {{
            color: {text_color};
            background-color: {box_background_color};  /* Light Gray background */
            padding-top: 2rem; /* Adjust padding for top */
            padding-bottom: 2rem; /* Adjust padding for bottom */
        }}
        .reportview-container .main .block-container {{
            padding: 2rem 3rem;
        }}
        h1 {{
            color: {primary_color};
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 48px;  /* Increase font size for h1 */
            margin-bottom: 2rem; /* Adjust margin for bottom */
        }}
        .stTextInput > div > div > input {{
            color: {primary_color};  /* Indigo text */
            background-color: {box_background_color};  /* Light Gray background */
            border: 1px solid {secondary_color};  /* Slate Blue border */
            font-size: 20px;  /* Increase font size for input */
        }}
        .stTextInput > div > div > div > div > div > svg {{
            fill: {primary_color};  /* Indigo SVG icons */
        }}
        .stButton > button {{
            background-color: {accent_color};  /* Medium Purple button */
            color: {text_color};  /* White text */
            border-radius: 5px;
            font-size: 24px;  /* Increase font size for button */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 15px 30px; /* Increased padding for better clickability */
            transition: background-color 0.3s ease; /* Smooth transition on hover */
        }}
        .stButton > button:hover {{
            background-color: #8A2BE2;  /* Darker Purple hover effect */
        }}
        .stSelectbox > div > div > div {{
            color: {secondary_color};  /* Slate Blue text */
            background-color: {box_background_color};  /* Light Gray background */
            border: 1px solid {secondary_color};  /* Slate Blue border */
            font-size: 20px;  /* Increase font size for selectbox */
        }}
        .stSelectbox > div > div > div > div > div > svg {{
            fill: {secondary_color};  /* Slate Blue SVG icons */
        }}
        .stSelectbox div[role="listbox"] .st-af {{
            color: {secondary_color}; /* Slate Blue for selected options */
        }}
        .stSelectbox div[role="listbox"] .st-ae {{
            color: {secondary_color}; /* Slate Blue for dropdown indicator */
        }}
        .stSelectbox div[role="listbox"] .st-dx {{
            color: {secondary_color}; /* Slate Blue for dropdown indicator on hover */
        }}
        .stSelectbox div[role="listbox"] .st-ae path {{
            fill: {secondary_color}; /* Slate Blue for dropdown indicator arrow */
        }}
        .stSelectbox div[role="listbox"] .st-dx path {{
            fill: {secondary_color}; /* Slate Blue for dropdown indicator arrow on hover */
        }}
        .st-av {{
            border-color: {secondary_color}; /* Slate Blue border color */
        }}
        .st-av:hover {{
            border-color: {secondary_color}; /* Slate Blue border color on hover */
        }}
        .st-ax {{
            background-color: {accent_color}; /* Medium Purple background color */
        }}
        .st-ax:hover {{
            background-color: #8A2BE2; /* Darker Purple background color on hover */
        }}
        .st-bs {{
            background-color: {accent_color}; /* Medium Purple background color for dropdown scrollbar */
        }}
        .stPageLink > a {{
            color: {primary_color}; /* Indigo color */
            font-size: 24px; /* Increase font size */
            text-decoration: none; /* Remove underline */
        }}
        .stPageLink > a:hover {{
            color: {accent_color}; /* Medium Purple color on hover */
        }}
    </style>
    """

    return style

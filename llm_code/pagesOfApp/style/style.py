def configure_streamlit_theme():
    primary_color = '#2c3e50'  # Dark blue text color
    secondary_color = '#ecf0f1'  # Light gray background for inputs
    tertiary_color = '#3498db'  # Blue border
    accent_color = '#3498db'  # Blue fill for input icons
    text_color = '#2c3e50'  # Dark blue text color
    background_color = 'rgb(238,174,202)'  # Background gradient
    button_color = '#3498db'  # Blue background for buttons
    button_hover_color = '#ccc'  # Gray background on hover

    style = f"""
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: {primary_color};
            background: {background_color};
        }}

        
        .text-color-adjusted {{
            color: white; /* Default text color */
        }}
        @media (min-width: 576px) {{
            .text-color-adjusted {{
                color: {primary_color}; /* Text color for larger screens */
            }}
        }}

        [data-testid="collapsedControl"] {{
            display: none;
        }}
        .main-content {{
            padding: 20px; /* Add padding to the main content */
            max-width: 800px; /* Set maximum width for the content */
            margin: 0 auto; /* Center the content horizontally */
        }}

        .stTextInput > div > div > input, .stSelectbox > div > div > div > div > div > input {{
            color: {primary_color};
            background-color: {secondary_color};
            border: 2px solid {tertiary_color};
            border-radius: 5px;
            padding: 10px;
            width: 100%; /* Adjust the width as needed */
            box-sizing: border-box;
        }}

        .stTextInput > div > div > div > div > div > svg, .stSelectbox > div > div > div > div > div > svg {{
            fill: {accent_color};
        }}
        ..button-container {{
            display: flex;
            justify-content: center;
            margin-top: 20px; /* Adjust margin as needed */
        }}
        .stButton > button {{
            background-color: #3498db; /* Blue background for buttons */
            color: white !important; /* White text color for buttons */
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        .stButton > button:hover {{
            background-color: #ccc; /* Gray background on hover */
        }}
        .welcome-message, .greeting-message {{
            color: #3498db; /* Blue color for messages */
            font-size: 20px; /* Adjust font size as needed */
            margin-bottom: 20px; /* Add some margin */
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #3498db; /* Blue color for headings */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: bold;
            text-align: center; /* Center headings */
        }}
        .greeting-message {{
            font-size: 20px; /* Adjust font size as needed */
            margin-bottom: 20px; /* Add some margin */
        }}
    </style>
    """

    return style

def configure_home_theme():
    custom_styles = """
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #2c3e50; /* Dark blue text color */
            background: rgb(238,174,202);
            background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);
        }

        /* Dynamically adjust text color based on background luminance */
        .text-color-adjusted {
            color: white; /* Default text color */
        }
        @media (min-width: 576px) {
            .text-color-adjusted {
                color: #2c3e50; /* Text color for larger screens */
            }
        }

        [data-testid="collapsedControl"] {
            display: none;
        }
        .main-content {
            padding: 20px; /* Add padding to the main content */
            max-width: 800px; /* Set maximum width for the content */
            margin: 0 auto; /* Center the content horizontally */
        }

        .stTextInput > div > div > input, .stSelectbox > div > div > div > div > div > input {
            color: #2c3e50; /* Dark blue text color */
            background-color: #ecf0f1; /* Light gray background for inputs */
            border: 2px solid #3498db; /* Blue border */
            border-radius: 5px;
            padding: 10px;
        }
        .stTextInput > div > div > div > div > div > svg, .stSelectbox > div > div > div > div > div > svg {
            fill: #3498db; /* Blue fill for input icons */
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px; /* Adjust margin as needed */
        }
        .stButton > button {
            background-color: #3498db; /* Blue background for buttons */
            color: white !important; /* White text color for buttons */
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #ccc; /* Gray background on hover */
        }
        .welcome-message, .greeting-message {
            color: #3498db; /* Blue color for messages */
            font-size: 20px; /* Adjust font size as needed */
            margin-bottom: 20px; /* Add some margin */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #3498db; /* Blue color for headings */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: bold;
            text-align: center; /* Center headings */
        }
        .greeting-message {
            font-size: 20px; /* Adjust font size as needed */
            margin-bottom: 20px; /* Add some margin */
        }
    </style>
    """
    return custom_styles

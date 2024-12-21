import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from data_loading import load_data, handle_missing_values, add_years_since_last_sold, encode_categorical_columns, remove_nan_rows
from eda import exploratory_data_analysis, correlation_scatter_plots, location_impact, housing_status_comparison, historical_trends, brokers_and_streets
from modeling import predictive_modeling
import os
import signal

app = Flask(__name__)

# Load and preprocess data
file_path = 'data/realtor-data.csv'
data = load_data(file_path)
data = handle_missing_values(data)
data = add_years_since_last_sold(data)
data = encode_categorical_columns(data, 'status')
data = remove_nan_rows(data)

@app.route('/')
def index():
    """
    Renders the homepage of the application.

    This function is triggered by a GET request to the '/' route. It renders and returns the 'index.html'
    template, which serves as the homepage for the real estate data analysis application.

    Returns
    -------
    Response
        A response containing the rendered 'index.html' template.
    """
    return render_template('index.html')

@app.route('/run_analysis', methods=['POST'])
def run_analysis():
    """
    Handles the selection of analysis type from the form and executes the corresponding analysis function.

    This function is triggered by a POST request to the '/run_analysis' route. Based on the user's 
    selection from the dropdown menu, it calls the appropriate analysis function, such as exploratory 
    data analysis, correlation scatter plots, location impact analysis, housing status comparison, 
    historical trends analysis, brokers and streets analysis, or predictive modeling.

    Returns
    -------
    Response
        A redirect response that navigates back to the index page.
    """
    choice = request.form['analysis']
    if choice == "Exploratory Data Analysis":
        exploratory_data_analysis(data)
    elif choice == "Correlation Scatter Plots":
        correlation_scatter_plots(data)
    elif choice == "Location Impact":
        location_impact(data)
    elif choice == "Housing Status Comparison":
        housing_status_comparison(data)
    elif choice == "Historical Trends":
        historical_trends(data)
    elif choice == "Brokers and Streets":
        brokers_and_streets(data)
    elif choice == "Predictive Modeling":
        predictive_modeling(data)
    return redirect(url_for('index'))

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """
    Handles a POST request to shut down the server.

    This function is triggered by a POST request to the '/shutdown' route. It calls the shutdown_server
    function to shut down the server and returns a response with the message "Server shutting down...".

    Returns
    -------
    Response
        A response with the message "Server shutting down...".
    """
    shutdown_server()
    return "Server shutting down..."

def shutdown_server():
    """
    Shuts down the server by sending a SIGINT signal to the process with the current pid.

    This function is used to shut down the Flask server when the user selects the "Close Application" button
    on the index page. It calls os.kill with the current process id and a SIGINT signal to shut down the
    server.

    Returns
    -------
    None
    """
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

if __name__ == "__main__":
    app.run(debug=True)
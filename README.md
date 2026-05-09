# Real-Time Weather Data Pipeline

## Overview
This project fetches real-time weather data using OpenWeather API, processes the data using Python, and stores it in CSV format for analysis.

## Features
- Real-time weather data collection
- Automated scheduling
- Data storage using CSV
- Temperature trend visualization
- Data analysis using Pandas

## Technologies Used
- Python
- REST API
- Pandas
- Matplotlib
- Schedule Library

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Add your OpenWeatherMap API key to `API_KEY` in `main.py`
3. Run the pipeline: `python main.py`
4. Analyze data: `python analysis.py`

## Project Structure
```
weather-data-pipeline/
├── main.py              # Main weather data pipeline
├── analysis.py          # Data analysis and visualization
├── weather_data.csv     # CSV storage for weather data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Getting an API Key
1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Create a free account
3. Copy your API key from the dashboard
4. Paste it in `main.py` where it says `API_KEY = "YOUR_API_KEY"`

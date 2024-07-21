# Student Performance Indicator

This project aims to predict students' performance (test scores) based on various features such as Gender, Ethnicity, Parental level of education, Lunch, and Test preparation course. It involves data ingestion, transformation, model training, and setting up a Flask app for prediction pipelines.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Data Collection](#data-collection)
- [Installation](#installation)
- [Usage](#usage)
- [Enhancements](#enhancements)
- [Contributing](#contributing)

## Problem Statement

This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch, and Test preparation course.

## Data Collection

- **Dataset Source**: [Kaggle - Student Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
- The data consists of 8 columns and 1000 rows.

## Installation

### Clone the Repository

git clone https://github.com/Keerthan04/student-performance-indicator.git
cd student-performance-indicator

#### Create a Virtual Environment

#### using conda

conda create -n student-perf-env python=3.8
conda activate student-perf-env

#### using python venv

python3 -m venv student-perf-env
source student-perf-env/bin/activate  # On Windows use `student-perf-env\Scripts\activate`

#### Install requirements

pip install -r requirements.txt

## Usage

### Run the application

python application.py

### Access the Flask App

Open your web browser and go to http://127.0.0.1:5000/ to access the application.
got to http://127.0.0.1:5000/predictdata/ to make predictions

## Enhancements

Future enhancements planned for this project include:

Enhancing the Frontend: Improve the user interface and user experience of the web application.
Containerization: Use Docker to containerize the application.
Deployment: Deploy the containerized application using Azure.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

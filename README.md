# Content-Based Movie Recommendation System

## Project Overview
This repository contains a content-based movie recommendation system designed to suggest movies similar to a user-selected title. The system utilizes a machine learning model to analyze movie descriptions and genres to find matches based on content similarity. The frontend is implemented using Streamlit, providing an interactive interface for users.

## Features
- **Movie Selection via Dropdown**: Users can choose a movie from a dropdown list to find similar movies.
- **Recommendation Display**: Displays five recommended movies that are content-wise similar to the chosen movie.
- **Interactive UI**: Built using Streamlit for a user-friendly experience.

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning algorithms for building the recommendation engine.
- **Streamlit**: Web app framework.
- **Pickle**: Serialization of Python objects.

## Installation and Setup

### Using Pipenv
This project uses Pipenv to manage dependencies. To set up the project:

1. Clone the repository:

2. Install dependencies using Pipenv:

3. Activate the Pipenv environment:

### Running the App
Start the Streamlit web app by running:
*streamlit run app.py*
Access the web interface by navigating to `http://localhost:8501` in your web browser.

## Data
The `dataset.csv` file is crucial for the operation of this app, containing necessary movie metadata like titles, genres, and descriptions.

## Files and Directories
- `app.py`: The Streamlit application.
- `main.ipynb`: Jupyter notebook containing the scripts for preprocessing the data and building the model.
- `movies_list.pkl`: Serialized file containing the movie list used by the app.
- `dataset.csv`: Dataset file used for model training.
- `Pipfile` & `Pipfile.lock`: Used for managing package installations and ensuring that the environment is reproducible.

## Contributing
We welcome contributions from the community. Here are some ways you can contribute:
- Report bugs and issues.
- Suggest enhancements.
- Improve documentation or extend the functionality.

To contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request.



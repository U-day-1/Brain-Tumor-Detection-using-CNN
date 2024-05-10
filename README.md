# Brain Tumor Detection using Convolutional Neural Networks (CNN)

Welcome to the Brain Tumor Detection project! In this project, we have developed a deep learning model based on Convolutional Neural Networks (CNN) to detect brain tumors from MRI images. We utilized various CNN architectures and techniques to train the model and achieve accurate tumor detection.

## Overview

This project aims to provide a tool for early and accurate detection of brain tumors using MRI scans. Early detection is crucial for timely medical intervention and improving patient outcomes. The deep learning model developed here can assist healthcare professionals in identifying potential tumors quickly and accurately.

### NOTE : Use python 3.11.2 

## Project Structure

- **model/**: Contains the saved trained models.
- **pages/**: Contains different pages for the Streamlit application.
- **About.py**: The main program to run the application.
- **requirements.txt**: Lists all the dependencies required to run the project.

## How to Use

1. **Clone the Repository**: 
   ```
   git clone https://github.com/U-day-1/Brain-Tumor-Detection-using-CNN.git
   cd Brain-Tumor-Detection-using-CNN
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Hosting the Model and UI**:
   - Navigate to the `pages/` directory.
   - Run the Streamlit application:
     ```
     streamlit run About.py
     ```
   - Access the application in your web browser at `http://localhost:8501`.

## Model Performance

We have evaluated the performance of our trained models using various metrics such as accuracy, precision, recall, and F1-score. The models have been trained on a labeled dataset of MRI images containing both tumor and non-tumor samples. 



## Acknowledgments

We would like to express our gratitude to the open-source community for their valuable contributions and support. Special thanks to [Streamlit](https://streamlit.io/) for providing an excellent platform for building interactive web applications with Python.

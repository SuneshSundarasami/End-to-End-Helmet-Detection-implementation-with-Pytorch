# End-to-End Helmet Detection Implementation with PyTorch

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.8%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This repository contains an end-to-end implementation of a **Helmet Detection** system using **PyTorch**. The goal of this project is to detect whether individuals in images or video streams are wearing helmets, which is particularly useful for safety monitoring in workplaces, construction sites, and traffic surveillance.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dataset](#dataset)
6. [Training](#training)
7. [Evaluation](#evaluation)
8. [Results](#results)
9. [Contributing](#contributing)
10. [License](#license)

## Overview
Helmet detection is a critical task in ensuring safety compliance in various industries. This project leverages deep learning techniques to detect helmet usage using **PyTorch**. It includes dataset management with Amazon S3, model training and evaluation, a Flask-based web interface, and containerization with Docker for deployment.

## Features
- **Dataset Management with Amazon S3**: 
  - Loads dataset from an S3 bucket.
  - Saves trained models back to S3 if they outperform previous ones.
- **Model Training & Evaluation**:
  - Implements a deep learning-based helmet detection model using PyTorch.
  - Evaluates model performance and updates the best model in S3.
- **Flask-based Web Interface**:
  - Provides an API to start training and view progress.
  - Access API documentation at `http://127.0.0.1:5000/docs`
- **Docker Support**:
  - Containerizes the entire application for easy deployment.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- AWS CLI configured with the necessary S3 permissions
- Docker (if using containerized deployment)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/SuneshSundarasami/End-to-End-Helmet-Detection-implementation-with-Pytorch.git
   cd End-to-End-Helmet-Detection-implementation-with-Pytorch
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up AWS credentials for S3 access.

## Usage
### Training the Model
Run the following command to start training:
```sh
python train_pipeline.py
```
This will:
- Download the dataset from S3.
- Train the model.
- Evaluate and upload the best model to S3.

### Running the Flask Web Interface
Start the Flask application:
```sh
python app.py
```
Access the interface at: `http://127.0.0.1:5000/`
Access API documentation at: `http://127.0.0.1:5000/docs`

### Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t helmet-detection .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 helmet-detection
   ```

## Dataset
The dataset consists of labeled images of individuals wearing or not wearing helmets. The dataset is stored in an Amazon S3 bucket and is automatically downloaded during training.

## Training
The model is trained using a convolutional neural network (CNN) implemented with PyTorch. The training process includes:
- Data augmentation and preprocessing
- Model architecture definition
- Optimization and loss calculation
- Saving the best-performing model to S3

## Evaluation
The model is evaluated using standard performance metrics such as:
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix

## Results
Results and trained models are stored in the `models/` directory and uploaded to S3. Performance metrics and logs are saved for analysis.

## Folder Structure
```
├── dataset/           # Local dataset storage (if needed)
├── models/            # Trained models
├── scripts/           # Utility scripts
├── app.py             # Flask web application
├── train.py           # Training script
├── Dockerfile         # Docker setup
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## Contributing
Feel free to open issues or submit pull requests to improve this project.

## License
This project is licensed under the MIT License.

## Author
[Sunesh Praveen Raja Sundarasami](https://github.com/SuneshSundarasami)


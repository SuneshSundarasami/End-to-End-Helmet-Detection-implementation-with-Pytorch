import os

# Define the folder structure
folders = {
    "components": [
        "data_ingestion.py",
        "data_transformation.py",
        "model_evaluation.py",
        "model_trainer.py",
        "model_pusher.py"
    ],
    "configuration": [
        "s3_operations.py"
    ],
    "constant": [],
    "entity": [
        "artifact_entity.py",
        "config_entity.py"
    ],
    "exception": [],
    "logger": [],
    "pipeline": [
        "prediction_pipeline.py",
        "train_pipeline.py"
    ],
    "utils": [
        "main_utils.py"
    ],
    "ml/feature": [],
    "ml/models": []
}

# Get the directory where the script is located
base_path = os.path.dirname(os.path.abspath(__file__))

# Function to create directories and files
def create_project_structure(base_path):
    for folder, files in folders.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                pass  # Create an empty file

# Create the structure in the script's directory
create_project_structure(base_path)

print("Project structure created successfully in the same folder as this script!")

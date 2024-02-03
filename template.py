import os

file_paths = [
    "./README.md",
    "./requirements.txt",
    "./config/g_config.yaml",
    "./documentation/project_documentation.docx",
    "./scripts/main.py",
    "./scripts/code/__init__.py",
    "./scripts/code/components/__init__.py",
    "./scripts/code/config/__init__.py",
    "./scripts/code/config/l_config.yaml",
    "./scripts/code/utilities/__init__.py",
    "./scripts/code/utilities/common_utils.py",
    "./scripts/code/utilities/db_utils.py",
    "./scripts/code/logging/__init__.py",
    "./scripts/logs/__init__.py",
    "./scripts/code/pipelines/__init__.py",
    "./scripts/code/pipelines/data_gathering.py",
    "./scripts/code/pipelines/data_preparation.py",
    "./scripts/code/pipelines/model_training.py",
    "./scripts/code/pipelines/model_inferencing.py",
]

for path in file_paths:
    if not os.path.isfile(path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, "w") as file:
            file.write("")
        print(f"File created: {path}")
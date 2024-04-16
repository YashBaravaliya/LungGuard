import os
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")


MLFLOW_TRACKING_URI = "https://dagshub.com/YashBaravaliya/LungGuard.mlflow"
MLFLOW_TRACKING_USERNAME = "YashBaravaliya"
MLFLOW_TRACKING_PASSWORD = "dccbf6bb1455433d1334e5707014fe7da9d06553"

# Set environment variables
os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
os.environ["MLFLOW_TRACKING_USERNAME"] = MLFLOW_TRACKING_USERNAME
os.environ["MLFLOW_TRACKING_PASSWORD"] = MLFLOW_TRACKING_PASSWORD
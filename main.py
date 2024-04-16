import os
from cnnClassifier import logger
from cnnClassifier.pipeline.pipe_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.pipe_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.pipe_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.pipe_04_model_evaluation_with_mlflow import ModelEvaluationPipeline
from cnnClassifier.constants import MLFLOW_TRACKING_URI,MLFLOW_TRACKING_PASSWORD,MLFLOW_TRACKING_USERNAME


if __name__ == "__main__":

    os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
    os.environ["MLFLOW_TRACKING_USERNAME"] = MLFLOW_TRACKING_USERNAME
    os.environ["MLFLOW_TRACKING_PASSWORD"] = MLFLOW_TRACKING_PASSWORD

    STAGE_NAME = "Data Ingestion"
    """
    try:
        logger.info("Starting Data Ingestion Pipeline")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info("Data Ingestion Pipeline completed")
    except Exception as e:
        logger.error(f"Error in Data Ingestion Pipeline: {str(e)}")
        raise e
    """
    
    STAGE_NAME = "Prepare Base Model"
    
    try:
        logger.info("Starting Prepare Base Model Pipeline")
        pipeline = PrepareBaseModelPipeline()
        pipeline.run()
        logger.info("Prepare Base Model Pipeline completed")
    except Exception as e:
        logger.error(f"Error in Prepare Base Model Pipeline: {str(e)}")
        raise e
    
    STAGE_NAME = "Training"
    
    try:
        logger.info(f"Running stage: {STAGE_NAME}")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Completed stage: {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "MODEL EVALUATION"
    
    try:
        logger.info(f"Running stage: {STAGE_NAME}")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Completed stage: {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e

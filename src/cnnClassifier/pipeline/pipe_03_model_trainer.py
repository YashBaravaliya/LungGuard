from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

class ModelTrainerPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.config = self.config_manager.get_training_config()
        self.training = Training(self.config)

    def run(self):
        logger.info("Running stage: Model Training")
        self.training.train_model()
        logger.info("Completed stage: Model Training")

if __name__ == "__main__":
    try:
        logger.info("Starting Model Training Pipeline")
        pipeline = ModelTrainerPipeline()
        pipeline.run()
        logger.info("Model Training Pipeline completed")
    except Exception as e:
        logger.error(f"Error in Model Training Pipeline: {str(e)}")
        raise e
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(f"Running stage: {STAGE_NAME}")
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        logger.info(f"Completed stage: {STAGE_NAME}")


if __name__ == '__main__':
    try:
        logger.info(f"Running stage: {STAGE_NAME}")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Completed stage: {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
        
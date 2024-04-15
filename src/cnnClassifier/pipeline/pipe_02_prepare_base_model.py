from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.config = self.config_manager.get_prepare_base_model_config()
        self.prepare_base_model = PrepareBaseModel(self.config)

    def run(self):
        logger.info(f"Running stage: {STAGE_NAME}")
        self.prepare_base_model.get_base_model()
        self.prepare_base_model.update_base_model()
        logger.info(f"Completed stage: {STAGE_NAME}")

if __name__ == "__main__":
    try:
        logger.info("Starting Prepare Base Model Pipeline")
        pipeline = PrepareBaseModelPipeline()
        pipeline.run()
        logger.info("Prepare Base Model Pipeline completed")
    except Exception as e:
        logger.error(f"Error in Prepare Base Model Pipeline: {str(e)}")
        raise e
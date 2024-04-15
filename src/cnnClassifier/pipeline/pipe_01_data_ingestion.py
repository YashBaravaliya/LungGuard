from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger   

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.config = self.config_manager.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(self.config)

    def run(self):
        logger.info(f"Running stage: {STAGE_NAME}")
        self.data_ingestion.download_file()
        self.data_ingestion.extract_zip_file()
        logger.info(f"Completed stage: {STAGE_NAME}")


if __name__ == "__main__":
    try:
        logger.info("Starting Data Ingestion Pipeline")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info("Data Ingestion Pipeline completed")
    except Exception as e:
        logger.error(f"Error in Data Ingestion Pipeline: {str(e)}")
        raise e
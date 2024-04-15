import os
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evalution import Evaluation
from cnnClassifier import logger

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/YashBaravaliya/LungGuard.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="YashBaravaliya"
os.environ["MLFLOW_TRACKING_PASSWORD"]="dccbf6bb1455433d1334e5707014fe7da9d06553"

STAGE_NAME = "MODEL EVALUATION"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f"Running stage: {STAGE_NAME}")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Completed stage: {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
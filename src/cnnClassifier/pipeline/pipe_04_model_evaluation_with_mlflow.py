from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evalution import Evaluation
from cnnClassifier import logger

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
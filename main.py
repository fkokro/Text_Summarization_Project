from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarization.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarization.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarization.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> Finished {STAGE_NAME} <<<<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> Finished {STAGE_NAME} <<<<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> Finished {STAGE_NAME} <<<<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> Finished {STAGE_NAME} <<<<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>> Finished {STAGE_NAME} <<<<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e
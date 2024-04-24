from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarization.logging import logger


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> Finished {STAGE_NAME} <<<<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e
from textSummarization.config.configuration import ConfigurationManager
from Text_Summarization_Project.src.textSummarization.components.data_transformation import DataTransformation
from textSummarization.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
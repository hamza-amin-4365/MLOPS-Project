from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject import logger

STAGE_NAME = "Data Validation"

class DataValidationStage:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate()
        
if __name__ =='__main__':
    try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataValidationStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject import logger
from pathlib import Path
import json

STAGE_NAME = "Data Transformation"

class DataTransformationStage:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/stats.json"), "r") as f:
                status = json.load(f)

            column_validation_status = status.get("column_validation_status", False)
            datatype_validation_status = status.get("datatype_validation_status", False)

            if column_validation_status and datatype_validation_status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.split_dataset()
            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            print(e)
        
if __name__ =='__main__':
    try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataTransformationStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e
        
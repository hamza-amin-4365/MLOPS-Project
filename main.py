from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionStage
from src.mlProject.pipeline.stage_02_data_validation import DataValidationStage
from src.mlProject.pipeline.stage_03_data_transfromation import DataTransformationStage



STAGE_NAME = "Data Ingestion"
try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataIngestionStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e

STAGE_NAME = "Data Validation"
try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataValidationStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e

STAGE_NAME = "Data Transformation"
try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataTransformationStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e
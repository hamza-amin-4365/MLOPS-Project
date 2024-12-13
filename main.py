from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionStage

STAGE_NAME = "Data Ingestion"
try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataIngestionStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e
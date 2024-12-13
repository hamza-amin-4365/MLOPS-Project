from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_ingetsion import DataIngestion
from src.mlProject import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionStage:
    def __init__(self):
        pass
    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
if __name__ =='__main__':
    try:
        logger.info(f">>>>>>>>>>Starting {STAGE_NAME} Stage<<<<<<<<<<")
        stage = DataIngestionStage()
        stage.main()
        logger.info(f">>>>>>>>>>Completed {STAGE_NAME} Stage<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e
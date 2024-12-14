from src.mlProject import logger
from src.mlProject.entity.config_entity import DataValidationConfig
import pandas as pd
import json
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    logger.error(f"Column {col} is not in the schema.")
                    return False
                else:
                    logger.info(f"Column {col} is valid.")
            return True
        except Exception as e:
            logger.exception("Exception occurred during column validation.")
            raise e

    def validate_column_datatype(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema

            for col in all_cols:
                if all_schema[col] != str(data[col].dtype):
                    logger.error(f"Data type of column {col} is {data[col].dtype}, expected {all_schema[col]}.")
                    return False
                else:
                    logger.info(f"Data type of column {col} is valid.")
            return True
        except Exception as e:
            logger.exception("Exception occurred during data type validation.")
            raise e

    def validate(self):
        try:
            column_validation_status = self.validate_all_columns()
            datatype_validation_status = self.validate_column_datatype()

            validation_status = {
                "column_validation_status": column_validation_status,
                "datatype_validation_status": datatype_validation_status
            }

            logger.info("Validation status: {}".format(validation_status))

            # Ensure the directory for STATUS_FILE exists
            status_file_dir = Path(self.config.STATUS_FILE).parent
            status_file_dir.mkdir(parents=True, exist_ok=True)

            with open(self.config.STATUS_FILE, 'w') as f:
                json.dump(validation_status, f)
                logger.info("Validation status written to {}".format(self.config.STATUS_FILE))

            return validation_status
        except Exception as e:
            logger.exception("Exception occurred during validation: {}".format(str(e)))
            raise e

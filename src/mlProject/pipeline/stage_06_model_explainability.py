from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_explainability import ModelExplainability
from src.mlProject import logger

STAGE_NAME = "Model Explainability"

class ModelExplainabilityPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_explainability_config = config.get_model_explainability_config()
            model_explainability = ModelExplainability(config=model_explainability_config)
            model_explainability.explain_model()
        except Exception as e:
            logger.error(f"Error in Model Explainability Pipeline: {e}")
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelExplainabilityPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
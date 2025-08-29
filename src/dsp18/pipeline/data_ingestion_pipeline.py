from src.dsp18.config.configuration import ConfigurationManager
from src.dsp18.components.data_ingestion import DataIngestion    
from src.dsp18 import logger
from pathlib import Path




STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        print("Artifacts root exists:", Path("artifacts").exists())
        print("Data ingestion dir exists:", Path("artifacts/data_ingestion").exists())
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_data()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.init()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise e

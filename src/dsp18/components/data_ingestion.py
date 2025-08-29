import os
import urllib.request as request
from src.dsp18 import logger
import zipfile
from src.dsp18.entity.config_entity import (DataIngestionConfig)

## Component-DataIngestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists.")

    # Unzipping the downloaded file

    def unzip_data(self):
        """
        zip_file_path: str
        Extracts the contents of a zip file to a specified directory.
        Function returns None.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Data unzipped to {self.config.unzip_dir}")

    
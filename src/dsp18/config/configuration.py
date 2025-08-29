from src.dsp18.constants import *
from src.dsp18.utils.common import read_yaml, create_directories
from src.dsp18.entity.config_entity import DataIngestionConfig
from src.dsp18.entity.config_entity import ValidationConfig

class ConfigurationManager:
    def __init__(self, config_filepath=config_filepath, params_filepath=params_filepath, schema_filepath=schema_filepath):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
    
    def get_data_validation_config(self) -> ValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])
        
        return ValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_dir=config.unzip_dir,
            all_schema=schema
        )
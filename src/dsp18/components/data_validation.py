from src.dsp18.entity.config_entity import ValidationConfig
import pandas as pd


# Component-Data Validation
class DataValidation:
    def __init__(self, config: ValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for column in all_cols:
                if column not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True

        except Exception as e:
            raise e

        return validation_status
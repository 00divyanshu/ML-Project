from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.logger import logging

if __name__ == "__main__":
    try:
        # Step 1: Data Ingestion
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()

        # Step 2: Data Transformation
        transformation = DataTransformation()
        train_arr, test_arr, _ = transformation.initiate_data_transformation(
            train_path, test_path
        )

        # Step 3: Model Training
        model_trainer = ModelTrainer()
        r2_score_value = model_trainer.initiate_model_trainer(
            train_arr, test_arr
        )

        logging.info(f"Final R2 Score: {r2_score_value}")
        print(f"Final R2 Score: {r2_score_value}")

    except Exception as e:
        raise e
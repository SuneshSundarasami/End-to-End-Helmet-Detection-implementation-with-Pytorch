from Helmet_Detection_PyTorch.pipeline.train_pipeline import TrainPipeline
from Helmet_Detection_PyTorch.logger import logging

train_pipeline = TrainPipeline()
train_pipeline.run_pipeline()
logging.info("successfully completed Data Ingestion!")
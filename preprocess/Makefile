SHELL := /bin/bash

include .env

.EXPORT_ALL_VARIABLES:

.PHONY: upload-dags-to-bucket
upload-dags-to-bucket:
	@echo "Uploading dags to $(S3_BUCKET_NAME)..."
	s3cmd put --recursive dags/ s3://$(S3_BUCKET_NAME)/dags/
	@echo "DAGs uploaded successfully"

.PHONY: upload-src-to-bucket
upload-src-to-bucket:
	@echo "Uploading src to $(S3_BUCKET_NAME)..."
	s3cmd put --recursive src/ s3://$(S3_BUCKET_NAME)/src/
	@echo "Src uploaded successfully"

.PHONY: upload-data-to-bucket
upload-data-to-bucket:
	@echo "Uploading data to $(S3_BUCKET_NAME)..."
	s3cmd put --recursive input_data/*.txt s3://$(S3_BUCKET_NAME)/input_data/
	@echo "Data uploaded successfully"

.PHONY: download-output-data-from-bucket
download-output-data-from-bucket:
	@echo "Downloading output data from $(S3_BUCKET_NAME)..."
	s3cmd get --recursive s3://$(S3_BUCKET_NAME)/output_data/ output_data/
	@echo "Output data downloaded successfully"



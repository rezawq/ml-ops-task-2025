#!/bin/bash

# Функция логирования
function log() {
    sep="----------------------------------------------------------"
    echo "[$(date)] $sep "
    echo "[$(date)] [INFO] $1"
}

TARGET_BUCKET=rezawq-bucket-b1g13sct68pr90ornldm

hadoop distcp /user/ubuntu/data_convert/data.parquet s3a://$TARGET_BUCKET/
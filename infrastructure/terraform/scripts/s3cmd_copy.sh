#!/bin/bash

# Функция для логирования
function log() {
    sep="----------------------------------------------------------"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $sep " | tee -a $HOME/s3cmd_copy.log
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [INFO] $1" | tee -a $HOME/s3cmd_copy.log
}

log "Starting user data script execution"


# Устанавливаем s3cmd
log "Installing s3cmd"
sudo apt-get install -y s3cmd


# Настраиваем s3cmd
log "Configuring s3cmd"
cat <<EOF > /home/ubuntu/.s3cfg
[default]
access_key = ${access_key}
secret_key = ${secret_key}
host_base = storage.yandexcloud.net
host_bucket = %(bucket)s.storage.yandexcloud.net
use_https = True
EOF

chown ubuntu:ubuntu /home/ubuntu/.s3cfg
chmod 600 /home/ubuntu/.s3cfg

# Определяем целевой бакет
TARGET_BUCKET=${s3_bucket}


# Копируем конкретный файл из исходного бакета в наш новый бакет
log "Copying file from source bucket to destination bucket"
FILE_NAME="2022-11-04.txt"
s3cmd cp \
    --config=/home/ubuntu/.s3cfg \
    --acl-public \
    s3://otus-mlops-source-data/$FILE_NAME \
    s3://$TARGET_BUCKET/$FILE_NAME

# Проверяем успешность копирования
if [ $? -eq 0 ]; then
    log "File $FILE_NAME successfully copied to $TARGET_BUCKET"
    log "Listing contents of $TARGET_BUCKET"
    s3cmd ls --config=/home/ubuntu/.s3cfg s3://$TARGET_BUCKET/
else
    log "Error occurred while copying file $FILE_NAME to $TARGET_BUCKET"
fi
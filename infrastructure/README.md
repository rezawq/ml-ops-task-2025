# Инфраструктура 

Разворачивается с помощью Terraform в облаке Yandex.


### 1. Создание нового bucket

Смотри описание ресурса ```resource "yandex_storage_bucket" "data_bucket"``` в [main.tf](terraform/main.tf)

Создать инфрастуктуру (втч bucket)
```bash
make tf_apply
```

После создания бакет доступен по адресу s3://rezawq-bucket-b1g13sct68pr90ornldm или https://storage.yandexcloud.net/rezawq-bucket-b1g13sct68pr90ornldm/

### 2. Копирование из s3://otus-mlops-source-data/ в новый bucket

#### Способ вручную

```bash
# Устанавливаем s3cmd
sudo apt-get install -y s3cmd
```

```bash
# Настраиваем s3cmd

cat <<EOF > ~/.s3cfg
[default]
access_key = ${access_key}
secret_key = ${secret_key}
host_base = storage.yandexcloud.net
use_https = True
EOF
```

Значения `access_key` и `secret_key` берем из [terraform.tfstate](terraform/terraform.tfstate) после применения ```make tf_apply```

```bash
# Копируем
TARGET_BUCKET=aresh2025-bucket-b1gdo3s8323p2nfiiqgl
s3cmd sync --acl-public  s3://otus-mlops-source-data/ s3://$TARGET_BUCKET/
```

Желательно выполнить на каком-то хосте в облаке, чтобы копирование файлов шло внутри облака (быстрее).

### 3. Создание Spark-кластера

Описан в [main.tf](terraform/main.tf)

### 4. Копирование содержимого хранилища в файловую систему HDFS

```ssh
ssh -l ubuntu 158.160.38.21
```
IP динамический, смотреть в консоли облака

```bash
# Создаем директорию в HDFS
hdfs dfs -mkdir -p /user/ubuntu/data
```


```bash
# Копируем все данные
s3_bucket=aresh2025-bucket-b1gdo3s8323p2nfiiqgl
hadoop distcp s3a://$s3_bucket/ /user/ubuntu/data
```


```bash
# Выводим содержимое директории для проверки
hdfs dfs -ls /user/ubuntu/data
```

### 5. Jump Server

#### Ключевая пара для ssh

Выполните интерактивную команду:

```bash
ssh-keygen -t ed25519
```

> Note: Назовите ключ `yc`. В противном случае измените переменную `SSH_PUBLIC_KEY_PATH` в файле `env.sh` и используйте свой путь к ключу в соответствующих командах.


### Копирование данных

```bash
DATAPROC_MASTER_FQDN=$(yc compute instance list --format json | jq -r '.[] | select(.labels.subcluster_role == "masternode") | .fqdn')
echo $DATAPROC_MASTER_FQDN
```

```bash
ssh -i ~/.ssh/yc ubuntu@<proxy_public_ip>
```

```bash
ssh ubuntu@$DATAPROC_MASTER_FQDN
./upload_data_to_hdfs.sh
```




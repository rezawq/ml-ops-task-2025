# Инфраструктура 

Разворачивается с помощью Terraform в облаке Yandex.


### 1. Создание нового bucket

Смотри описание ресурса ```resource "yandex_storage_bucket" "data_bucket"``` в [main.tf](terraform/main.tf)

Создать инфрастуктуру (втч bucket)
```bash
make tf_apply
```

### 2. Копирование из s3://otus-mlops-source-data/ в новый bucket

#### Способ вручную

```bash
# Устанавливаем s3cmd
sudo pip install s3cmd
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



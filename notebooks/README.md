# Анализ данных


### Проброс порта для Jupyter

```bash
PROXY_PUBLIC_IP=158.160.56.161
DATAPROC_MASTER_FQDN=$(yc compute instance list --format json | jq -r '.[] | select(.labels.subcluster_role == "masternode") | .fqdn')
echo $DATAPROC_MASTER_FQDN

# Проброс порта с вашей машины на Jump Server
ssh -i ~/.ssh/yc -L 8888:localhost:8888 ubuntu@$PROXY_PUBLIC_IP

# Проброс порта с Jump Server на мастер-ноду
ssh -i .ssh/yc -L 8888:localhost:8888 ubuntu@$DATAPROC_MASTER_FQDN

# Запуск Jupyter
jupyter notebook
```

### Получаем URL для подключения к Jupyter Notebook


## Загрузка в бакет
[upload_to_bucket.sh](upload_to_bucket.sh)
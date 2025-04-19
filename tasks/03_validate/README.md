# Регулярное переобучение модели обнаружения мошенничества

1. Создать инфраструктуру с помощью [infra](../../infra)
2. Сконфигурировать Apache Airflow c помощью [variables.json](../../infra/variables.json)
3. Отконфигурить локальный конфиг s3 ```nano .s3cfg```
4. Загрузка

```bash
# Создать и загрузить виртуальное окружение
make create-venv-archive
make upload-venv-to-bucket

# Загрузить исходный код модели
make upload-src-to-bucket

# Загрузить DAG файлы
make upload-dags-to-bucket

# Загрузить данные в S3
make upload-data-to-bucket

# Или выполнить полное развертывание одной командой
make deploy-full
```

5. Фильтрация логов в кластере по фильтру json_payload.yarn_log_type = stdout
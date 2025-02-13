# Анализ данных


### Копируем ноутбуки на мастер-ноду 

```bash
# Сперва на jump-сервер
scp -i ~/.ssh/yc notebooks/*.ipynb {публичный-IP-вашей-ВМ}:

# Потом идем на jump-сервер
ssh -i ~/.ssh/yc {публичный-IP-вашей-ВМ}

# И копируем файлы на мастер-ноду
scp -i ~/.ssh/yc *.ipynb ubuntu@{fqdn-мастер-ноды}:
```

### Попадаем через Jupyter

```bash
# Проброс порта с вашей машины на Jump Server
ssh -i ~/.ssh/yc -L 8888:localhost:8888 {публичный-IP-вашей-ВМ}

# Проброс порта с Jump Server на мастер-ноду
ssh -i .ssh/yc -L 8888:localhost:8888 ubuntu@{fqdn-мастер-ноды}

# Запуск Jupyter
jupyter notebook
```
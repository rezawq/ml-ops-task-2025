# Предварительный анализ задачи определения мошеннических финансовых операций

## Цель

1. Проектирование системы выявления мошеннических операций для компании, предоставляющей банковские услуги.
2. Сбор требований к системе
3. Определение состава работ

## Требования

### Бизнес-требования

1. Бюджет - 10 млн. рублей
2. Срок - 3 месяца на MVP
3. Число ложно-отрицательных срабатываний не должно превышать 2%
4. Число ложно-положительных срабатываний не должно превышать 5%

### Функциональные требования

1. Система должна получать на вход информацию о транзакции. Формат передачи данных - csv файл, каждая строка
   соответствует одной транзакции.
2. Система должна определять что транзакция мошенническая или нет.

### Нефункциональные требования

1. Производительность системы должна быть достаточной, для того, чтобы обрабатывать пиковые значения 400 транзакций в
   секунду при среднем числе 50 транзакций в секунду.
2. Собственные сервера заказчик под разрабатываемый модель не выделяет.
3. Информация о транзакциях является конфиденциальной, ее
   утечка недопустима. 



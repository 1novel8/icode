# Как запустить проект
1. Склонировать проект
2. Создать файл .env в корне проекта с этим содержимым:
```
  POSTGRES_NAME=postgres
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_HOST_AUTH_METHOD=trust
  POSTGRES_PORT=5432
  POSTGRES_HOST=localhost
  TIMEZONE=Europe/Minsk
  ```
3. Запустить базу с помощью Docker
   ```
   docker-compose up --build -d
   ```
4. Запустить **main.py** 

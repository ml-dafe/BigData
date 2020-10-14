
### Часть 1 - Работа с HDFS

1. Переходим на сайт [Cloudera](https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html)
2. Выбираем Docker в Installation Type и нажимаем LET'S GO!  
3. Запускаем `bash docker-deploy-hdp30.sh`
4. Открываем `http://localhost:1080`

### Часть 2 - Работа с образами
Создание образов:
1. Скопируйте свой скрипт для чтения данных из очереди для решения кейса в папку `consumer/src`
2. Создайте файл Dockerfile в директории `consumer/` в котором в качестве базового образа будет [Python](https://hub.docker.com/_/python), для этого используйте диррективу `FROM`
3. С помощью диррективы `RUN` установите в образе все зависимости. Вы можете попробовать вынести их вотдельный файл requirements.txt
4. С помощью диррективы `COPY` поместите в контейнер файлы вашего приложения из `consumer/src` и укажите `WORKDIR`
5. Финализируйте файл запуском приложения, например так `CMD [ "python", "./*название скрипта*" ]`
Сборка образа и запуск контейнера: 
1. Соберите образ `docker build -t image_name . ` и проверьте с помощью `docker images`
2. Запустите контейнер `docker run -d consumer` и проверьте с помощью `docker ps`

### Часть 3 - Оркестрирование контейнеров 
1. Создайте файл `docker-compose.yml` 
2. Запишите в нем: 
```
version: "3.8"
services:
  consumer:
    build:
      context: ./consumer
```
3. Запустите `docker-compose up -d`
4. Остановите оркестратор с помощью команды `docker-compose down`
5. Попробуйти примаунтить папку внутрь контейнера с помощью директивы `volumes` и перезапустите контейнер
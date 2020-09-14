# BigData

## Кейс «Контроль и диагностика»
В рамках данного кейса предлагается решить задачу предиктивной аналитики - прогнозирование отказа двигателя самолета в режиме реального времени. Под отказом в данном случае понимается вывод двигателя на обслуживание.   

В ходе эксплуатации двигателя происходит постепенное ухудшение характеристик двигателя. Это называется нормальной деградацией.   

Первые 100-200 полётов идёт "приработка" двигателя. Характеристики двигателя приходят в установившееся состояние. По завершении приработки процесс установления параметров завершился, но двигатель всё ещё можно считать совершенно новым. Это состояние называется эталонным, значения параметров в этом состоянии - эталонными значениями. В число таких параметров как правило входят: температура выхлопных газов, относительные частоты вращения валов, давление в различных зонах двигателя, расход топлива и так далее.  

Дальше начинается процесс нормальной деградации параметров двигателя. Выявление аномальной деградации характеристик позволяет предсказать надвигающуюся поломку. Искусственный интеллект в данном случае интересен тем, что дает перспективу выявить незамеченные ранее тренды и получить конкурентное преимущество.   

По условиям задачи информация поступает с 21 датчика, в одном из трех режимов работы. Информация о расположении, устройстве датчиков и конкретном значении их данных не раскрывается. Данные поступают в режиме реального времени через брокер сообщений mqtt. На основе этих данных нужно решить несколько задач:
- классификации (будет ли выведен в ремонт двигатель через n циклов)
- регрессии (предсказать сколько циклов осталось до вывода в ремонт после прохождения m циклов). 
- поиск детектирования в данных  
  
После реализации алгоритмов, нужно оценить качество его работы на исторических данных.  

### Предпоcылки и условия 
Каждый двигатель после различного количества циклов выводится в ремонт (перестают поступать данные с этого двигателя)
Время и условия вывода в работу нового двигателя - недоступны. 
В каждый момент времени в работе находится от 1 до 50 двигателей.
Для каждого двигателя:
Существует уникальный ID (двигатель после ремонта считаем новым). 
Каждый цикл с двигателя поступают данные: 
- Информация о режимах работы: 
Два поля «setting1» и «setting2» заданы вещественными числами. Пример режимов работы одного двигателя для периода из 5 циклов представлен ниже:  


id|cycle|setting1|setting2 
--- | --- | --- | --- | 
1|1|-0,0007|-0,0004
1|2|0,0019|-0,0003
1|3|-0,0043|0,0003
1|4|0,0007|0
1|5|-0,0019|-0,0002

- Информация с датчиков
Поля «s1», «s2», …, «s21» заданы вещественными числами.
Пример данных с датчиков одного двигателя для периода из 5 циклов представлен ниже:  

id|cycle|s1|s2|…|s21
--- | --- | --- | --- | --- | --- | 
1|1|518,67|641,82||23,419
1|2|518,67|642,15||23,4236
1|3|518,67|642,35||23,3442
1|4|518,67|642,35||23,3739
1|5|518,67|642,37||23,4044

Существует брокер сообщений mqtt в который поступают данные о каждом двигателе. 

Задача 
1. Подключиться к внешнему брокеру сообщений mqtt c потоком данных в режиме реального времени. 
2. Реализовать программу для чтения входящих сообщений с данными о двигателях и их сохранения в хранилище. 
3. Реализовать хранилище для данных, учитывая их структуру. Предусмотреть, что хранилище должно быть горизонтально масштабируемым. Выбор хранилища требуется обосновать. 
4. Проанализировать данные, найти зависимости и закономерности. Сгенерировать новые признаки на основе существующих, расчитывать их в режиме реального времени и сохранять в хранилище. 
5. Реализовать алгоритм (например, машинного обучения) для решения задачи классификации (будет ли выведен в ремонт двигатель через n циклов) и/или регрессии (предсказать сколько циклов осталось до вывода в ремонт после прохождения m циклов). Оценить качество работы алгоритма(ов) на исторических данных. 
6. Реализовать применение алгоритма из п.4 на потоке данных в режиме реального времени. Собирать оценку качества работы алгоритма(ов) на потоковых данных. 
7. Построить систему для визуализации в реальном времени: Данных, прогнозов, метрик и других необходимых параметров

Для реализации указанных выше задач, студенту так же необходимо: 
1. Выбрать технологии и обосновать его, например: 
для работы с потоковыми данными: Java, Scala, Python, Kafka Streams, Spark Streams, etc
для Хранения данных: Hive, HBase, Casandra, etc
для визуализации Superset, Grafana, etc
2. Комплексное проектирование системы 
3. Все решение должно быть собрано в контейнеры Docker и должно разворачиваться на любой *nix машине с помощью системы оркестрации Docker Compose. Дополнительным плюсом является реализация развертывания на кластере из нескольких машин.

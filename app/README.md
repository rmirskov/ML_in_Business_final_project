Итоговый проект курса "Машинное обучение в бизнесе" от GeekBrains.

Данные взяты с https://archive.ics.uci.edu/ml/datasets/Adult
В проекте решается задача бинарной классификации - предсказание годового дохода людей (>50K или <=50K) по ряду параметров.

Используемые признаки:

    Раса (race) *набор данных 1994 года
    Пол (sex)
    Возраст (age)
    Страна проживания (native-country)
    Категория работника (workclass)
    Образование (education)
    Количество лет обучения (education-num)
    Сфера деятельности (occupation)
    Количество рабочих часов в неделю (hours-per-week)
    Семейное положение (marital-status)
    Отношения (relationship)
    Прирост капитала (capital_gain)
    Потеря капитала (capital_loss)

Преобразования признаков:
    категориальные признаки - LabelEncoder + MinMaxScaler
    числовые признаки - MinMaxScaler

Модель: GradientBoostingClassifier

Клонируем репозиторий

$ git clone <path_to_repo>

Переходим в папку, куда склонирован репозиторий и запускаем сборку образа

$ docker build -t <name_image> .

Запускаем контейнер

$ docker run -d -p 5000:5000 <name_image>

Переходим на localhost:5000

# Сайт доставки еды [Star Burger](https://dexter-superstar.ru/)

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню ресторанов Star Burger.

## Требования к запуску

Для начала необходимо установить [Docker](https://www.docker.com/): для локальной машины подойдёт установка [Docker Desktop](https://docs.docker.com/desktop/), для удалённых серверов следует использовать гайд по установке [Docker Engine](https://docs.docker.com/engine/install/).

## Как запустить dev-версию сайта

Определите переменные окружения, создав файл `.env` в каталоге `star_burger/`, и положите туда такой код:
```sh
SECRET_KEY=django-insecure-0if40nf4nf93n4
GEOCODER_YANDEX_API_KEY=<API KEY Янекс Геокодера>
ROLLBAR_TOKEN=<ROLLBAR_TOKEN>
ROLLBAR_ENVIRONMENT=development
ROLLBAR_NAME=<ROLLBAR_NAME>
POSTGRES_USER=<Имя пользователя Postgres, который будет создан при инициализации базы>
POSTGRES_PASSWORD=<пароль для пользователя Postgres>
POSTGRES_DB=<название базы данных, например star_burger>
```

Получить `GEOCODER_YANDEX_API_KEY` можно в кабинете разработчика [Яндекса](https://developer.tech.yandex.ru/). В меню выбора API выбираем `JavaScript API и HTTP Геокодер` и заполняем информационную форму.

`ROLLBAR_TOKEN` - токен сервиса для отслеживания ошибок в программном коде веб-приложений [Rollbar](https://rollbar.com/). Перейдите по ссылке, зарегестрируйтесь, при выборе SDK укажите **Django**, на шаге `Set up SDK` ищите строку `access_token` в ней и будет указан ваш токен.

`ROLLBAR_ENVIRONMENT` отвечает за классификацию среды при считывании ошибок в Rollbar и может принимать любое значение.

`ROLLBAR_NAME` - имя пользователя в Rollbar.

Запустите сборку Docker-образа командой:

```
docker-compose -f docker-compose.yml build
```
Запустите Docker-контейнеры:
```
docker-compose -f docker-compose.yml up -d
```
### Открытие сайта
Перейдите по ссылке http://localhost/

## Как запустить prod-версию сайта

Определите переменные окружения, создав файл `.env` в каталоге `star_burger/`, и положите туда такой код (подробности смотри выше):
```sh
ALLOWED_HOSTS=<ALLOWED_HOSTS>
DEBUG=False
SECRET_KEY=<секретный ключ проекта>
GEOCODER_YANDEX_API_KEY=<API KEY Янекс Геокодера>
export ROLLBAR_TOKEN=<ROLLBAR_TOKEN>
export ROLLBAR_ENVIRONMENT=production
export ROLLBAR_NAME=<ROLLBAR_NAME>
POSTGRES_USER=<Имя пользователя Postgres, который будет создан при инициализации базы>
POSTGRES_PASSWORD=<пароль для пользователя Postgres>
POSTGRES_DB=<название базы данных, например star_burger>
```
`ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

Запустите сборку Docker-образа командой:

```
docker-compose -f docker-compose.yml build
```
Запустите Docker-контейнеры:
```
docker-compose -f docker-compose.yml up -d
```

## Автоматизация деплоя

Для автоматизации деплоя запустите `bash-скрипт` с названием `deploy_star_burger.sh` из папки с проектом со следующей командой:

```bash
./deploy_star_burger.sh
```
**!ВАЖНО!** Перед запуском проверьте все абсолютные пути в скрипте - они могут отличаться от приведённого примера в зависимости от сборки системы.

В случае возникновения ошибки `Killed...`, связанной с работой `npm`, создайте файл-подкачки на сервере:

```bash
 sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
 sudo /sbin/mkswap /var/swap.1
 sudo /sbin/swapon /var/swap.1
```

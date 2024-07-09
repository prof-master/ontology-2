# Онтологии

### Обновление пакетов на сервере
```Shell
sudo apt update
sudo apt upgrade
```

### Создание пользователя 
```Shell
sudo adduser <username>
sudo usermod -aG sudo username
```

### Перейдем на аккаунт пользователя
```Shell
su - <username>
```

### Установим необходимые зависимости
```
sudo apt install python3-pip python3-dev python3-venv libpq postgresql
sudo apt install postrgesql-contrlib nginx curl git
```

### Склонируем проект на сервер
```Shell
git clone <link to project>
```

### Настройка PostgreSQL
```Shell
sudo -u <datat base username> createuser --interactive
sudo -u <data base username> createdb <databasename>

sudo -u <datat base username> psql
```

После выполнения этих команд, октроется коммандная строка базы данных. С помощью sql-команды зададим пароль пользователя и выдадим ему привелегии. 
```SQL
ALTER USER username WITH ENCRYPTED PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE yourdatabase TO youruser;
```
Выйдем из коммандной строки sql.

### Создание виртуального окружения
Создадим и активируем виртуальное окружение 
```Shell
python3 -m venv <название окружения>
source <название окружения>/bin/activate
```

### Установим необходимые пакеты в окпужение
```Shell
pip3 install django gunicorn uwsgi psycopg2-binary
```

### Выйдем из виртуального окружения
```Shell
deactivate
```

### Настройки проекта
Откроем файл `settings.py` проекта и пропишем настройки
```Python
ALLOWED_HOSTS = ['your_server_domain','another_server_domain',...,'localhost']

DATABASE = {
    'default':{
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'your data base name',
        'USER' : 'your user',
        'PASSWORD' : 'yourpassword',
        'HOST' : 'localhost',
        'PORT' : '',
    }
}
```

Пропишем настройку статических файлов, для этого создадим папку
```Python
STATIC_ROOT = '/var/www/yourdomain/static/'
```
И укажем путь к статическим файлам
```Python
STATIC_URL = '/static/'
```

> [!TIP]
> В некоторых случаях может возникнуть ошибка **`403 Forbiden`** для этого нужно прописать команду:
>
> ```Shell
> sudo chown -R $USER:$USER /var/www/<your_domain>
> sudo chmod -R 755 /var/www/<your_domain>
> ```


### Применим миграции
```Shell
python managy.py makemigrations
python managy.py migrate
```

### Создадим пользователя администратора
```Shell
python managy.py createsuperuser
```

### Для копирования файлов в папку static 
```Shell
python manage.py collectstatic
```

### Настройка `gunicorn`
Создадим файл
```Shell
sudo nano /etc/systemd/system/gunicorn.socket
```

И пропишем в нем следующее
```
[Unit]
Description=gunicorn socket
[Socket]
ListenStream=/run/gunicorn.sock
[Install]
WantedBy=sockets.target
```

Создадим ещё один файл
```Shell
sudo nano /etc/systemd/system/gunicorn.service
```

И пропишем в нем следующее
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ontology
Group=www-data
WorkingDirectory=/home/usermane/myproject
ExecStart=/home/username/project/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          ontology_constructor.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Запустим и активируем гуникорн
```Shell
sudo systemctl start gunicorn
sudo systemctl start gunicorn.socket

sudo systemctl enable gunicorn
sudo systemctl enable gunicorn.socket
```

### Создадим файл `uwsgi.ini`
```
[uwsgi]
module = myproject.wsgi

#полный путь к директории Django проекта
chdir = /path/to/your/project

#Протокол и порт для прослушивания
http = :8000

#количество процессов и потоков
processes = 4
threads = 2

#файл процесса
pidfile = /path/to/your/project/uwsgi.pid

#лог файл
daemonize = /home/ontology/ontology_constructor/uwsgi.log
```

### Запустим uwsgi c файлом конфигурации
```Shell
uwsgi --ini uwsgi.ini
```

### Настройка Nginx

Создадим конфигурационный файл nginx
```
sudo nano /etc/nginx/sites-available/<yordomain>
```

Укажем в нем следующее
```
server {
    server_name your_domain;

    location /static/ {
        root /var/www/your_domain;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Создадим символьческую ссылку в папку `sites-enabled`
```Shell
sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled
```

> [!TIP]
> Рекомендую проверить конфигурацию nginx на наличие ошибок
> ```Shell
> sudo nginx -t
> ```

Для применения изменений перезагрузим nginx
```Shell
sudo systemctl restart nginx
```

Так же не забудем настроить брендмаузер для nginx
```Shell
sudo ufw allow 'Nginx Full' 
```

---

## Подключение ssl/tsl

Для подключения ssl/tsl мпожно воспользоваться certbot
```Shell
sudo snap install --classic certbot
sudo certbot --nginx
```